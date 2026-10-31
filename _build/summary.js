/* 生成 Actions 运行摘要：读取构建出来的 meta 写进 GITHUB_STEP_SUMMARY */
const fs = require('fs');
const path = require('path');

const p = path.join(__dirname, '..', 'assets', 'data.js');
const lines = [];

function grab(file, varName) {
  if (!fs.existsSync(file)) return null;
  const src = fs.readFileSync(file, 'utf8');
  const i = src.indexOf('window.' + varName + ' = ');
  if (i === -1) return null;
  try {
    return JSON.parse(src.slice(i + ('window.' + varName + ' = ').length).replace(/;\s*$/, ''));
  } catch (e) {
    return null;
  }
}

const main = grab(p, 'GH_DATA');
const extra = grab(path.join(__dirname, '..', 'assets', 'data-extra.js'), 'GH_DATA_EXTRA');

if (main && main.meta) {
  const m = main.meta;
  lines.push('## 本次数据更新结果\n');
  lines.push('| 项目 | 数量 |');
  lines.push('| --- | --- |');
  lines.push('| 快照日期 | ' + m.updated + ' |');
  lines.push('| 万星池（Star ≥ 10000） | ' + m.ge10k + ' |');
  lines.push('| 扩展池（5000~9999） | ' + (extra ? extra.projects.length : 0) + ' |');
  lines.push('| 可搜索合计 | ' + m.total + ' |');
  lines.push('| 人工精选（含手写中文） | ' + m.curated + ' |');
} else {
  lines.push('## 数据更新结果\n');
  lines.push('未能读取到数据文件，请检查上方日志。');
}

const text = lines.join('\n') + '\n';
const out = process.env.GITHUB_STEP_SUMMARY;
if (out) {
  fs.appendFileSync(out, text);
}
process.stdout.write(text);
