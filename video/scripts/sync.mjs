// Reads the site's design tokens and fonts so the videos always match the site.
// Source of truth: ../products/landing/assets/tokens.css (see ../products/landing/THEMING.md).
// Writes src/generated/looks.json and copies the self-hosted fonts into public/fonts.
// Both outputs are generated (git-ignored); `npm run sync` runs before studio, still and render.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const assets = path.resolve(here, '../../products/landing/assets');
const css = fs.readFileSync(path.join(assets, 'tokens.css'), 'utf8').replace(/\/\*[\s\S]*?\*\//g, '');

const decls = (body) => {
  const out = {};
  for (const m of body.matchAll(/--([a-z0-9-]+)\s*:\s*([^;]+);/g)) out[m[1]] = m[2].trim();
  return out;
};
// Top-level rules only: the dark-mode variants sit inside @media and are skipped on purpose.
const rules = [];
let depth = 0, start = 0, sel = '';
for (let i = 0; i < css.length; i++) {
  const c = css[i];
  if (c === '{') {
    if (depth === 0) { sel = css.slice(start, i).trim(); start = i + 1; }
    depth++;
  } else if (c === '}') {
    depth--;
    if (depth === 0) { rules.push([sel, css.slice(start, i)]); start = i + 1; }
    // `@media screen{ ... }` wraps the look blocks: descend into it.
    else if (depth === 1 && /^@media screen/.test(sel)) { /* inner rule closed; keep scanning */ }
  }
}
// Pull the look rules out of `@media screen{...}` (their bodies hold nested rules).
const flat = [];
for (const [s, b] of rules) {
  if (/^@media screen/.test(s)) {
    for (const m of b.matchAll(/(^|\n)\s*(\[data-look[^\{]+)\{([^{}]*)\}/g)) flat.push([m[2].trim(), m[3]]);
  } else if (!s.startsWith('@')) flat.push([s, b]);
}
const base = {};
for (const [s, b] of flat) if (s === ':root,[data-palette]') Object.assign(base, decls(b));

const looks = {};
const names = new Set();
for (const [s] of flat) { const m = s.match(/^\[data-look="([^"]+)"\]$/); if (m) names.add(m[1]); }
const resolve = (vars) => {
  for (let pass = 0; pass < 4; pass++)
    for (const k of Object.keys(vars))
      vars[k] = vars[k].replace(/var\(--([a-z0-9-]+)\)/g, (_, n) => vars[n] ?? `var(--${n})`);
  return vars;
};
for (const name of names) {
  const family = name.split('-')[0];
  const v = {...base};
  for (const [s, b] of flat) {
    if (s === `[data-look^="${family}-"]` || s === `[data-look="${name}"]`) Object.assign(v, decls(b));
  }
  looks[name] = resolve(v);
}
fs.mkdirSync(path.join(here, '../src/generated'), {recursive: true});
fs.writeFileSync(path.join(here, '../src/generated/looks.json'), JSON.stringify(looks, null, 2));

const fonts = path.join(here, '../public/fonts');
fs.mkdirSync(fonts, {recursive: true});
for (const f of ['archivo.woff2', 'bangers.woff2', 'saira-stencil-one.woff2']) {
  fs.copyFileSync(path.join(assets, 'fonts', f), path.join(fonts, f));
}
console.log(`sync: ${names.size} looks, 3 fonts`);
