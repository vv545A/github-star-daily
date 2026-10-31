#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
用 GitHub REST API 把站点 + 构建脚本一次性推到 GitHub Pages。

为什么不用 git push：本机到 github.com:443 的通道被代理拦截，只有 api.github.com 可用。

为什么用 Git Data API 而不是逐个文件 PUT：
  逐个 PUT contents 每个文件都会产生一次提交，十几个文件就是十几次提交，
  会连续触发十几次 Pages 构建，容易互相打架报 errored。
  Git Data API 可以「建 blob → 建一棵树 → 建一个提交 → 移动分支引用」，
  所有文件落在同一个提交里，只触发一次构建。

用法：
    set GITHUB_TOKEN=ghp_xxx
    python deploy.py --repo github-star-daily
"""
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')

API = 'https://api.github.com'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 要发布到仓库的文件（相对路径）。抓取缓存、repos.jsonl 等中间产物不发布。
FILES = [
    'index.html',
    'README.md',
    '.nojekyll',
    '.gitignore',
    'assets/style.css',
    'assets/app.js',
    # 自动更新需要的构建链
    '.github/workflows/update-data.yml',
    '_build/fetch_all.py',
    '_build/build.py',
    '_build/topics.py',
    '_build/test.js',
    '_build/summary.js',
    '_build/deploy.py',
    '_build/anno1.py',
    '_build/anno2.py',
    '_build/anno3.py',
    '_build/anno4.py',
    '_build/anno5.py',
]

# 由 GitHub Actions 每天生成并维护的数据文件。
# 默认不推，否则会用本地旧快照覆盖掉 CI 刚抓的新数据。
# 只有首次建站（仓库里还没有数据）时才需要 --with-data 一起推上去。
DATA_FILES = [
    'assets/topics.js',
    'assets/data.js',
    'assets/data-extra.js',
]


def call(method, path, token, body=None, allow=()):
    url = API + path if path.startswith('/') else path
    data = json.dumps(body).encode('utf-8') if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header('Authorization', 'Bearer ' + token)
    req.add_header('Accept', 'application/vnd.github+json')
    req.add_header('X-GitHub-Api-Version', '2022-11-28')
    if data:
        req.add_header('Content-Type', 'application/json')
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            txt = r.read().decode('utf-8')
            return r.status, (json.loads(txt) if txt.strip() else {})
    except urllib.error.HTTPError as e:
        txt = e.read().decode('utf-8', 'replace')
        try:
            payload = json.loads(txt)
        except Exception:
            payload = {'raw': txt[:300]}
        if e.code in allow:
            return e.code, payload
        raise SystemExit(f'[失败] {method} {url} -> {e.code}\n{json.dumps(payload, ensure_ascii=False)[:600]}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default='github-star-daily')
    ap.add_argument('--desc', default='GitHub 万星开源项目每日推荐站 · 收录 1.1 万+ 千星项目')
    ap.add_argument('--private', action='store_true')
    ap.add_argument('--message', default='')
    ap.add_argument('--with-data', action='store_true',
                    help='连数据文件一起推（仅首次建站用；平时数据由 GitHub Actions 维护）')
    args = ap.parse_args()

    token = os.environ.get('GITHUB_TOKEN', '').strip()
    if not token:
        raise SystemExit('请先设置环境变量 GITHUB_TOKEN')

    st, me = call('GET', '/user', token)
    owner = me['login']
    print(f'[1/5] 身份：{owner}')

    # ---- 仓库 ----
    st, repo = call('GET', f'/repos/{owner}/{args.repo}', token, allow=(404,))
    if st == 200:
        print(f'[2/5] 仓库已存在：{repo["full_name"]}')
    else:
        st, repo = call('POST', '/user/repos', token, {
            'name': args.repo, 'description': args.desc, 'private': args.private,
            'has_issues': True, 'has_wiki': False, 'auto_init': False,
        })
        print(f'[2/5] 仓库已创建：{repo["full_name"]}')

    branch = repo.get('default_branch') or 'main'

    # 仓库里还没有数据文件（首次建站）时，自动把本地数据一起推上去
    if not args.with_data:
        st_data, _ = call('GET', f'/repos/{owner}/{args.repo}/contents/assets/data.js', token, allow=(404,))
        if st_data == 404:
            print('    仓库里还没有 assets/data.js，自动带上本地数据文件')
            args.with_data = True

    # ---- 收集本地文件 ----
    wanted = FILES + (DATA_FILES if args.with_data else [])
    if not args.with_data:
        print('    注意：数据文件由 GitHub Actions 每天维护，本次不推送（要推加 --with-data）')
    blobs = []
    total = 0
    for rel in wanted:
        fp = os.path.join(ROOT, rel)
        if not os.path.exists(fp):
            print(f'    [跳过] {rel} 不存在')
            continue
        raw = open(fp, 'rb').read()
        blobs.append((rel, raw))
        total += len(raw)

    # ---- 当前分支头 ----
    st, ref = call('GET', f'/repos/{owner}/{args.repo}/git/ref/heads/{branch}', token, allow=(404, 409))
    base_commit = ref.get('object', {}).get('sha') if st == 200 else None
    base_tree = None
    if base_commit:
        _, c = call('GET', f'/repos/{owner}/{args.repo}/git/commits/{base_commit}', token)
        base_tree = c['tree']['sha']

    # ---- 建 blob ----
    print(f'[3/5] 上传 {len(blobs)} 个文件（{total / 1024 / 1024:.2f} MB）：')
    entries = []
    for rel, raw in blobs:
        _, b = call('POST', f'/repos/{owner}/{args.repo}/git/blobs', token,
                    {'content': base64.b64encode(raw).decode('ascii'), 'encoding': 'base64'})
        entries.append({'path': rel, 'mode': '100644', 'type': 'blob', 'sha': b['sha']})
        print(f'    OK {rel:<40} {len(raw) / 1024:>8.1f} KB')

    # ---- 建树（base_tree 保留未列出的已有文件）----
    tree_body = {'tree': entries}
    if base_tree:
        tree_body['base_tree'] = base_tree
    _, tree = call('POST', f'/repos/{owner}/{args.repo}/git/trees', token, tree_body)

    # ---- 建提交 ----
    msg = args.message or f'deploy: 同步站点文件（{len(entries)} 个）'
    commit_body = {'message': msg, 'tree': tree['sha']}
    if base_commit:
        commit_body['parents'] = [base_commit]
    _, commit = call('POST', f'/repos/{owner}/{args.repo}/git/commits', token, commit_body)

    # ---- 移动分支 ----
    if base_commit:
        call('PATCH', f'/repos/{owner}/{args.repo}/git/refs/heads/{branch}', token, {'sha': commit['sha']})
    else:
        call('POST', f'/repos/{owner}/{args.repo}/git/refs', token,
             {'ref': f'refs/heads/{branch}', 'sha': commit['sha']})
    print(f'[4/5] 已提交：{commit["sha"][:8]}（单个提交，只触发一次 Pages 构建）')

    # ---- Pages ----
    if args.private:
        print('[5/5] 私有仓库跳过 Pages 配置（需要 GitHub Pro）')
    else:
        st, pg = call('POST', f'/repos/{owner}/{args.repo}/pages', token,
                      {'source': {'branch': branch, 'path': '/'}}, allow=(409, 422))
        print(f'[5/5] Pages：{"已配置" if st in (201, 409) else "返回 " + str(st)}')

    print()
    print('=' * 52)
    print('  仓库：', repo['html_url'])
    print('  网站：', f'https://{owner}.github.io/{args.repo}/')
    print('=' * 52)


if __name__ == '__main__':
    main()
