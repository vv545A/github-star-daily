/* 数据与逻辑自检（Node 环境，不依赖浏览器） */
const fs = require('fs');
const path = require('path');

function loadData(file, varName) {
  const p = path.join(__dirname, '..', 'assets', file);
  if (!fs.existsSync(p)) return null;
  const src = fs.readFileSync(p, 'utf8');
  const i = src.indexOf('window.' + varName + ' = ');
  if (i === -1) return null;
  let body = src.slice(i + ('window.' + varName + ' = ').length);
  body = body.replace(/;\s*$/, '');
  return JSON.parse(body);
}

const MAIN = loadData('data.js', 'GH_DATA');
const EXTRA = loadData('data-extra.js', 'GH_DATA_EXTRA');
const TOPICS = (function () {
  const src = fs.readFileSync(path.join(__dirname, '..', 'assets', 'topics.js'), 'utf8');
  let body = src.slice(src.indexOf('window.GH_TOPICS = ') + 'window.GH_TOPICS = '.length).replace(/;\s*$/, '');
  return JSON.parse(body);
})();

let fail = 0;
function ok(cond, msg) {
  if (!cond) { console.log('  ✗ ' + msg); fail++; }
}
function section(t) { console.log('\n=== ' + t + ' ==='); }

/* ---------- 等价的纯函数（与 app.js 保持一致） ---------- */
const LANG_CN = { JavaScript: 'JavaScript', TypeScript: 'TypeScript', Python: 'Python', Go: 'Go', Rust: 'Rust', 'C#': 'C#', 'C++': 'C++', C: 'C' };
const SHORT_STACK = {
  'AI / 大模型': 'AI', '前端': '前端', '后端 / 服务端': '后端服务', '开发工具': '开发者工具',
  'DevOps / 云原生': '云原生运维', '数据库 / 存储': '数据库', '数据 / 分析': '数据分析',
  '移动端': '移动端', '安全': '安全', '系统 / 底层': '系统底层', '学习资源': '学习资料',
  '区块链 / Web3': '区块链', '音视频 / 图形': '音视频处理', '游戏': '游戏', '网络': '网络',
  '自动化 / 效率': '效率工具', '硬件 / 物联网': '物联网硬件', '其他': '开源'
};
function monthsSince(ym) {
  const parts = String(ym || '').split('-');
  const y = Number(parts[0]), m = Number(parts[1] || 1);
  if (!y) return 999;
  const now = new Date();
  return (now.getFullYear() - y) * 12 + (now.getMonth() - (m - 1));
}
function autoIntro(p) {
  const short = SHORT_STACK[p.st] || '开源';
  const lang = LANG_CN[p.l] || p.l || '';
  const names = [];
  for (const t of (p.t || [])) {
    const n = TOPICS[t];
    if (!n) continue;
    if (n.includes(short) || short.includes(n)) continue;
    if (lang && n.includes(lang)) continue;
    if (!names.includes(n)) names.push(n);
    if (names.length >= 3) break;
  }
  if (!names.length) {
    for (const raw of (p.t || [])) {
      if (!raw || TOPICS[raw]) continue;
      names.push(raw);
      if (names.length >= 3) break;
    }
  }
  const head = lang ? '这是一个用 ' + lang + ' 写的' : '这是一个';
  let s1;
  if (names.length) s1 = head + short + '项目，主要涉及' + names.join('、') + '。';
  else if (!lang) s1 = '这是 ' + p.f.split('/')[0] + ' 名下的开源项目，作者没有填写简介，可以点开仓库看 README 了解。';
  else s1 = head + short + '项目。';
  const mo = monthsSince(p.c);
  let s2 = '';
  if (mo < 900) {
    const age = mo < 12 ? mo + ' 个月' : Math.floor(mo / 12) + ' 年';
    s2 = '上线 ' + age + '，目前 ' + (p.s >= 10000 ? (p.s / 10000).toFixed(1).replace(/\.0$/, '') + ' 万' : p.s) + ' Star' +
      (mo <= 36 ? '，属于这两年冒出来的新项目。' : '。');
  }
  return s1 + s2;
}

const ALL = [].concat(MAIN.projects, EXTRA ? EXTRA.projects : []);
const MARKS = MAIN.meta;

