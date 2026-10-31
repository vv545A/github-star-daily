# -*- coding: utf-8 -*-
"""
分层抓取 GitHub 万星/千星项目快照（断点续传、令牌桶限速）

用法:
    python fetch_all.py            # 按优先级抓取
    python fetch_all.py --tier 1   # 只抓 >=10000
"""
import json, os, sys, time, urllib.request, urllib.error, urllib.parse

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'raw')
STATE = os.path.join(HERE, 'fetch_state.json')
OUT = os.path.join(HERE, 'repos.jsonl')
os.makedirs(RAW, exist_ok=True)

API = 'https://api.github.com/search/repositories'
UA = 'Mozilla/5.0 (compatible; gh-star-index-builder/1.0)'
# 未登录搜索接口限 10 次/分钟，认证后 30 次/分钟。
# 有令牌时用 GH_SLEEP 调快（默认 2.5s ≈ 24 次/分钟）
TOKEN = os.environ.get('GITHUB_TOKEN', '').strip()
SLEEP = float(os.environ.get('GH_SLEEP') or (2.5 if TOKEN else 6.6))


def _budget_per_min():
    return 26 if TOKEN else 9


PER_PAGE = 100

# 优先级从高到低：先保证 >=10000 完整，再往下补
TIERS = [
    (10000, None),      # 5705 个
    (5000, 9999),       # 7149 个
    (2000, 4999),       # 21080 个
    (1000, 1999),       # 32168 个（可选，量最大）
]


def load_state():
    if os.path.exists(STATE):
        return json.load(open(STATE, encoding='utf-8'))
    return {'done': [], 'seen': 0}


def save_state(st):
    json.dump(st, open(STATE, 'w', encoding='utf-8'))


def req(url, tries=6):
    for t in range(tries):
        try:
            headers = {
                'User-Agent': UA,
                'Accept': 'application/vnd.github+json',
                'X-GitHub-Api-Version': '2022-11-28',
            }
            if TOKEN:
                headers['Authorization'] = 'Bearer ' + TOKEN
            r = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(r, timeout=45) as resp:
                return json.loads(resp.read().decode('utf-8')), resp.headers
        except urllib.error.HTTPError as e:
            body = ''
            try:
                body = e.read().decode('utf-8', 'replace')[:300]
            except Exception:
                pass
            if e.code in (403, 429):
                reset = e.headers.get('X-RateLimit-Reset')
                wait = 62
                if reset:
                    try:
                        wait = max(10, int(reset) - int(time.time()) + 6)
                    except Exception:
                        pass
                wait = min(wait, 130)
                print(f'    [限流 {e.code}] 等待 {wait}s …', flush=True)
                time.sleep(wait)
                continue
            if e.code == 422:
                return {'__split__': True}, None
            print(f'    [HTTP {e.code}] {body}', flush=True)
            time.sleep(8)
        except Exception as ex:
            print(f'    [错误] {type(ex).__name__}: {ex}', flush=True)
            time.sleep(8)
    return None, None


def star_q(lo, hi):
    if hi is None:
        return f'stars:>={lo} archived:false'
    return f'stars:{lo}..{hi} archived:false'


