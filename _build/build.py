# -*- coding: utf-8 -*-
"""
构建前端数据文件

输入：repos.jsonl（fetch_all.py 抓的 GitHub 快照）+ anno*.py（人工中文标注）
输出：
    assets/data.js        —— 精选项目 + 全部 Star≥10000 项目（首屏加载）
    assets/data-extra.js  —— Star 5000~9999 项目（首屏后懒加载）

用法：python build.py
"""
import json, os, sys, datetime, collections

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, '..', 'assets')

import topics

# ---------------- 人工标注 ----------------
ANNO = {}
_mods = []
for name in ('anno1', 'anno2', 'anno3', 'anno4', 'anno5'):
    p = os.path.join(HERE, name + '.py')
    if not os.path.exists(p):
        continue
    m = __import__(name)
    _mods.append(name)
    ANNO.update(m.A)

# ---------------- 排除名单 ----------------
# 非技术内容、盗版/激活工具、翻墙代理、deepfake、攻击工具等，站内不展示。
# 注意：规则要精确，别误伤正常项目（例如 "Crack LeetCode" 是「攻克」的意思）
BLOCK = {
    '996icu/996.ICU',                                   # 劳工维权议题，非技术项目
    'TapXWorld/ChinaTextbook',                          # 盗版教材
    'massgravel/Microsoft-Activation-Scripts',           # Windows/Office 激活工具
    'TGSAN/CMWTAT_Digital_Edition',                     # 数字授权激活工具
    'xtekky/gpt4free',                                  # 绕过付费接口
    'eternity4719/HowToLiveBetter',                      # 生活类非技术内容
    'byoungd/up',                                       # 生活类非技术内容
}
import re

_BAD_PATTERNS = [
    r'\bkeygen\b', r'\bactivator\b', r'\bwarez\b', r'\bdeepfake',
    r'\bddos\b', r'\bbotnet\b', r'\brat(?:-client)?\b', r'\bstealer\b',
    r'phishing[- ]kit', r'\bpiracy\b',
    r'\b(software|game|app|windows|office|idm|adobe)[- ]crack',
    r'\bcrack(?:ed)?[- ](?:version|download|software|premiere|photoshop)',
    r'\bserial[- ]key\b', r'\bnulled\b',
]
_BAD_RE = re.compile('|'.join(_BAD_PATTERNS), re.I)

# 仓库名里带这些词的，属于代理/翻墙客户端
_PROXY_RE = re.compile(r'(v2ray|shadowsocks|clash|trojan|hysteria|sing-box|xray)', re.I)


def blocked(full, desc, tpcs):
    if full in BLOCK:
        return True
    if _PROXY_RE.search(full.split('/')[-1]):
        return True
    text = full + ' ' + (desc or '') + ' ' + ' '.join(tpcs)
    return bool(_BAD_RE.search(text))


# ---------------- 语言 -> 方向 兜底 ----------------
LANG_STACK = {
    'TypeScript': '前端', 'JavaScript': '前端', 'Vue': '前端', 'Svelte': '前端',
    'CSS': '前端', 'HTML': '前端', 'SCSS': '前端',
    'Python': '后端 / 服务端', 'Go': '后端 / 服务端', 'Java': '后端 / 服务端',
    'PHP': '后端 / 服务端', 'Ruby': '后端 / 服务端', 'C#': '后端 / 服务端',
    'Kotlin': '后端 / 服务端', 'Scala': '后端 / 服务端', 'Elixir': '后端 / 服务端',
    'Rust': '系统 / 底层', 'C': '系统 / 底层', 'C++': '系统 / 底层',
    'Zig': '系统 / 底层', 'Assembly': '系统 / 底层', 'Lua': '系统 / 底层',
    'Swift': '移动端', 'Dart': '移动端', 'Objective-C': '移动端',
    'Shell': '开发工具', 'Dockerfile': 'DevOps / 云原生', 'HCL': 'DevOps / 云原生',
    'Jupyter Notebook': '数据 / 分析', 'Markdown': '学习资源',
    'TeX': '学习资源', 'Vim Script': '开发工具', 'Nix': 'DevOps / 云原生',
    'Solidity': '区块链 / Web3', 'GLSL': '音视频 / 图形', 'HLSL': '音视频 / 图形',
    'PowerShell': '开发工具', 'Batchfile': '开发工具', 'CMake': '开发工具',
}

# 方向优先级：topics 命中数相同的情况下，优先更「具体」的方向
CAT_WEIGHT = {
    'AI / 大模型': 1.35, '安全': 1.2, '区块链 / Web3': 1.15, '游戏': 1.12,
    '系统 / 底层': 1.12, '移动端': 1.08, '数据库 / 存储': 1.05,
    'DevOps / 云原生': 1.03, '开发工具': 1.02, '音视频 / 图形': 1.02,
    '硬件 / 物联网': 1.0, '网络': 1.0, '数据 / 分析': 0.98,
    '自动化 / 效率': 0.96, '前端': 0.95, '后端 / 服务端': 0.94,
    '学习资源': 0.9, '其他': 0.5,
}


def guess_stack(tpcs, lang):
    score = collections.defaultdict(float)
    for t in tpcs:
        c = topics.cat_of(t)
        if c:
            score[c] += CAT_WEIGHT.get(c, 1.0)
    if score:
        best = max(score.items(), key=lambda x: (x[1], x[0]))
        if best[1] >= 1.0:
            return best[0]
    return LANG_STACK.get(lang, '其他')