/* ---------- 数据完整性 ---------- */
section('数据完整性');
console.log('  主文件 ' + MAIN.projects.length + ' 条 | 扩展 ' + (EXTRA ? EXTRA.projects.length : 0) + ' 条 | 合计 ' + ALL.length);
console.log('  快照 ' + MARKS.updated + ' | 万星 ' + MARKS.ge10k + ' | 精选 ' + MARKS.curated);
ok(MAIN.projects.length > 100, '主文件条目应 > 100');
/* CI 护栏：抓取不完整时这里会红，从而阻止覆盖线上数据 */
ok(MAIN.projects.length >= 4500, '万星池应 ≥ 4500 条（当前 ' + MAIN.projects.length + '）');
ok((EXTRA ? EXTRA.projects.length : 0) >= 5000, '扩展池应 ≥ 5000 条（当前 ' + (EXTRA ? EXTRA.projects.length : 0) + '）');
ok(ALL.length >= 10000, '合计可搜索应 ≥ 10000 条（当前 ' + ALL.length + '）');
ok(MARKS.curated >= 300, '人工精选应 ≥ 300 条（当前 ' + MARKS.curated + '）');
ok(MAIN.projects.every(p => p.s >= 10000), '主文件所有项目 Star ≥ 1w');
ok((EXTRA ? EXTRA.projects : []).every(p => p.s >= 5000 && p.s < 10000), '扩展文件均为 5000~9999');
ok(MAIN.projects.every(p => p.f && p.f.includes('/')), '仓库全名格式正确');
ok(MAIN.projects.every(p => p.st && p.st !== ''), '每条都有方向归类');
ok(MAIN.projects.every(p => Array.isArray(p.t)), 'topics 为数组');

const ids = new Set(ALL.map(p => p.f));
ok(ids.size === ALL.length, '没有重复仓库（' + (ALL.length - ids.size) + ' 条重复）');

const VALID = new Set(['AI / 大模型', '前端', '后端 / 服务端', '开发工具', 'DevOps / 云原生',
  '数据库 / 存储', '数据 / 分析', '移动端', '安全', '系统 / 底层', '学习资源',
  '区块链 / Web3', '音视频 / 图形', '游戏', '网络', '自动化 / 效率', '硬件 / 物联网', '其他']);
const badStack = ALL.filter(p => !VALID.has(p.st));
ok(badStack.length === 0, '方向名都在合法集合内（异常 ' + badStack.length + ' 条）');
if (badStack.length) console.log('    ' + badStack.slice(0, 5).map(p => p.f + '=' + p.st).join(', '));

/* ---------- 人工精选质量 ---------- */
section('人工精选中文质量');
const curated = ALL.filter(p => p.x);
console.log('  精选 ' + curated.length + ' 条（其中万星 ' + curated.filter(p => p.s >= 10000).length + '）');
ok(curated.length >= 250, '精选条目应 ≥ 250');
const noCn = curated.filter(p => !p.cn || p.cn.length < 12);
ok(noCn.length === 0, '精选条目都有中文简介');
const noSc = curated.filter(p => !p.sc || p.sc.length < 8);
ok(noSc.length === 0, '精选条目都有适用场景');
const noTg = curated.filter(p => !Array.isArray(p.tg) || !p.tg.length);
ok(noTg.length === 0, '精选条目都有标签');
const lens = curated.map(p => p.cn.length);
const avg = Math.round(lens.reduce((a, b) => a + b, 0) / (lens.length || 1));
console.log('  中文简介平均 ' + avg + ' 字 | 最短 ' + Math.min.apply(null, lens) + ' | 最长 ' + Math.max.apply(null, lens));
ok(avg >= 40, '精选简介平均长度应 ≥ 40 字（当前 ' + avg + '）');
const shortCn = curated.filter(p => p.cn.length < 20);
if (shortCn.length) console.log('    偏短：' + shortCn.slice(0, 5).map(p => p.f).join(', '));
const withTip = curated.filter(p => p.tp);
console.log('  含手写上手提示 ' + withTip.length + ' 条（其余按语言自动生成）');

const autoList = ALL.filter(p => !p.x);
const withEn = autoList.filter(p => p.ed);
console.log('  长尾项目带英文原描述 ' + withEn.length + '/' + autoList.length +
  ' (' + Math.round(withEn.length / Math.max(1, autoList.length) * 100) + '%)');

