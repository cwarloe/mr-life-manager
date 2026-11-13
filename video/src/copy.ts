// The words in the videos. DRAFT: these are the flier lines under review in
// ../docs/copy/ (see docs/copy/README.md). When reviewers change a line there,
// change it here too; nothing else in the video holds wording.
// Rules: plain speech, every verb gets its object, about right now (content/README.md).

export type Audience = {
  /** Short id used in file names and tags. */
  id: 'students' | 'career' | 'military';
  /** Which look in tokens.css colors this video. */
  look: string;
  /** The line at the top of the flier. */
  hook: string;
  /** Three problems, in the reader's words (flier boxes). */
  problems: [string, string, string];
  /** What the scan page shows as its heading (the first problem). */
  scanHeading: string;
  /** What they'll do, for the "pick a day and time" screen. */
  task: string;
  /** Address to show at the end. */
  url: string;
};

export const SHARED = {
  scanLabel: 'You scanned this one:',
  home: "I'm home now. Let's start.",
  away: "I'm not home yet. Let me pick a day and time.",
  pickLead: 'Not home? Pick the day and time you’ll do it.',
  remind: 'Your phone will remind you.',
  when: 'Saturday at 10:00 a.m.',
  addCal: 'Add to my calendar',
  offer: 'A free checklist.',
  noApp: 'No app to download.',
  noEmail: 'No email needed.',
  sound: 'Sound like your place?',
} as const;

export const AUDIENCES: Audience[] = [
  {
    id: 'students',
    look: 'students-blue',
    hook: 'Living on your own for the first time?',
    problems: [
      "Your dishes are piling up, there are clothes all over the floor, and you haven't opened your mail.",
      "People are coming over tonight and your place isn't ready.",
      'Your kitchen table is covered with stuff and you end up eating on your bed.',
    ],
    scanHeading: "Your dishes are piling up, there are clothes all over the floor, and you haven't opened your mail.",
    task: 'wash the dishes and pick up your place',
    url: 'mrlifemanager.com/students',
  },
  {
    id: 'career',
    look: 'career-teal',
    hook: 'Working long hours and living on your own for the first time?',
    problems: [
      'You keep getting home late, and the dishes and mail keep piling up.',
      "Someone's coming over tonight and your place isn't ready.",
      'Your kitchen table is covered with stuff and you end up eating standing at the counter.',
    ],
    scanHeading: 'You keep getting home late, and the dishes and mail keep piling up.',
    task: 'wash the dishes and pick up your place',
    url: 'mrlifemanager.com/career',
  },
  {
    id: 'military',
    look: 'military-navy',
    hook: 'Living off base for the first time?',
    problems: [
      "You just moved into your first place off base, and your household goods haven't arrived yet.",
      "People from your unit are coming over tonight and your place isn't ready.",
      'Your spare room is still full of boxes from the move.',
    ],
    scanHeading: "You just moved into your first place off base, and your household goods haven't arrived yet.",
    task: 'get your new place set up for tonight',
    url: 'mrlifemanager.com/military',
  },
];
