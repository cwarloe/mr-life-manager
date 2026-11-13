import React from 'react';
import {Composition} from 'remotion';
import {AUDIENCES} from './copy';
import {DURATION, FPS, Promo} from './Promo';
import {ActionPromo} from './ActionPromo';
import {COMPANY, COMPANY_ALT, TABLE, FIRST_NIGHT} from './action-copy';

// One vertical (9:16) video per audience: 1080x1920 for Reels, Shorts and TikTok.
export const Root: React.FC = () => (
  <>
    <Composition id="Action-company" component={ActionPromo} durationInFrames={20 * FPS} fps={FPS} width={1080} height={1920} defaultProps={{cut: COMPANY}} />
    <Composition id="Action-company-alt" component={ActionPromo} durationInFrames={20 * FPS} fps={FPS} width={1080} height={1920} defaultProps={{cut: COMPANY_ALT}} />
    <Composition id="Action-table" component={ActionPromo} durationInFrames={20 * FPS} fps={FPS} width={1080} height={1920} defaultProps={{cut: TABLE}} />
    <Composition id="Action-first-night" component={ActionPromo} durationInFrames={21 * FPS} fps={FPS} width={1080} height={1920} defaultProps={{cut: FIRST_NIGHT}} />
    {AUDIENCES.map((a) => (
      <Composition
        key={a.id}
        id={`Promo-${a.id}`}
        component={Promo}
        durationInFrames={DURATION}
        fps={FPS}
        width={1080}
        height={1920}
        defaultProps={{audience: a}}
      />
    ))}
  </>
);