/* ---------- 自动中文摘要 ---------- */
section('长尾自动摘要');
const autoLens = autoList.slice(0, 400).map(p => autoIntro(p));
const aAvg = Math.round(autoLens.reduce((a, s) => a + s.length, 0) / Math.max(1, autoLens.length));
console.log('  抽 400 条，平均 ' + aAvg + ' 字');
ok(aAvg >= 30, '自动摘要平均应 ≥ 30 字');
const badAuto = autoLens.filter(s => !s.endsWith('。') || s.length < 12);
ok(badAuto.length === 0, '自动摘要格式正常');
console.log('  样例：');
autoLens.slice(0, 3).forEach(s => console.log('    ' + s));
ok(!/undefined|null|NaN/.test(autoLens.join('')), '自动摘要无异常字符');

/* ---------- 每日挑选 ---------- */
section('每日挑选');
function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a = (a + 0x6D2B79F5) >>> 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
function shuffle(arr, rnd) {
  for (let i = arr.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); const t = arr[i]; arr[i] = arr[j]; arr[j] = t; }
  return arr;
}
const CUR8 = ALL.filter(p => p.x && p.s >= 10000).map(p => ({
  id: p.f, s: p.s, st: p.st, c: p.c,
  novel: p.s >= 10000 && monthsSince(p.c) <= 36
}));

function pick(seed, batch) {
  const rnd = mulberry32(((seed + batch * 7919) >>> 0));
  const pool = shuffle(CUR8.slice(), rnd);
  const out = [], cnt = new Map();
  const take = p => {
    if (!p || out.includes(p)) return false;
    if ((cnt.get(p.st) || 0) >= 2) return false;
    cnt.set(p.st, (cnt.get(p.st) || 0) + 1); out.push(p); return true;
  };
  let nv = 0;
  for (const p of pool) { if (nv >= 2) break; if (p.novel && take(p)) nv++; }
  for (const p of pool) { if (out.length >= 10) break; take(p); }
  return out;
}
console.log('  精选万星池 ' + CUR8.length + ' 条');
const b0 = pick(20261031, 0), b1 = pick(20261031, 1), b2 = pick(20261031, 2);
ok(b0.length === 10, '每批 10 个');
ok(new Set(b0.map(p => p.id)).size === 10, '同批不重复');
ok(new Set(b0.map(p => p.st)).size >= 5, '至少覆盖 5 个方向（实际 ' + new Set(b0.map(p => p.st)).size + '）');
ok(b0.filter(p => p.novel).length >= 2, '至少 2 个新锐项目（实际 ' + b0.filter(p => p.novel).length + '）');
ok(JSON.stringify(b0.map(p => p.id)) === JSON.stringify(pick(20261031, 0).map(p => p.id)), '同一天同批次结果稳定');
ok(JSON.stringify(b0.map(p => p.id)) !== JSON.stringify(b1.map(p => p.id)), '换一批结果不同');
ok(JSON.stringify(b1.map(p => p.id)) !== JSON.stringify(b2.map(p => p.id)), '连续换批结果不同');
ok(JSON.stringify(pick(20261031, 0).map(p => p.id)) !== JSON.stringify(pick(20261101, 0).map(p => p.id)), '跨天结果不同');
console.log('  第1批方向：' + b0.map(p => p.st).join(' / '));

const seen = new Set();
for (let i = 0; i < 60; i++) pick(20261031, i).forEach(p => seen.add(p.id));
console.log('  连续 60 批覆盖 ' + seen.size + ' 个不同项目（池 ' + CUR8.length + '）');
ok(seen.size >= 60, '连续换批能带出足够多不同项目');

