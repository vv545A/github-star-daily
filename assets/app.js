/* ==========================================================================
   万星日推 · 应用逻辑（原生 JS，零依赖）
   --------------------------------------------------------------------------
   数据分两层：
     · 本地快照（data.js / data-extra.js）—— 保证秒开、离线可用、可全文模糊搜
     · GitHub 实时接口 —— 按需同步 Star、兜底搜索本地未收录的千星项目
   ========================================================================== */
(function () {
  'use strict';

  /* ---------------- 常量 ---------------- */
  const DAILY_SIZE = 10;
  const MAX_PER_STACK = 2;
  const NOVEL_SLOTS = 2;          /* 日推里至少几个「新锐创新」项目 */
  const NOVEL_MONTHS = 36;        /* 创建 3 年内算新锐 */
  const NOVEL_MIN_STARS = 10000;
  const PAGE_SIZE = 60;           /* 搜索结果每屏条数 */

  const FAV_KEY = 'ghstar_favorites_v1';
  const TOKEN_KEY = 'ghstar_token_v1';
  const LIVE_KEY = 'ghstar_live_v1';

  const TOPIC_CN = window.GH_TOPICS || {};

  const LANG_CN = {
    JavaScript: 'JavaScript', TypeScript: 'TypeScript', Python: 'Python', Go: 'Go',
    Rust: 'Rust', Java: 'Java', C: 'C', 'C++': 'C++', 'C#': 'C#', PHP: 'PHP',
    Ruby: 'Ruby', Swift: 'Swift', Kotlin: 'Kotlin', Dart: 'Dart', Shell: 'Shell',
    HTML: 'HTML', CSS: 'CSS', Vue: 'Vue', Svelte: 'Svelte', 'Jupyter Notebook': 'Jupyter',
    Markdown: '文档类', Zig: 'Zig', Lua: 'Lua', Scala: 'Scala', Elixir: 'Elixir',
    Haskell: 'Haskell', 'Objective-C': 'Objective-C', Assembly: '汇编'
  };

  const LANG_COLOR = {
    JavaScript: '#f1e05a', TypeScript: '#3178c6', Python: '#3572A5', Go: '#00ADD8',
    Rust: '#dea584', Java: '#b07219', C: '#555555', 'C++': '#f34b7d', 'C#': '#178600',
    PHP: '#4F5D95', Ruby: '#701516', Swift: '#F05138', Kotlin: '#A97BFF',
    Dart: '#00B4AB', Shell: '#89e051', HTML: '#e34c26', CSS: '#563d7c',
    Vue: '#41b883', Svelte: '#ff3e00', Markdown: '#083fa1',
    'Jupyter Notebook': '#DA5B0B', MDX: '#fcb32c', Zig: '#ec915c',
    Lua: '#000080', Scala: '#c22d40', Elixir: '#6e4a7e', Haskell: '#5e5086',
    'Objective-C': '#438eff', Assembly: '#6E4C13', Batchfile: '#C1F12E',
    'Vim Script': '#199f4b', Dockerfile: '#384d54', Nix: '#7e7eff'
  };

  /* 方向名的「口语化」写法 —— 用在自动生成的中文句子里，避免「硬件 / 物联网方向」这种读着别扭的表达 */
  const SHORT_STACK = {
    'AI / 大模型': 'AI', '前端': '前端', '后端 / 服务端': '后端服务',
    '开发工具': '开发者工具', 'DevOps / 云原生': '云原生运维',
    '数据库 / 存储': '数据库', '数据 / 分析': '数据分析',
    '移动端': '移动端', '安全': '安全', '系统 / 底层': '系统底层',
    '学习资源': '学习资料', '区块链 / Web3': '区块链', '音视频 / 图形': '音视频处理',
    '游戏': '游戏', '网络': '网络', '自动化 / 效率': '效率工具',
    '硬件 / 物联网': '物联网硬件', '其他': '开源'
  };

  /* 各方向的「什么时候用」—— 给长尾项目自动生成中文时的兜底 */
  const STACK_SCENE = {
    'AI / 大模型': '想在项目里接入 AI 能力，或想在自己电脑上跑模型时。',
    '前端': '做界面、做官网、做后台面板时，可以直接拿来当基础。',
    '后端 / 服务端': '写接口、搭服务、做业务系统时，可作为现成的骨架。',
    '开发工具': '写代码、调试、提效的日常环节里，装上就能用。',
    'DevOps / 云原生': '做部署、监控、自动化流水线时用得上。',
    '数据库 / 存储': '需要存数据、查数据、扛并发读写时。',
    '数据 / 分析': '要做报表、跑数据分析、做可视化时。',
    '移动端': '做手机 App 或跨端应用时。',
    '安全': '做安全自查、渗透测试、隐私保护时。',
    '系统 / 底层': '想深入理解计算机原理，或写高性能底层程序时。',
    '学习资源': '想系统入门某个方向时，从这里挑一份跟着练。',
    '区块链 / Web3': '做链上应用、合约或钱包相关开发时。',
    '音视频 / 图形': '处理图片、音视频、3D 或渲染时。',
    '游戏': '做游戏、做模拟器或研究引擎实现时。',
    '网络': '做网络编程、爬虫、代理或协议分析时。',
    '自动化 / 效率': '想把重复的活交给程序自动跑时。',
    '硬件 / 物联网': '玩开发板、单片机或做物联网设备时。',
    '其他': '具体用途看下方仓库说明。'
  };

  /* 各语言的上手提示 —— 新手最需要的一句 */
  const LANG_TIP = {
    TypeScript: '先装 Node.js 18+，然后 npm install && npm run dev。',
    JavaScript: '先装 Node.js 18+，按 README 执行 npm install 即可。',
    Python: '装好 Python 3.10+，多数情况 pip install -r requirements.txt 就能跑。',
    Go: '装 Go 1.21+，或直接下载 Releases 里编译好的可执行文件（最省事）。',
    Rust: '装 Rust 工具链后 cargo build；不想编译就直接下 Releases 的二进制。',
    Java: '需要 JDK 17+，多数项目提供打包好的 jar，java -jar 直接运行。',
    Kotlin: '装 JDK 17+ 后用 Gradle 构建，Android 项目用 Android Studio 打开。',
    C: '需要自己编译，按 README 装依赖后 make 构建。',
    'C++': '需要自己编译，按 README 装依赖后 cmake 构建。',
    'C#': '装 .NET SDK 后 dotnet run，Windows 项目用 Visual Studio 打开。',
    PHP: '装 PHP 8+ 和 Composer，composer install 后即可启动。',
    Ruby: '装 Ruby 3+，bundle install 后启动。',
    Swift: 'macOS 上用 Xcode 打开工程直接运行。',
    Dart: '装 Flutter SDK，flutter run 即可。',
    Shell: '照着 README 里的命令逐条执行，建议先看脚本内容再运行。',
    HTML: '纯前端项目，直接双击 index.html 或起个静态服务器就能看。',
    Vue: '装 Node.js 18+，npm install 后 npm run dev。',
    'Jupyter Notebook': '装 Python 与 Jupyter，用浏览器打开 .ipynb 逐格运行。'
  };

  const STACK_TONE = {
    'AI / 大模型': 't2', '前端': 't0', '后端 / 服务端': 't1', '开发工具': 't7',
    'DevOps / 云原生': 't5', '数据库 / 存储': 't4', '数据 / 分析': 't6',
    '移动端': 't1', '安全': 't4', '系统 / 底层': 't3', '学习资源': 't6',
    '区块链 / Web3': 't3', '音视频 / 图形': 't2', '游戏': 't5',
    '网络': 't5', '自动化 / 效率': 't6', '硬件 / 物联网': 't7', '其他': 't7'
  };

  const TONE_DOT = {
    t0: '#0550ae', t1: '#116329', t2: '#8250df', t3: '#953800',
    t4: '#a3216b', t5: '#0f6f76', t6: '#7d4e00', t7: '#4a545e'
  };

  const ICONS = {
    star: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z"/></svg>',
    starOutline: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"/></svg>',
    fork: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"/></svg>',
    copy: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"/><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"/></svg>',
    download: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"/><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"/></svg>',
    zip: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.75 0h8.5C13.216 0 14 .784 14 1.75v12.5A1.75 1.75 0 0 1 12.25 16h-8.5A1.75 1.75 0 0 1 2 14.25V1.75C2 .784 2.784 0 3.75 0Zm0 1.5a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Z"/><path d="M8.5 2.25v1.5h-2v-1.5Zm0 2.75v1.5h-2V5Zm0 2.75v1.5h-2v-1.5Zm-1 2.75h1v1.5h-1Z"/></svg>',
    github: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"/></svg>',
    check: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"/></svg>',
    arrow: '<svg class="arrow" viewBox="0 0 16 16" aria-hidden="true"><path d="M8.22 2.97a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l2.97-2.97H3.75a.75.75 0 0 1 0-1.5h7.44L8.22 4.03a.75.75 0 0 1 0-1.06Z"/></svg>'
  };

  /* ---------------- 工具 ---------------- */
  const $ = function (s) { return document.querySelector(s); };
  const $$ = function (s) { return Array.prototype.slice.call(document.querySelectorAll(s)); };
  const fmtNum = function (n) { return Number(n || 0).toLocaleString('en-US'); };

  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  function fmtK(n) {
    if (n >= 1000) {
      const k = n / 1000;
      return (k >= 100 ? Math.round(k) : k.toFixed(1).replace(/\.0$/, '')) + 'k';
    }
    return String(n || 0);
  }

  function langColor(l) { return LANG_COLOR[l] || '#8b949e'; }

  function relDate(iso) {
    if (!iso) return '';
    const d = new Date(iso + 'T00:00:00');
    if (isNaN(d.getTime())) return '';
    const days = Math.floor((Date.now() - d.getTime()) / 86400000);
    if (days <= 0) return '今天有更新';
    if (days === 1) return '昨天更新';
    if (days < 30) return days + ' 天前更新';
    if (days < 365) return Math.floor(days / 30) + ' 个月前更新';
    return Math.floor(days / 365) + ' 年前更新';
  }

  function monthsSince(ym) {
    if (!ym) return 999;
    const parts = String(ym).split('-');
    const y = parseInt(parts[0], 10), m = parseInt(parts[1] || '1', 10) - 1;
    if (isNaN(y)) return 999;
    const now = new Date();
    return (now.getFullYear() - y) * 12 + (now.getMonth() - m);
  }

  function ageLabel(ym) {
    const mo = monthsSince(ym);
    if (mo < 1) return '刚发布';
    if (mo < 12) return mo + ' 个月前创建';
    const y = Math.floor(mo / 12);
    return y + ' 年前创建';
  }

  function todayLabel() {
    const d = new Date();
    const week = ['周日', '周一', '周二', '周三', '周四', '周五', '周六'];
    return d.getFullYear() + ' 年 ' + (d.getMonth() + 1) + ' 月 ' + d.getDate() + ' 日 · ' + week[d.getDay()];
  }

  function daySeed() {
    const d = new Date();
    return d.getFullYear() * 10000 + (d.getMonth() + 1) * 100 + d.getDate();
  }

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
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(rnd() * (i + 1));
      const t = arr[i]; arr[i] = arr[j]; arr[j] = t;
    }
    return arr;
  }

  /* ---------------- 数据装载 ---------------- */
  const projects = [];          /* 全部项目（本地快照，按需追加） */
  const byId = new Map();
  let META = {};
  let CURATED = [];             /* 人工精选（有手写中文简介） */
  let TENK = [];                /* Star ≥ 1w */
  let NOVEL = [];               /* 新锐创新 */
  let extraLoaded = false;

  function normalize(r) {
    const i = r.f.indexOf('/');
    return {
      id: r.f,
      owner: r.f.slice(0, i),
      name: r.f.slice(i + 1),
      full: r.f,
      stars: r.s,
      forks: r.k,
      lang: r.l || '',
      topics: r.t || [],
      created: r.c || '',
      pushed: r.p || '',
      archived: r.a === 1,
      stack: r.st || '其他',
      tags: r.tg || null,
      cn: r.cn || '',
      scene: r.sc || '',
      tip: r.tp || '',
      curated: !!r.x,
      enDesc: r.ed || '',
      url: 'https://github.com/' + r.f,
      clone: 'git clone https://github.com/' + r.f + '.git',
      release: 'https://github.com/' + r.f + '/releases'
    };
  }

  function isNovel(p) {
    return p.stars >= NOVEL_MIN_STARS && monthsSince(p.created) <= NOVEL_MONTHS;
  }

  function wan(n) {
    if (n >= 10000) return (n / 10000).toFixed(1).replace(/\.0$/, '') + ' 万';
    return Number(n || 0).toLocaleString('en-US');
  }

  /* 长尾项目：用 topic 词典拼一段中文说明 */
  function autoIntro(p) {
    const short = SHORT_STACK[p.stack] || '开源';
    const lang = LANG_CN[p.lang] || p.lang || '';
    const names = [];
    for (let i = 0; i < p.topics.length && names.length < 3; i++) {
      const n = TOPIC_CN[p.topics[i]];
      if (!n) continue;
      /* 和方向名重复（如「物联网」vs「物联网硬件」）就别再列一遍 */
      if (n.indexOf(short) !== -1 || short.indexOf(n) !== -1) continue;
      /* 和语言名重复（如「用 Rust 写的…Rust 语言生态」）也别列 */
      if (lang && n.indexOf(lang) !== -1) continue;
      if (names.indexOf(n) === -1) names.push(n);
    }
    /* 词典里没有的 topic，保留原文也比空着强（开发者看得懂英文标签） */
    if (!names.length) {
      for (let i = 0; i < p.topics.length && names.length < 3; i++) {
        const raw = p.topics[i];
        if (!raw || TOPIC_CN[raw]) continue;
        names.push(raw);
      }
    }
    const head = lang ? ('这是一个用 ' + lang + ' 写的') : '这是一个';
    let s1;
    if (names.length) {
      s1 = head + short + '项目，主要涉及' + names.join('、') + '。';
    } else if (!lang) {
      /* 作者没填语言也没打标签，别硬凑，直接告诉人去看 README */
      s1 = '这是 ' + p.owner + ' 名下的开源项目，作者没有填写简介，可以点开仓库看 README 了解。';
    } else {
      s1 = head + short + '项目。';
    }

    /* 再补一句客观信息，让新手对「多成熟」有概念 */
    let s2 = '';
    const mo = monthsSince(p.created);
    if (mo < 900) {
      const age = mo < 12 ? mo + ' 个月' : Math.floor(mo / 12) + ' 年';
      s2 = '上线 ' + age + '，目前 ' + wan(p.stars) + ' Star' +
        (mo <= NOVEL_MONTHS ? '，属于这两年冒出来的新项目。' : '。');
    }
    return s1 + s2;
  }

  /* 逐字段补齐：精选项目可能只写了简介，没写场景/上手提示，这里按语言与方向兜底 */
  function ensureText(p) {
    if (!p.cn) {
      p.auto = true;
      p.cn = autoIntro(p);
    }
    if (!p.scene) p.scene = STACK_SCENE[p.stack] || STACK_SCENE['其他'];
    if (!p.tip) {
      p.tip = LANG_TIP[p.lang] || '看 README 的 Quick Start，多数项目也提供 Docker 一键启动。';
      p.tipAuto = true;
    }
    return p;
  }

  function addAll(arr) {
    for (let i = 0; i < arr.length; i++) {
      const r = arr[i];
      if (byId.has(r.f)) continue;
      const p = normalize(r);
      p.novel = isNovel(p);
      ensureText(p);          /* 长尾项目在这里补齐中文说明与上手提示 */
      projects.push(p);
      byId.set(p.id, p);
    }
  }

  function rebuildDerived() {
    CURATED = projects.filter(function (p) { return p.curated; });
    TENK = projects.filter(function (p) { return p.stars >= 10000; });
    NOVEL = TENK.filter(function (p) { return p.novel; });
    /* 用最新 Star 快照覆盖 */
    applyLiveCache();
  }

  /* ---------------- 收藏 ---------------- */
  const state = {
    view: 'home',
    query: '',
    favs: [],
    batch: 0,
    results: [],
    shown: PAGE_SIZE,
    liveResults: [],
    liveLoading: false,
    novelStack: ''
  };

  function loadFavs() {
    try {
      const arr = JSON.parse(localStorage.getItem(FAV_KEY) || '[]');
      return Array.isArray(arr) ? arr : [];
    } catch (e) { return []; }
  }
  function saveFavs() {
    try { localStorage.setItem(FAV_KEY, JSON.stringify(state.favs)); } catch (e) { /* 忽略 */ }
  }
  function isFav(id) { return state.favs.indexOf(id) !== -1; }

  /* ---------------- 实时 Star 缓存 ---------------- */
  let liveCache = {};

  function loadLiveCache() {
    try { liveCache = JSON.parse(localStorage.getItem(LIVE_KEY) || '{}') || {}; } catch (e) { liveCache = {}; }
  }
  function saveLiveCache() {
    try { localStorage.setItem(LIVE_KEY, JSON.stringify(liveCache)); } catch (e) { /* 忽略 */ }
  }
  function applyLiveCache() {
    const now = Date.now();
    Object.keys(liveCache).forEach(function (id) {
      const rec = liveCache[id];
      const p = byId.get(id);
      if (!p || !rec) return;
      if (now - rec.t > 7 * 86400000) return;      /* 超过 7 天不用了 */
      if (rec.s > p.stars) p.stars = rec.s;         /* 只涨不跌，避免数据回退 */
      p.liveStars = rec.s;
      p.liveAt = rec.t;
    });
  }

  /* ---------------- 每日挑选 ---------------- */
  function pickDaily() {
    const seed = (daySeed() + state.batch * 7919) >>> 0;
    const rnd = mulberry32(seed);
    /* 日推只用「人工精选 + Star 过万」的项目，保证每张卡片的中文都是人写的 */
    const pool = shuffle(CURATED.filter(function (p) { return p.stars >= 10000; }), rnd);

    const out = [];
    const cnt = new Map();
    function take(p) {
      if (!p || out.indexOf(p) !== -1) return false;
      const c = cnt.get(p.stack) || 0;
      if (c >= MAX_PER_STACK) return false;
      cnt.set(p.stack, c + 1);
      out.push(p);
      return true;
    }

    /* 先塞够「新锐创新」名额 */
    let novelN = 0;
    for (let i = 0; i < pool.length && novelN < NOVEL_SLOTS; i++) {
      if (pool[i].novel && take(pool[i])) novelN++;
    }
    /* 再按顺序补齐，保证方向分散 */
    for (let i = 0; i < pool.length && out.length < DAILY_SIZE; i++) take(pool[i]);

    /* 兜底：精选池太小时允许突破方向上限 */
    if (out.length < DAILY_SIZE) {
      for (let i = 0; i < TENK.length && out.length < DAILY_SIZE; i++) {
        const p = TENK[i];
        if (out.indexOf(p) === -1) out.push(p);
      }
    }
    return out;
  }

  /* ---------------- 搜索 ---------------- */
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

  function topicNames(p) {
    if (p._tn !== undefined) return p._tn;
    const out = [];
    for (let i = 0; i < p.topics.length; i++) {
      const n = TOPIC_CN[p.topics[i]];
      if (n) out.push(n);
    }
    p._tn = out.join(' ');
    return p._tn;
  }

  function searchBlob(p) {
    if (p._b) return p._b;
    const tags = p.tags ? p.tags.join(' ') : '';
    p._b = (p.name + ' ' + p.owner + ' ' + p.lang + ' ' + p.stack + ' ' +
            p.topics.join(' ') + ' ' + topicNames(p) + ' ' + tags + ' ' +
            p.cn + ' ' + p.scene).toLowerCase();
    return p._b;
  }

  /* 中文近义词扩展：搜「播放器」也要能命中「音乐播放」这类标签 */
  const SYN = {
    '播放器': ['播放', '音乐', '视频', 'player'],
    '截图': ['截屏', '录屏', 'screenshot'],
    '同步': ['备份', 'sync', 'backup'],
    '下载': ['downloader', '下载器', 'torrent'],
    '剪辑': ['视频编辑', '视频处理'],
    '笔记': ['note', '记事'],
    '待办': ['任务管理', 'todo', 'task'],
    '记账': ['预算', '财务', 'budget'],
    '网盘': ['云存储', '文件同步', 'storage'],
    '壁纸': ['主题', 'wallpaper'],
    '输入法': ['输入', 'ime'],
    '键盘': ['keyboard', '快捷键'],
    '浏览器': ['browser', 'webkit'],
    '文档': ['文档站', 'docs', 'documentation'],
    '电子书': ['阅读', 'ebook', 'book'],
    '游戏': ['game', 'gamedev', '引擎'],
    '机器人': ['bot', '自动化'],
    '代理': ['proxy', '反向代理'],
    '数据库': ['database', 'sql', '存储'],
    '监控': ['monitoring', '告警', 'observability'],
    '可视化': ['图表', 'chart', 'dashboard'],
    '语音': ['tts', '语音合成', '语音识别', 'speech'],
    '翻译': ['translate', '多语言'],
    '压缩': ['压缩包', 'zip', '解压'],
    '清理': ['cleaner', '清理工具'],
    '密码': ['password', '密码管理', '密钥'],
    '同步盘': ['网盘', '云存储']
  };

  function kwVariants(k) {
    const s = SYN[k];
    return s ? [k].concat(s) : [k];
  }

  function hitAny(text, vs) {
    for (let i = 0; i < vs.length; i++) {
      if (kwHit(text, vs[i])) return true;
    }
    return false;
  }

  function scoreOf(p, kws) {
    const name = p.name.toLowerCase();
    const owner = p.owner.toLowerCase();
    const tags = p.tags ? p.tags.join(' ').toLowerCase() : '';
    const stack = p.stack.toLowerCase();
    const lang = p.lang.toLowerCase();
    const topics = p.topics.join(' ').toLowerCase();
    const tcn = topicNames(p).toLowerCase();
    const text = (p.cn + ' ' + p.scene).toLowerCase();

    let total = 0;
    for (let i = 0; i < kws.length; i++) {
      const k = kws[i];
      const vs = kwVariants(k);
      let s = 0;
      if (name === k) s += 900;
      else if (kwPrefix(name, k)) s += 520;
      else if (kwHit(name, k)) s += 300;

      if (hitAny(owner, vs)) s += 200;
      if (hitAny(tags, vs)) s += 250;
      if (hitAny(topics, vs)) s += 235;
      if (hitAny(tcn, vs)) s += 235;
      if (hitAny(stack, vs)) s += 150;
      if (hitAny(lang, vs)) s += 130;
      if (hitAny(text, vs)) s += 70;

      if (s === 0) return 0;
      total += s;
    }
    return total;
  }

  function runSearch(q) {
    const kws = q.trim().toLowerCase().split(/\s+/).filter(Boolean);
    if (!kws.length) return [];
    /* 有近义词或短词时不能走整串快筛，必须逐字段算分 */
    const needFull = kws.some(function (k) { return SYN[k] || isShortKw(k); });
    const hits = [];
    for (let i = 0; i < projects.length; i++) {
      const p = projects[i];
      if (!needFull) {
        const b = searchBlob(p);
        let allIn = true;
        for (let j = 0; j < kws.length; j++) {
          if (b.indexOf(kws[j]) === -1) { allIn = false; break; }
        }
        if (!allIn) continue;
      }
      const s = scoreOf(p, kws);
      if (s > 0) hits.push({ p: p, s: s });
    }
    hits.sort(function (a, b) { return b.s - a.s || b.p.stars - a.p.stars; });
    return hits.map(function (h) { return h.p; });
  }

  /* ---------------- 卡片渲染 ---------------- */
  function tagsHTML(p) {
    const tone = STACK_TONE[p.stack] || 't7';
    let html = '<span class="tag is-stack ' + tone + '" data-tag="' + esc(p.stack) + '" title="筛选该方向">' + esc(p.stack) + '</span>';
    let list = p.tags;
    if (!list) {
      list = [];
      const short = SHORT_STACK[p.stack] || '';
      for (let i = 0; i < p.topics.length && list.length < 3; i++) {
        const cn = TOPIC_CN[p.topics[i]];
        if (!cn) continue;
        if (cn.indexOf(short) !== -1 || (short && short.indexOf(cn) !== -1)) continue;
        if (list.indexOf(cn) === -1) list.push(cn);
      }
    }
    for (let i = 0; i < list.length && i < 3; i++) {
      if (list[i] === p.stack) continue;
      html += '<span class="tag t7" data-tag="' + esc(list[i]) + '">' + esc(list[i]) + '</span>';
    }
    return html;
  }

  function cardHTML(p, idx) {
    const fav = isFav(p.id);
    const delay = Math.min(idx || 0, 14);
    const langBlock = p.lang
      ? '<span class="meta"><i class="lang-dot" style="background:' + langColor(p.lang) + '"></i>' + esc(p.lang) + '</span>'
      : '';
    const novelBadge = p.novel
      ? '<span class="badge-novel" title="' + esc(ageLabel(p.created)) + '">⚡ 新锐</span>'
      : '';
    const autoBadge = p.auto ? '<span class="badge-auto" title="由项目标签自动生成，非人工撰写">自动概述</span>' : '';
    const liveMark = p.liveStars ? ' is-live' : '';

    const enBlock = (p.auto && p.enDesc)
      ? '<p class="card-en"><span>英文原描述</span>' + esc(p.enDesc) + '</p>'
      : '';

    return '' +
      '<article class="card" style="--i:' + delay + '" data-card="' + esc(p.id) + '">' +
        '<div class="card-head">' +
          '<div class="repo-line">' +
            '<span class="repo-owner">' + esc(p.owner) + '</span>' +
            '<span class="repo-sep">/</span>' +
            '<a class="repo-name" href="' + esc(p.url) + '" target="_blank" rel="noopener noreferrer">' + esc(p.name) + '</a>' +
          '</div>' +
          '<button class="fav-btn' + (fav ? ' is-fav' : '') + '" type="button" data-fav="' + esc(p.id) + '"' +
            ' title="' + (fav ? '取消收藏' : '收藏这个项目') + '" aria-pressed="' + (fav ? 'true' : 'false') + '">' +
            (fav ? ICONS.star : ICONS.starOutline) +
          '</button>' +
        '</div>' +
        '<div class="meta-row">' +
          '<span class="meta meta-star' + liveMark + '" data-stars="' + esc(p.id) + '" title="' +
            (p.liveStars ? '已同步最新 Star（' + new Date(p.liveAt).toLocaleString('zh-CN') + '）' : '数据快照，可点上方同步') + '">' +
            ICONS.star + fmtNum(p.stars) +
          '</span>' +
          '<span class="meta">' + ICONS.fork + fmtNum(p.forks) + '</span>' +
          langBlock +
          novelBadge +
          autoBadge +
        '</div>' +
        '<div class="card-intro">' +
          '<p class="card-cn">' + esc(p.cn) + '</p>' +
          '<p class="card-line"><span class="lb lb-scene">什么时候用</span><span class="tx">' + esc(p.scene) + '</span></p>' +
          '<p class="card-line"><span class="lb lb-tip">怎么上手</span><span class="tx">' + esc(p.tip) + '</span></p>' +
          enBlock +
        '</div>' +
        '<div class="tag-list">' + tagsHTML(p) + '</div>' +
        '<div class="deploy">' +
          '<div class="cmd-row">' +
            '<span class="cmd-tag">clone</span>' +
            '<code class="cmd-code" title="' + esc(p.clone) + '">' + esc(p.clone) + '</code>' +
            '<button class="copy-btn" type="button" data-copy="' + esc(p.clone) + '" title="复制克隆命令" aria-label="复制克隆命令">' + ICONS.copy + '</button>' +
          '</div>' +
          '<div class="deploy-links">' +
            '<a class="release-link" href="' + esc(p.release) + '" target="_blank" rel="noopener noreferrer" title="前往 Releases 下载安装包">' +
              ICONS.download + 'Release 包' +
            '</a>' +
            '<a class="release-link" href="' + esc(p.url) + '/archive/HEAD.zip" target="_blank" rel="noopener noreferrer" title="下载源码压缩包">' +
              ICONS.zip + '源码 ZIP' +
            '</a>' +
          '</div>' +
        '</div>' +
        '<div class="card-foot">' +
          '<a class="gh-link" href="' + esc(p.url) + '" target="_blank" rel="noopener noreferrer">' +
            ICONS.github + 'GitHub 仓库' + ICONS.arrow +
          '</a>' +
          '<span class="pushed">' + esc(relDate(p.pushed)) + '</span>' +
        '</div>' +
      '</article>';
  }

  function renderList(container, list, limit) {
    const n = limit ? Math.min(limit, list.length) : list.length;
    let html = '';
    for (let i = 0; i < n; i++) html += cardHTML(list[i], i);
    container.innerHTML = html;
    return n;
  }

  /* ---------------- 首页 ---------------- */
  function renderHome() {
    const q = state.query.trim();
    const hero = $('#viewHome .hero');
    if (hero) hero.hidden = !!q;
    $('#quickTags').hidden = !!q;
    $('#dailyHead').hidden = !!q;

    if (!q) {
      const list = pickDaily();
      renderList($('#grid'), list, DAILY_SIZE);
      $('#resultBar').hidden = true;
      $('#emptyState').hidden = true;
      $('#loadMoreWrap').hidden = true;
      $('#liveSearchBtn').hidden = true;
      $('#backToDaily').hidden = true;

      const stacks = {};
      list.forEach(function (p) { stacks[p.stack] = 1; });
      const nov = list.filter(function (p) { return p.novel; }).length;
      $('#dailyMeta').textContent =
        list.length + ' 个 · 覆盖 ' + Object.keys(stacks).length + ' 个方向 · 含 ' + nov + ' 个新锐项目';
      return;
    }

    /* 搜索态 */
    const res = runSearch(q);
    state.results = res;
    state.shown = PAGE_SIZE;

    $('#resultBar').hidden = false;
    $('#emptyState').hidden = res.length !== 0;
    $('#backToDaily').hidden = false;
    $('#liveSearchBtn').hidden = false;
    $('#liveSearchBtn').textContent = state.liveResults.length ? '重新搜索 GitHub' : '在 GitHub 全站搜索（Star≥1000）';

    const totalNote = extraLoaded ? '' : '（更多项目仍在加载）';
    $('#resultTitle').innerHTML = '搜索 <span class="q">' + esc(q) + '</span> · 本地命中 <b>' +
      res.length + '</b> 个' + totalNote;

    const grid = $('#grid');
    let html = '';
    const n = Math.min(state.shown, res.length);
    for (let i = 0; i < n; i++) html += cardHTML(res[i], i);

    if (state.liveResults.length) {
      html += '<div class="grid-divider"><span>GitHub 实时搜索结果（本地库未收录）</span></div>';
      for (let i = 0; i < state.liveResults.length; i++) html += cardHTML(state.liveResults[i], i);
    }
    grid.innerHTML = html;

    $('#loadMoreWrap').hidden = res.length <= state.shown;
    if (res.length === 0) showEmpty(q);
  }

  function showEmpty(q) {
    $('#emptyTitle').textContent = '本地库里没有匹配「' + q + '」的项目';
    $('#emptyHint').textContent = '可以换个更通用的词，或者直接去 GitHub 全站搜索 —— 会覆盖所有 Star≥1000 的项目，包括本地没收录的。';
    const pool = ['AI Agent', 'MCP', '本地大模型', '终端', '爬虫', '可视化', '自托管', 'Rust', '数据库', '面试'];
    const box = $('#emptySuggest');
    box.innerHTML = pool.map(function (t) {
      return '<button class="chip" type="button" data-tag="' + esc(t) + '">' + esc(t) + '</button>';
    }).join('') +
      '<button class="chip is-hot" type="button" data-live="' + esc(q) + '">搜索 GitHub 全站 →</button>';
  }

  /* ---------------- 创新雷达 ---------------- */
  function renderNovel() {
    let list = NOVEL.slice();
    if (state.novelStack) list = list.filter(function (p) { return p.stack === state.novelStack; });

    list.sort(function (a, b) {
      const ra = a.stars / Math.max(1, monthsSince(a.created));
      const rb = b.stars / Math.max(1, monthsSince(b.created));
      return rb - ra;
    });

    $('#novelTitle').textContent = state.novelStack || '全部新锐项目';
    $('#novelMeta').textContent = list.length + ' 个 · 按「每月新增 Star」排序';
    renderList($('#novelGrid'), list, list.length);
  }

  function buildNovelTags() {
    const freq = new Map();
    NOVEL.forEach(function (p) { freq.set(p.stack, (freq.get(p.stack) || 0) + 1); });
    const arr = Array.from(freq.entries()).sort(function (a, b) { return b[1] - a[1]; }).slice(0, 10);
    const all = '<button class="chip' + (state.novelStack ? '' : ' is-hot') + '" type="button" data-nstack="">全部 <b>' + NOVEL.length + '</b></button>';
    $('#novelTags').innerHTML = all + arr.map(function (e) {
      const on = state.novelStack === e[0];
      return '<button class="chip' + (on ? ' is-hot' : '') + '" type="button" data-nstack="' + esc(e[0]) + '">' +
        '<i class="gdot" style="background:' + (TONE_DOT[STACK_TONE[e[0]] || 't7']) + '"></i>' +
        esc(e[0]) + '<b>' + e[1] + '</b></button>';
    }).join('');
  }

  /* ---------------- 收藏页 ---------------- */
  function renderFav() {
    const body = $('#favBody');
    const nav = $('#groupNav');
    const items = state.favs.map(function (id) { return byId.get(id); }).filter(Boolean);

    $('#favTotal').textContent = items.length;
    $('#favCount').textContent = items.length;
    $('#favCount').hidden = items.length === 0;
    $('#favTenK').textContent = items.filter(function (p) { return p.stars >= 10000; }).length;

    if (!items.length) {
      nav.hidden = true;
      $('#favGroups').textContent = '0';
      body.innerHTML =
        '<div class="empty">' +
          '<div class="empty-icon">★</div>' +
          '<h3>还没有收藏任何项目</h3>' +
          '<p>回到每日推荐，点卡片右上角的星标就能收藏。收藏会按技术方向自动分组，数据只存在你自己的浏览器里。</p>' +
          '<div class="empty-suggest"><a class="chip is-hot" href="#/">去逛今日推荐</a>' +
          '<a class="chip" href="#/novel">看新锐项目</a></div>' +
        '</div>';
      return;
    }

    const groups = new Map();
    items.forEach(function (p) {
      if (!groups.has(p.stack)) groups.set(p.stack, []);
      groups.get(p.stack).push(p);
    });
    const sorted = Array.from(groups.entries()).sort(function (a, b) {
      return b[1].length - a[1].length || a[0].localeCompare(b[0], 'zh');
    });

    $('#favGroups').textContent = sorted.length;

    nav.hidden = false;
    nav.innerHTML = sorted.map(function (g) {
      return '<button class="chip" type="button" data-anchor="' + esc(slug(g[0])) + '">' +
        '<i class="gdot" style="background:' + (TONE_DOT[STACK_TONE[g[0]] || 't7']) + '"></i>' +
        esc(g[0]) + '<b>' + g[1].length + '</b></button>';
    }).join('');

    body.innerHTML = sorted.map(function (g) {
      return '<section class="fav-group" id="' + esc(slug(g[0])) + '">' +
        '<div class="fav-group-head">' +
          '<h2>' + esc(g[0]) + '</h2>' +
          '<span class="group-count">' + g[1].length + ' 个</span>' +
          '<span class="group-line"></span>' +
        '</div>' +
        '<div class="grid">' + g[1].map(cardHTML).join('') + '</div>' +
      '</section>';
    }).join('');
  }

  function slug(s) { return 'g-' + s.replace(/[^\w\u4e00-\u9fa5]/g, ''); }

  /* ---------------- 视图切换 ---------------- */
  function render() {
    const v = state.view;
    $('#viewHome').hidden = v !== 'home';
    $('#viewNovel').hidden = v !== 'novel';
    $('#viewFav').hidden = v !== 'fav';

    $$('[data-nav]').forEach(function (el) {
      el.classList.toggle('is-active', el.dataset.nav === v);
    });

    if (v === 'home') renderHome();
    else if (v === 'novel') { buildNovelTags(); renderNovel(); }
    else renderFav();
  }

  function route() {
    const h = location.hash || '#/';
    state.view = h.indexOf('/favorites') !== -1 ? 'fav'
      : h.indexOf('/novel') !== -1 ? 'novel'
      : 'home';
    state.liveResults = [];
    render();
    window.scrollTo(0, 0);
  }

  /* ---------------- 收藏交互 ---------------- */
  function toggleFav(id, btn) {
    const i = state.favs.indexOf(id);
    if (i !== -1) {
      state.favs.splice(i, 1);
      toast('已取消收藏');
    } else {
      state.favs.unshift(id);
      toast('已收藏 · 保存在本机浏览器');
    }
    saveFavs();

    const now = isFav(id);
    if (btn) {
      btn.classList.toggle('is-fav', now);
      btn.innerHTML = now ? ICONS.star : ICONS.starOutline;
      btn.title = now ? '取消收藏' : '收藏这个项目';
      btn.setAttribute('aria-pressed', now ? 'true' : 'false');
    }
    syncFavCounters();
    if (state.view === 'fav') {
      const y = window.scrollY;
      renderFav();
      window.scrollTo(0, y);
    }
  }

  function syncFavCounters() {
    const n = state.favs.length;
    const badge = $('#favCount');
    badge.textContent = n;
    badge.hidden = n === 0;
  }

  /* ---------------- 复制 ---------------- */
  function copyText(text, btn) {
    function done() {
      if (btn) {
        btn.classList.add('is-done');
        setTimeout(function () { btn.classList.remove('is-done'); }, 1400);
      }
      toast('克隆命令已复制');
    }
    function fallback() {
      const ta = document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.cssText = 'position:fixed;top:-9999px;left:-9999px;opacity:0';
      document.body.appendChild(ta);
      ta.select();
      let ok = false;
      try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
      document.body.removeChild(ta);
      if (ok) done(); else toast('复制失败，请手动选中命令');
    }
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(done).catch(fallback);
    } else fallback();
  }

  /* ---------------- Toast ---------------- */
  let toastTimer = null;
  function toast(msg) {
    const el = $('#toast');
    el.innerHTML = ICONS.check + '<span>' + esc(msg) + '</span>';
    el.classList.add('is-show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { el.classList.remove('is-show'); }, 2200);
  }

  /* ---------------- 搜索交互 ---------------- */
  let searchTimer = null;

  function setQuery(q, focus) {
    const input = $('#searchInput');
    input.value = q;
    state.query = q;
    state.liveResults = [];
    updateClearBtn();
    if (state.view !== 'home') {
      try { history.replaceState(null, '', '#/'); } catch (e) { location.hash = '#/'; }
      state.view = 'home';
      $$('[data-nav]').forEach(function (el) { el.classList.toggle('is-active', el.dataset.nav === 'home'); });
      $('#viewHome').hidden = false;
      $('#viewNovel').hidden = true;
      $('#viewFav').hidden = true;
    }
    renderHome();
    if (focus) input.focus();
  }

  function updateClearBtn() {
    $('#searchClear').hidden = !$('#searchInput').value;
  }

  /* ---------------- 换一批 ---------------- */
  function shuffleBatch() {
    if (state.query) setQuery('');
    if (state.view !== 'home') { location.hash = '#/'; }
    state.batch += 1;
    const grid = $('#grid');
    grid.style.opacity = '0';
    setTimeout(function () {
      renderHome();
      grid.style.opacity = '';
    }, 110);
    const btn = $('#shuffleBtn');
    btn.classList.remove('is-spinning');
    void btn.offsetWidth;
    btn.classList.add('is-spinning');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  /* ---------------- GitHub 接口 ---------------- */
  function getToken() {
    try { return localStorage.getItem(TOKEN_KEY) || ''; } catch (e) { return ''; }
  }

  function ghHeaders() {
    const h = { 'Accept': 'application/vnd.github+json' };
    const t = getToken();
    if (t) h['Authorization'] = 'Bearer ' + t;
    return h;
  }

  /* 同步当前页卡片的实时 Star */
  function visibleIds() {
    const cards = $$('#viewHome .card, #viewNovel .card, #viewFav .card');
    const ids = [];
    cards.forEach(function (c) {
      const id = c.dataset.card;
      if (id && byId.has(id) && ids.indexOf(id) === -1) ids.push(id);
    });
    return ids;
  }

  let syncing = false;
  async function syncStars() {
    if (syncing) return;
    const ids = visibleIds().slice(0, 12);
    if (!ids.length) return;
    syncing = true;
    const btn = $('#syncBtn');
    const note = $('#syncNote');
    btn.disabled = true;
    note.className = 'sync-note';
    note.textContent = '同步中 0/' + ids.length;
    $('#syncBtnText').textContent = '同步中…';

    let ok = 0, failed = 0;
    for (let i = 0; i < ids.length; i++) {
      try {
        const r = await fetch('https://api.github.com/repos/' + ids[i], { headers: ghHeaders() });
        if (r.status === 403 || r.status === 429) throw new Error('rate');
        if (!r.ok) throw new Error('http');
        const d = await r.json();
        const p = byId.get(ids[i]);
        if (p && typeof d.stargazers_count === 'number') {
          p.stars = d.stargazers_count;
          p.forks = d.forks_count;
          p.liveStars = d.stargazers_count;
          p.liveAt = Date.now();
          liveCache[p.id] = { s: d.stargazers_count, t: Date.now() };
          const el = document.querySelector('[data-stars="' + cssEsc(p.id) + '"]');
          if (el) {
            el.classList.add('is-live');
            el.innerHTML = ICONS.star + fmtNum(p.stars);
            el.title = '已同步最新 Star（' + new Date().toLocaleTimeString('zh-CN') + '）';
          }
          ok++;
        }
      } catch (e) {
        failed++;
        if (e.message === 'rate') break;
      }
      note.textContent = '同步中 ' + (i + 1) + '/' + ids.length;
    }
    saveLiveCache();
    btn.disabled = false;
    $('#syncBtnText').textContent = '同步最新 Star';
    note.className = 'sync-note ' + (ok ? 'is-ok' : 'is-err');
    note.textContent = ok
      ? '已更新 ' + ok + ' 个项目的实时 Star'
      : (failed ? '接口限流了，稍后再试或填入 Token' : '没有可同步的项目');
    if (ok) toast('已同步 ' + ok + ' 个项目的实时 Star');
    syncing = false;
  }

  function cssEsc(s) { return String(s).replace(/["\\]/g, '\\$&'); }

  /* 实时搜索 GitHub 全站（覆盖所有 Star≥1000） */
  async function liveSearch(q) {
    if (!q || state.liveLoading) return;
    state.liveLoading = true;
    const btn = $('#liveSearchBtn');
    const old = btn.textContent;
    btn.disabled = true;
    btn.textContent = '正在请求 GitHub…';
    $('#extraLoading').hidden = false;

    try {
      const url = 'https://api.github.com/search/repositories?q=' +
        encodeURIComponent(q + ' stars:>=1000') + '&sort=stars&order=desc&per_page=30';
      const res = await fetch(url, { headers: ghHeaders() });
      if (res.status === 403 || res.status === 429) throw new Error('rate');
      if (!res.ok) throw new Error('http');
      const data = await res.json();
      const items = (data.items || []).slice(0, 30);

      state.liveResults = items.map(function (it) {
        const p = normalize({
          f: it.full_name, s: it.stargazers_count, k: it.forks_count,
          l: it.language || '', t: (it.topics || []).slice(0, 8),
          c: (it.created_at || '').slice(0, 7), p: (it.pushed_at || '').slice(0, 10),
          a: it.archived ? 1 : 0
        });
        p.enDesc = it.description || '';
        p.live = true;
        ensureText(p);
        p.novel = isNovel(p);
        return p;
      });

      if (!state.liveResults.length) {
        toast('GitHub 上也没有找到匹配的千星项目');
      } else {
        toast('从 GitHub 拿到 ' + state.liveResults.length + ' 个实时结果');
      }
      renderHome();
    } catch (e) {
      toast(e.message === 'rate'
        ? 'GitHub 接口限流，请等 1 分钟或填入 Token'
        : '请求 GitHub 失败，检查网络后重试');
    } finally {
      state.liveLoading = false;
      btn.disabled = false;
      btn.textContent = old;
      $('#extraLoading').hidden = true;
    }
  }

  /* ---------------- 懒加载第二批数据 ---------------- */
  let extraLoading = false;

  function loadExtra() {
    if (window.GH_DATA_EXTRA_LOADED || extraLoading) return;
    extraLoading = true;
    const s = document.createElement('script');
    s.src = 'assets/data-extra.js';
    s.onload = function () {
      const d = window.GH_DATA_EXTRA;
      if (!d || !d.projects || !d.projects.length) {
        extraLoading = false;
        $('#extraLoading').hidden = true;
        return;
      }
      addAll(d.projects);
      window.GH_DATA_EXTRA_LOADED = true;
      extraLoaded = true;
      rebuildDerived();
      initStats();
      $('#extraLoading').hidden = true;
      if (state.view === 'home') renderHome();
      if (state.view === 'novel') { buildNovelTags(); renderNovel(); }
    };
    s.onerror = function () { extraLoading = false; $('#extraLoading').hidden = true; };
    document.body.appendChild(s);
  }

  /* ---------------- 统计 ---------------- */
  function initStats() {
    /* 优先用构建时统计的总量（含尚未加载的扩展包），加载完再以前端实际数为准 */
    const pool = Math.max(projects.length, META.total || 0);
    $('#statPool').textContent = fmtNum(pool);
    $('#statTenK').textContent = fmtNum(TENK.length);
    $('#statNovel').textContent = fmtNum(NOVEL.length);
    const stacks = {};
    projects.forEach(function (p) { stacks[p.stack] = 1; });
    $('#statStacks').textContent = Object.keys(stacks).length;
    $('#heroDate').textContent = todayLabel();
    $('#footUpdated').textContent = META.updated || '未知';

    const t = META.built ? new Date(META.built) : null;
    if (t) {
      const days = Math.floor((Date.now() - t.getTime()) / 86400000);
      $('#dataAge').textContent = days <= 0 ? '数据快照：今天' : '数据快照：' + days + ' 天前';
    }
    syncFavCounters();
  }

  /* ---------------- 快捷标签 ---------------- */
  function buildQuickTags() {
    const wanted = ['AI Agent', 'MCP', '本地大模型', 'AI 编程', 'RAG', '自托管',
                    '终端', '爬虫', '可视化', 'Rust', 'DevOps', '知识库'];
    const valid = [];
    for (let i = 0; i < wanted.length && valid.length < 12; i++) {
      const t = wanted[i];
      if (runSearch(t).length >= 3) valid.push(t);
    }
    $('#quickTags').innerHTML = valid.map(function (t) {
      return '<button class="chip" type="button" data-tag="' + esc(t) + '">' + esc(t) + '</button>';
    }).join('');
  }

  /* ---------------- 设置（Token） ---------------- */
  function initSettings() {
    const panel = $('#settingsPanel');
    const input = $('#tokenInput');
    const btn = $('#settingsBtn');

    btn.addEventListener('click', function () {
      panel.hidden = !panel.hidden;
      btn.classList.toggle('is-on', !panel.hidden);
      if (!panel.hidden) {
        input.value = getToken();
        input.focus();
      }
    });
    $('#tokenSave').addEventListener('click', function () {
      try { localStorage.setItem(TOKEN_KEY, input.value.trim()); } catch (e) { /* 忽略 */ }
      toast(input.value.trim() ? 'Token 已保存到本机' : 'Token 已清空');
      panel.hidden = true;
      btn.classList.remove('is-on');
    });
    $('#tokenClear').addEventListener('click', function () {
      try { localStorage.removeItem(TOKEN_KEY); } catch (e) { /* 忽略 */ }
      input.value = '';
      toast('Token 已清除');
    });
  }

  /* ---------------- 事件 ---------------- */
  document.addEventListener('click', function (e) {
    const favBtn = e.target.closest('[data-fav]');
    if (favBtn) { toggleFav(favBtn.dataset.fav, favBtn); return; }

    const copyBtn = e.target.closest('[data-copy]');
    if (copyBtn) { copyText(copyBtn.dataset.copy, copyBtn); return; }

    const nstack = e.target.closest('[data-nstack]');
    if (nstack) { state.novelStack = nstack.dataset.nstack; buildNovelTags(); renderNovel(); return; }

    const liveBtn = e.target.closest('[data-live]');
    if (liveBtn) { liveSearch(liveBtn.dataset.live); return; }

    const tagEl = e.target.closest('[data-tag]');
    if (tagEl) {
      e.preventDefault();
      setQuery(tagEl.dataset.tag, true);
      window.scrollTo({ top: 0, behavior: 'smooth' });
      return;
    }

    const anchorBtn = e.target.closest('[data-anchor]');
    if (anchorBtn) {
      const t = document.getElementById(anchorBtn.dataset.anchor);
      if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' });
      return;
    }
  });

  const input = $('#searchInput');
  input.addEventListener('input', function () {
    updateClearBtn();
    clearTimeout(searchTimer);
    searchTimer = setTimeout(function () {
      state.query = input.value;
      state.liveResults = [];
      if (state.view !== 'home') {
        try { history.replaceState(null, '', '#/'); } catch (e) { location.hash = '#/'; }
        state.view = 'home';
        $('#viewHome').hidden = false;
        $('#viewNovel').hidden = true;
        $('#viewFav').hidden = true;
        $$('[data-nav]').forEach(function (el) {
          el.classList.toggle('is-active', el.dataset.nav === 'home');
        });
      }
      renderHome();
    }, 150);
  });

  input.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { setQuery(''); input.blur(); }
    if (e.key === 'Enter') {
      const q = input.value.trim();
      if (q && runSearch(q).length === 0) liveSearch(q);
    }
  });

  $('#searchClear').addEventListener('click', function () { setQuery('', true); });
  $('#backToDaily').addEventListener('click', function () {
    setQuery('');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
  $('#shuffleBtn').addEventListener('click', shuffleBatch);
  $('#syncBtn').addEventListener('click', syncStars);
  $('#liveSearchBtn').addEventListener('click', function () {
    liveSearch($('#searchInput').value.trim());
  });
  $('#loadMoreBtn').addEventListener('click', function () {
    state.shown += PAGE_SIZE;
    const y = window.scrollY;
    renderHome();
    window.scrollTo(0, y);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && document.activeElement !== input) {
      e.preventDefault();
      input.focus();
      input.select();
    }
  });

  window.addEventListener('hashchange', route);

  /* ---------------- 启动 ---------------- */
  function boot() {
    const D = window.GH_DATA || { meta: {}, projects: [] };
    META = D.meta || {};
    addAll(D.projects || []);
    loadLiveCache();
    rebuildDerived();
    state.favs = loadFavs();

    /* ?q= 直接进搜索结果 */
    try {
      const q = new URLSearchParams(location.search).get('q');
      if (q) {
        state.query = q;
        input.value = q;
        updateClearBtn();
      }
    } catch (e) { /* 忽略 */ }

    initStats();
    buildQuickTags();
    initSettings();
    route();

    /* 首屏渲染完再拉第二批，避免拖慢打开速度 */
    setTimeout(loadExtra, 420);
  }

  boot();
})();
