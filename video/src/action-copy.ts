/** Task-specific Instagram cuts. Wording is ours; outcomes follow live tasks. */
export type ActionKind = 'company' | 'table' | 'first-night';
export type ActionCut = {
  id: string;
  kind: ActionKind;
  seconds: number;
  hook: string;
  result: string;
  proof: string;
  home: string;
  away: string;
  close: string;
  route: string;
  screenshot: string;
  firstStep: string;
};

export const COMPANY: ActionCut = {
  id: 'Action-company', kind: 'company', seconds: 20,
  hook: "You want them over.\nYour place isn't ready.",
  result: 'Room to sit.\nReady for company.',
  proof: 'Six steps to get\nyour place ready.',
  home: 'Home now? Start the checklist.',
  away: "Away? Schedule when you'll get ready.",
  close: 'Get ready\nfor company.',
  route: 'guests', screenshot: 'guests-step.png',
  firstStep: 'Bag the kitchen trash and let in fresh air.',
};
export const COMPANY_ALT: ActionCut = {...COMPANY, id: 'Action-company-alt',
  hook: 'Friends coming over?\nGet the place ready.'};
export const TABLE: ActionCut = {
  id: 'Action-table', kind: 'table', seconds: 20,
  hook: "Dinner's ready.\nThere's nowhere to eat.",
  result: 'Somewhere to sit.\nRoom to eat.',
  proof: 'Clear the table.\nFollow six steps.',
  home: 'Home now? Start at the table.',
  away: 'Away? Schedule before your next meal.',
  close: 'Make room\nfor dinner.',
  route: 'dinner', screenshot: 'dinner-step.png',
  firstStep: 'Throw away the obvious trash.',
};
export const FIRST_NIGHT: ActionCut = {
  id: 'Action-first-night', kind: 'first-night', seconds: 21,
  hook: 'Moving in today?\nMake tonight work first.',
  result: 'Bed ready.\nEssentials out.',
  proof: 'Your first night.\nSix useful steps.',
  home: "Home now? Start tonight's setup.",
  away: "Away? Schedule tonight's setup.",
  close: 'Make your\nfirst night work.',
  route: 'first-night', screenshot: 'first-night-step.png',
  firstStep: 'Photograph each room before unpacking more.',
};