/* ---------- 搜索 ---------- */
section('搜索（本地库 ' + ALL.length + ' 条）');
function isShortKw(k) { return k.length <= 2 && /^[a-z0-9]+$/.test(k); }
function kwHit(text, k) {
  if (!text) return false;
  if (isShortKw(k)) return new RegExp('(^|[^a-z0-9])' + k + '([^a-z0-9]|$)').test(text);
  return text.indexOf(k) !== -1;
}
function kwPrefix(text, k) {
  if (!text) return false;
  if (isShortKw(k)) return new RegExp('^' + k + '([^a-z0-9]|$)').test(text);
  return text.indexOf(k) === 0;
}
function tNames(p) { return (p.t || []).map(t => TOPICS[t]).filter(Boolean).join(' '); }
function score(p, kws) {
  const name = p.f.split('/')[1].toLowerCase(), owner = p.f.split('/')[0].toLowerCase();
  const tags = (p.tg || []).join(' ').toLowerCase();
  const stack = (p.st || '').toLowerCase(), lang = (p.l || '').toLowerCase();
  const tp = (p.t || []).join(' ').toLowerCase(), tcn = tNames(p).toLowerCase();
  const text = ((p.cn || '') + ' ' + (p.sc || '')).toLowerCase();
  let total = 0;
  for (const k of kws) {
    let s = 0;
    if (name === k) s += 900;
    else if (kwPrefix(name, k)) s += 520;
    else if (kwHit(name, k)) s += 300;
    if (kwHit(owner, k)) s += 200;
    if (kwHit(tags, k)) s += 250;
    if (kwHit(tp, k)) s += 235;
    if (kwHit(tcn, k)) s += 235;
    if (kwHit(stack, k)) s += 150;
    if (kwHit(lang, k)) s += 130;
    if (kwHit(text, k)) s += 70;
    if (s === 0) return 0;
    total += s;
  }
  return total;
}
function search(q) {
  const kws = q.trim().toLowerCase().split(/\s+/).filter(Boolean);
  if (!kws.length) return [];
  const hits = [];
  for (const p of ALL) { const s = score(p, kws); if (s > 0) hits.push({ p, s }); }
  hits.sort((a, b) => b.s - a.s || b.p.s - a.p.s);
  return hits.map(h => h.p);
}
const cases = ['AI Agent', 'MCP', '本地大模型', '微调', 'RAG', '爬虫', 'rust', 'go',
  '截图', '同步', '自托管', '终端', '翻译', '向量', '播放器', '密码', '监控', '表格',
  'OCR', '语音', '自动化', 'zzzz不存在'];
for (const q of cases) {
  const r = search(q);
  console.log('  ' + q.padEnd(12) + ' → ' + String(r.length).padStart(4) + ' 条   ' +
    r.slice(0, 3).map(p => p.f.split('/')[1]).join(', '));
}
ok(search('MCP').length > 0, 'MCP 有结果');
ok(search('zzzz不存在').length === 0, '乱码无结果');
ok(search('爬虫').length > 0, '中文用途可搜');
ok(search('微调').length > 0, '中文术语可搜');

const multi = search('rust 终端');
console.log('  多词 rust 终端 → ' + multi.length + ' 条');
ok(multi.length > 0, '多关键词可用');

const t0 = Date.now();
for (let i = 0; i < 20; i++) search('rust 终端');
const cost = Date.now() - t0;
console.log('  20 次搜索耗时 ' + cost + 'ms（每次约 ' + Math.round(cost / 20) + 'ms）');

/* ---------- 新锐池 ---------- */
section('新锐创新池');
const NOVEL = ALL.filter(p => p.s >= 10000 && monthsSince(p.c) <= 36);
console.log('  新锐项目 ' + NOVEL.length + ' 个');
ok(NOVEL.length >= 30, '新锐项目应 ≥ 30');
const byStack = {};
NOVEL.forEach(p => { byStack[p.st] = (byStack[p.st] || 0) + 1; });
console.log('  ' + Object.entries(byStack).sort((a, b) => b[1] - a[1]).map(e => e[0] + ':' + e[1]).join('  '));

/* ---------- 方向分布 ---------- */
section('方向分布（万星池）');
const dist = {};
ALL.filter(p => p.s >= 10000).forEach(p => { dist[p.st] = (dist[p.st] || 0) + 1; });
console.log('  ' + Object.entries(dist).sort((a, b) => b[1] - a[1]).map(e => e[0] + ':' + e[1]).join('  '));

/* ---------- 体积 ---------- */
section('体积');
['data.js', 'data-extra.js', 'topics.js', 'app.js', 'style.css'].forEach(f => {
  const p = path.join(__dirname, '..', 'assets', f);
  if (fs.existsSync(p)) console.log('  ' + f.padEnd(16) + (fs.statSync(p).size / 1024).toFixed(1) + ' KB');
});

console.log('\n' + (fail === 0 ? '✅ 全部通过' : '❌ ' + fail + ' 项失败'));
process.exitCode = fail === 0 ? 0 : 1;
