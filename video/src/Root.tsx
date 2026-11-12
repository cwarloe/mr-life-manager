import React from 'react';
import {Composition} from 'remotion';
import {AUDIENCES} from './copy';
import {DURATION, FPS, Promo} from './Promo';

// One vertical (9:16) video per audience: 1080x1920 for Reels, Shorts and TikTok.
export const Root: React.FC = () => (
  <>
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