def auto_tags(tpcs, stack, limit=3):
    out = []
    for t in tpcs:
        cn = topics.cn_of(t)
        if cn and cn not in out and cn != stack:
            out.append(cn)
        if len(out) >= limit:
            break
    return out


# 旧标注里用的方向名 -> 新方向体系（早期人工标注沿用了更细的划分）
LEGACY_STACK = {
    'Vue': '前端', 'React': '前端', '前端其他': '前端', 'Node.js / TS': '前端',
    'Python': '后端 / 服务端', 'Go': '后端 / 服务端', 'Java': '后端 / 服务端',
    'PHP': '后端 / 服务端', 'C / C++': '系统 / 底层', 'Rust': '系统 / 底层',
    '数据可视化': '数据 / 分析',
}


def norm_stack(s):
    return LEGACY_STACK.get(s, s)


# ---------------- 读取快照 ----------------
def load_repos():
    path = os.path.join(HERE, 'repos.jsonl')
    seen = {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except Exception:
                continue
            k = r['f']
            if k in seen:
                # 保留 Star 更多 / 描述更全的一条
                old = seen[k]
                if r.get('s', 0) > old.get('s', 0):
                    seen[k] = r
                continue
            seen[k] = r
    return list(seen.values())


def main():
    repos = load_repos()
    print(f'快照条目: {len(repos)}')

    out = []
    dropped = 0
    for r in repos:
        full = r['f']
        if r.get('a'):
            dropped += 1
            continue
        tpcs = r.get('t') or []
        if blocked(full, r.get('d', ''), tpcs):
            dropped += 1
            continue

        anno = ANNO.get(full)
        if anno:
            stack = norm_stack(anno[0])
            tags = [t for t in anno[1].split('|') if t]
            cn, scene = anno[2], anno[3]
            tip = anno[4] if len(anno) > 4 else ''
            rec = {
                'f': full, 's': r['s'], 'k': r.get('k', 0), 'l': r.get('l', ''),
                't': tpcs[:8], 'c': r.get('c', ''), 'p': r.get('p', ''), 'a': 0,
                'x': 1, 'st': stack, 'tg': tags, 'cn': cn, 'sc': scene,
            }
            if tip:
                rec['tp'] = tip
        else:
            stack = guess_stack(tpcs, r.get('l', ''))
            rec = {
                'f': full, 's': r['s'], 'k': r.get('k', 0), 'l': r.get('l', ''),
                't': tpcs[:8], 'c': r.get('c', ''), 'p': r.get('p', ''), 'a': 0,
                'st': stack, 'tg': auto_tags(tpcs, stack),
            }
            if r.get('d'):
                rec['ed'] = r['d'][:150]
        out.append(rec)

    out.sort(key=lambda x: -x['s'])

    main_list = [x for x in out if x['s'] >= 10000]
    extra_list = [x for x in out if 5000 <= x['s'] < 10000]
    rest = [x for x in out if x['s'] < 5000]

    today = datetime.date.today().isoformat()
    built = datetime.datetime.now().astimezone().isoformat(timespec='seconds')

    meta = {
        'updated': today,
        'built': built,
        'total': len(main_list) + len(extra_list),
        'ge10k': len(main_list),
        'ge5k': len(main_list) + len(extra_list),
        'curated': sum(1 for x in out if x.get('x')),
        'source': 'GitHub Search API',
    }

    def write(path, payload, note):
        body = json.dumps(payload, ensure_ascii=False, separators=(',', ':'))
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(f'/* {note} —— 由 _build/build.py 生成，请勿手改 */\n')
            f.write('window.' + payload['_g'] + ' = ')
            f.write(json.dumps({k: v for k, v in payload.items() if k != '_g'},
                               ensure_ascii=False, separators=(',', ':')))
            f.write(';\n')
        return os.path.getsize(path)

    s1 = write(os.path.join(ASSETS, 'data.js'),
               {'_g': 'GH_DATA', 'meta': meta, 'projects': main_list},
               'GitHub 万星项目数据集（首屏）')
    s2 = write(os.path.join(ASSETS, 'data-extra.js'),
               {'_g': 'GH_DATA_EXTRA', 'meta': meta, 'projects': extra_list},
               'GitHub 五千星以上项目（懒加载）')

    topics.dump_js(os.path.join(ASSETS, 'topics.js'))

    print(f'\n主文件 data.js     : {len(main_list):>6} 条  {s1/1024:8.1f} KB')
    print(f'扩展 data-extra.js : {len(extra_list):>6} 条  {s2/1024:8.1f} KB')
    print(f'合计可搜索         : {len(main_list)+len(extra_list):>6} 条')
    print(f'人工精选           : {meta["curated"]:>6} 条')
    print(f'丢弃（归档/违规）  : {dropped:>6} 条')
    print(f'未使用 5000 以下   : {len(rest):>6} 条')

    st = collections.Counter(x['st'] for x in main_list)
    print('\n万星池方向分布：')
    for k, v in st.most_common():
        print(f'  {k:<16}{v}')

    # 校验：人工标注里有没有落到空处（名字打错）
    names = {x['f'] for x in out}
    miss = [k for k in ANNO if k not in names]
    if miss:
        print(f'\n⚠ 有 {len(miss)} 条人工标注未匹配到仓库（可能改名/未收录）：')
        for m in miss[:15]:
            print('   ', m)


if __name__ == '__main__':
    main()
