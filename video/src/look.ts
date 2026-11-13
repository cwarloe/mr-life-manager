import looksJson from './generated/looks.json';

export type Vars = Record<string, string>;
export type Family = 'career' | 'students' | 'military';

const looks = looksJson as Record<string, Vars>;

/** Colors and fonts for one look, read from the site's tokens.css (see scripts/sync.mjs). */
export function getLook(name: string): {v: Vars; family: Family} {
  const v = looks[name];
  if (!v) throw new Error(`Unknown look "${name}". Known: ${Object.keys(looks).join(', ')}`);
  return {v, family: name.split('-')[0] as Family};
}

export const UI = '"Archivo", system-ui, -apple-system, "Segoe UI", sans-serif';
export const DISPLAY: Record<Family, string> = {
  career: UI,
  students: '"Bangers", "Comic Sans MS", Impact, sans-serif',
  military: '"Saira Stencil One", "Arial Black", Impact, sans-serif',
};
/** Display fonts are all-caps in two of the looks. */
export const CAPS: Record<Family, boolean> = {career: false, students: true, military: true};

/** Phone safe area at 1080x1920: keep text out of the strips the apps cover with buttons and captions. */
export const SAFE = {top: 230, bottom: 430, side: 72};