def fetch_range(lo, hi, st, out, budget):
    """抓一个星区间。第 1 页同时拿到 total_count，省掉一次探测请求"""
    q = star_q(lo, hi)
    key = f'{lo}-{hi if hi else "inf"}'
    if key in st['done']:
        print(f'  [跳过] {key}', flush=True)
        return 0

    fp1 = os.path.join(RAW, f'{key}_p1.json')
    first = None
    total = None

    if os.path.exists(fp1):
        first = json.load(open(fp1, encoding='utf-8'))
        total = len(first)  # 已抓过，按已知页数继续
    else:
        if budget[0] <= 0:
            return 0
        url = f'{API}?q={urllib.parse.quote(q)}&sort=stars&order=desc&per_page={PER_PAGE}&page=1'
        d, _ = req(url)
        budget[0] -= 1
        time.sleep(SLEEP)
        if d is None:
            return 0
        if d.get('__split__'):
            return split(lo, hi, st, out, budget)
        total = d.get('total_count', 0)
        items = d.get('items', [])
        print(f'  {key}: 共 {total} 个', flush=True)
        if total > 1000:
            return split(lo, hi, st, out, budget)
        if total == 0:
            st['done'].append(key)
            save_state(st)
            return 0
        json.dump(items, open(fp1, 'w', encoding='utf-8'), ensure_ascii=False)
        for it in items:
            out.write(json.dumps(trim(it), ensure_ascii=False) + '\n')
        out.flush()
        first = items

    # 已知总量从这里推：用第 1 页条目数是否满 100 判断还有后续
    pages = 10 if len(first) >= PER_PAGE else 1
    # 更准确的页数：重新用 total 判断（total 未知时按满页递推）
    got = len(first)
    p = 2
    while p <= 10:
        fp = os.path.join(RAW, f'{key}_p{p}.json')
        if os.path.exists(fp):
            got += len(json.load(open(fp, encoding='utf-8')))
            p += 1
            continue
        if len(first) < PER_PAGE:
            break
        if budget[0] <= 0:
            print(f'    [预算用尽] 停在 {key} 第 {p} 页', flush=True)
            return got
        u = f'{API}?q={urllib.parse.quote(q)}&sort=stars&order=desc&per_page={PER_PAGE}&page={p}'
        d2, _ = req(u)
        budget[0] -= 1
        time.sleep(SLEEP)
        if d2 is None or d2.get('__split__'):
            break
        items = d2.get('items', [])
        if not items:
            break
        json.dump(items, open(fp, 'w', encoding='utf-8'), ensure_ascii=False)
        for it in items:
            out.write(json.dumps(trim(it), ensure_ascii=False) + '\n')
        got += len(items)
        out.flush()
        print(f'    {key} 第{p}页 +{len(items)} (累计 {got})', flush=True)
        if len(items) < PER_PAGE:
            break
        p += 1

    st['done'].append(key)
    save_state(st)
    return got


def split(lo, hi, st, out, budget):
    if hi is None:
        hi = 1000000       # 上限要足够大，否则会漏掉 freeCodeCamp 这类 40 万星的项目
    if hi - lo <= 40:
        # 无法再分，直接取前 1000
        return fetch_pages_capped(lo, hi, st, out, budget)
    mid = (lo + hi) // 2
    a = fetch_range(lo, mid, st, out, budget)
    b = fetch_range(mid + 1, hi, st, out, budget)
    return a + b


def fetch_pages_capped(lo, hi, st, out, budget):
    key = f'{lo}-{hi}c'
    if key in st['done']:
        return 0
    q = star_q(lo, hi)
    got = 0
    for p in range(1, 11):
        fp = os.path.join(RAW, f'{key}_p{p}.json')
        if os.path.exists(fp):
            continue
        if budget[0] <= 0:
            return got
        u = f'{API}?q={urllib.parse.quote(q)}&sort=stars&order=desc&per_page={PER_PAGE}&page={p}'
        d2, _ = req(u)
        budget[0] -= 1
        time.sleep(SLEEP)
        if not d2 or d2.get('__split__'):
            continue
        items = d2.get('items', [])
        if not items:
            break
        json.dump(items, open(fp, 'w', encoding='utf-8'), ensure_ascii=False)
        for it in items:
            out.write(json.dumps(trim(it), ensure_ascii=False) + '\n')
        got += len(items)
        out.flush()
    st['done'].append(key)
    save_state(st)
    return got


def trim(it):
    return {
        'f': it['full_name'],
        's': it['stargazers_count'],
        'k': it['forks_count'],
        'l': it.get('language') or '',
        't': (it.get('topics') or [])[:10],
        'd': (it.get('description') or '').replace('\n', ' ').strip()[:180],
        'c': (it.get('created_at') or '')[:7],
        'p': (it.get('pushed_at') or '')[:10],
        'a': 1 if it.get('archived') else 0,
        'h': (it.get('homepage') or '')[:80],
    }


def main():
    tier = None
    if '--tier' in sys.argv:
        tier = int(sys.argv[sys.argv.index('--tier') + 1])
    budget = [10 ** 9]
    if '--budget' in sys.argv:
        budget[0] = int(sys.argv[sys.argv.index('--budget') + 1])

    print(f'模式: {"认证（30 次/分钟）" if TOKEN else "未认证（10 次/分钟）"} | 间隔 {SLEEP}s', flush=True)

    st = load_state()
    with open(OUT, 'a', encoding='utf-8') as out:
        for i, (lo, hi) in enumerate(TIERS, 1):
            if tier and i != tier:
                continue
            print(f'=== 第 {i} 层: {star_q(lo, hi)} ===', flush=True)
            fetch_range(lo, hi, st, out, budget)
            if budget[0] <= 0:
                print('预算用尽，退出', flush=True)
                break

    n = sum(1 for _ in open(OUT, encoding='utf-8')) if os.path.exists(OUT) else 0
    print(f'完成，repos.jsonl 共 {n} 行', flush=True)


if __name__ == '__main__':
    main()
