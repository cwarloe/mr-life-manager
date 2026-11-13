import React, {useEffect, useState} from 'react';
import {
  AbsoluteFill,
  Easing,
  Sequence,
  continueRender,
  delayRender,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {Audience, SHARED} from './copy';
import {CAPS, DISPLAY, Family, SAFE, UI, Vars, getLook} from './look';

export type PromoProps = {audience: Audience};

export const FPS = 30;
export const DURATION = 800; // frames: about 26.7 seconds at 30 fps

/* ---------- fonts (the site's self-hosted files, copied by scripts/sync.mjs) ---------- */
const FONT_FILES: [string, string, string?][] = [
  ['Archivo', 'fonts/archivo.woff2', '400 800'],
  ['Bangers', 'fonts/bangers.woff2'],
  ['Saira Stencil One', 'fonts/saira-stencil-one.woff2'],
];
function useFonts() {
  const [handle] = useState(() => delayRender('fonts'));
  useEffect(() => {
    Promise.all(
      FONT_FILES.map(async ([family, file, weight]) => {
        const face = new FontFace(family, `url(${staticFile(file)})`, weight ? {weight} : {});
        await face.load();
        document.fonts.add(face);
      }),
    )
      .catch((e) => console.error('font load failed', e))
      .finally(() => continueRender(handle));
  }, [handle]);
}

/* ---------- small helpers ---------- */
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;

/** Fades a scene in and out so cuts don't pop. */
const Fade: React.FC<{duration: number; children: React.ReactNode; inFrames?: number; outFrames?: number}> = ({
  duration,
  children,
  inFrames = 8,
  outFrames = 8,
}) => {
  const f = useCurrentFrame();
  const o = outFrames > 0
    ? interpolate(f, [0, inFrames, duration - outFrames, duration], [0, 1, 1, 0], clamp)
    : interpolate(f, [0, inFrames], [0, 1], clamp);
  return <AbsoluteFill style={{opacity: o}}>{children}</AbsoluteFill>;
};

/** Words rise in one after another. */
const Words: React.FC<{text: string; start?: number; stagger?: number; style?: React.CSSProperties; hi?: Vars}> = ({
  text,
  start = 0,
  stagger = 3,
  style,
}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  return (
    <div style={{display: 'flex', flexWrap: 'wrap', gap: '0 0.28em', ...style}}>
      {text.split(' ').map((w, i) => {
        const p = spring({frame: f - start - i * stagger, fps, config: {damping: 14, stiffness: 160}});
        return (
          <span key={i} style={{display: 'inline-block', opacity: p, transform: `translateY(${(1 - p) * 40}px)`}}>
            {w}
          </span>
        );
      })}
    </div>
  );
};

/* ---------- background, per family ---------- */
const Background: React.FC<{v: Vars; family: Family}> = ({v, family}) => {
  const f = useCurrentFrame();
  const drift = interpolate(f, [0, DURATION], [0, -120]);
  const base: React.CSSProperties = {backgroundColor: v.paper};
  if (family === 'students') {
    return (
      <AbsoluteFill
        style={{
          ...base,
          backgroundImage: `radial-gradient(${v.dots} 3px, transparent 4px)`,
          backgroundSize: '34px 34px',
          backgroundPosition: `0 ${drift}px`,
        }}
      />
    );
  }
  if (family === 'military') {
    return (
      <AbsoluteFill style={base}>
        <div style={{position: 'absolute', left: 0, right: 0, top: 0, height: 120, background: v.dark}} />
        <div style={{position: 'absolute', left: 0, right: 0, top: 120, height: 16, background: v.accent}} />
        <div
          style={{
            position: 'absolute',
            inset: '170px 36px 36px',
            border: `4px dashed ${v.rule}`,
            transform: `translateY(${drift / 20}px)`,
          }}
        />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={base}>
      <div
        style={{
          position: 'absolute',
          width: 1100,
          height: 1100,
          borderRadius: '50%',
          background: v['accent-soft'],
          left: -300,
          top: -380 + drift / 6,
        }}
      />
      <div
        style={{
          position: 'absolute',
          width: 760,
          height: 760,
          borderRadius: '50%',
          background: v['second-soft'],
          right: -300,
          bottom: 120 - drift / 8,
        }}
      />
    </AbsoluteFill>
  );
};

/* ---------- pieces ---------- */
const Tag: React.FC<{v: Vars; family: Family; children: React.ReactNode}> = ({v, family, children}) => {
  const style: React.CSSProperties =
    family === 'career'
      ? {background: v.accent, color: v['on-accent'], borderRadius: 999, padding: '10px 26px'}
      : family === 'students'
        ? {background: v.tape, color: v.ink, border: `4px solid ${v.ink}`, padding: '6px 22px'}
        : {background: v.tape, color: v.ink, padding: '8px 24px', transform: 'rotate(-1.5deg)'};
  return (
    <span
      style={{
        display: 'inline-block',
        fontFamily: DISPLAY[family],
        textTransform: 'uppercase',
        letterSpacing: family === 'career' ? 3 : 2,
        fontSize: 38,
        fontWeight: family === 'career' ? 700 : 400,
        ...style,
      }}
    >
      {children}
    </span>
  );
};

const panelStyle = (v: Vars, family: Family): React.CSSProperties =>
  family === 'career'
    ? {background: v.surface, borderRadius: 36, borderLeft: `18px solid ${v.accent}`, boxShadow: '0 18px 48px rgba(15,29,43,.14)'}
    : family === 'students'
      ? {background: v.surface, border: `6px solid ${v.ink}`, borderLeft: `26px solid ${v.accent}`, boxShadow: `12px 12px 0 ${v.ink}`}
      : {background: v.surface, border: `5px solid ${v.dark}`, borderLeft: `22px solid ${v.accent}`, outline: `3px dashed ${v.rule}`, outlineOffset: -14};

const headline = (v: Vars, family: Family, size: number): React.CSSProperties => ({
  fontFamily: DISPLAY[family],
  fontWeight: family === 'career' ? 800 : 400,
  textTransform: CAPS[family] ? 'uppercase' : 'none',
  letterSpacing: family === 'career' ? -2 : family === 'students' ? 1.5 : 1,
  lineHeight: 1.05,
  fontSize: size,
  color: v.ink,
  textShadow: family === 'students' ? `6px 6px 0 ${v.tape}` : undefined,
});

const body = (v: Vars, size: number, weight = 600): React.CSSProperties => ({
  fontFamily: UI,
  fontWeight: weight,
  fontSize: size,
  lineHeight: 1.22,
  color: v.ink,
});

/* ---------- scenes ---------- */
const Hook: React.FC<{a: Audience; v: Vars; family: Family}> = ({a, v, family}) => {
  const size = a.hook.length < 45 ? 150 : a.hook.length < 60 ? 124 : 108;
  return (
    <AbsoluteFill style={{padding: `${SAFE.top}px ${SAFE.side}px ${SAFE.bottom}px`, justifyContent: 'center', gap: 50}}>
      <div>
        <Tag v={v} family={family}>Mr. Life Manager</Tag>
      </div>
      <Words text={a.hook} start={6} stagger={4} style={headline(v, family, size)} />
    </AbsoluteFill>
  );
};

const Problems: React.FC<{a: Audience; v: Vars; family: Family}> = ({a, v, family}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const each = 100;
  return (
    <AbsoluteFill style={{padding: `${SAFE.top}px ${SAFE.side}px ${SAFE.bottom}px`, gap: 36}}>
      <div>
        <Tag v={v} family={family}>{SHARED.sound}</Tag>
      </div>
      <div style={{position: 'relative', flex: 1}}>
        {a.problems.map((text, i) => {
          const local = f - i * each;
          const p = spring({frame: local, fps, config: {damping: 15, stiffness: 140}});
          const out = interpolate(local, [each - 8, each], [1, 0], clamp);
          const visible = local >= 0 && local < each;
          if (!visible) return null;
          return (
            <div
              key={i}
              style={{
                position: 'absolute',
                left: 0,
                right: 0,
                top: 0,
                padding: '54px 50px',
                opacity: Math.min(p, out),
                transform: `translateY(${(1 - p) * 110}px) rotate(${family === 'students' ? (1 - p) * 3 : 0}deg)`,
                ...panelStyle(v, family),
              }}
            >
              <div style={{...body(v, 70, 700), lineHeight: 1.18}}>{text}</div>
              <div style={{display: 'flex', gap: 14, marginTop: 40}}>
                {[0, 1, 2].map((d) => (
                  <span
                    key={d}
                    style={{
                      width: 22,
                      height: 22,
                      borderRadius: family === 'career' ? 11 : 0,
                      background: d === i ? v.accent : 'transparent',
                      border: `4px solid ${d === i ? v.accent : v['rule-strong']}`,
                    }}
                  />
                ))}
              </div>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

/** The phone: scan page first, then picking a day and time. 270 frames. */
const PhoneScene: React.FC<{a: Audience; v: Vars; family: Family}> = ({a, v, family}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const rise = spring({frame: f, fps, config: {damping: 16, stiffness: 110}});
  const SWITCH = 140; // frame where the screen changes to picking a time
  const toPick = interpolate(f, [SWITCH, SWITCH + 10], [0, 1], clamp);
  const tap = interpolate(f, [96, 104, 122], [0, 1, 0], clamp); // tap on "I'm not home yet"
  const caption1 = 'Scan the code under yours. The checklist opens with your problem at the top.';
  const caption2 = `${SHARED.pickLead} ${SHARED.remind}`;
  const btn = (primary: boolean): React.CSSProperties => ({
    fontFamily: UI,
    fontWeight: 800,
    fontSize: 42,
    lineHeight: 1.15,
    padding: '32px 30px',
    marginTop: 22,
    borderRadius: family === 'career' ? 22 : family === 'military' ? 4 : 0,
    border: family === 'career' ? 'none' : `4px solid ${family === 'students' ? v.ink : v.dark}`,
    background: primary ? v.accent : v['accent-soft'],
    color: primary ? v['on-accent'] : v.ink,
    boxShadow: family === 'students' ? `6px 6px 0 ${v.ink}` : undefined,
  });
  return (
    <AbsoluteFill style={{padding: `${SAFE.top - 30}px ${SAFE.side}px ${SAFE.bottom}px`, alignItems: 'center', gap: 34}}>
      <div style={{...body(v, 46, 800), textAlign: 'center', width: '100%', minHeight: 170, position: 'relative', textWrap: 'balance'}}>
        <div style={{position: 'absolute', inset: 0, opacity: 1 - toPick}}>{caption1}</div>
        <div style={{position: 'absolute', inset: 0, opacity: toPick}}>{caption2}</div>
      </div>
      <div
        style={{
          width: 800,
          height: 1070,
          borderRadius: 78,
          background: '#0B0D10', // theme-ok: phone bezel, not a site color
          padding: 20,
          transform: `translateY(${(1 - rise) * 500}px)`,
          boxShadow: '0 40px 90px rgba(0,0,0,.35)',
        }}
      >
        <div style={{width: '100%', height: '100%', borderRadius: 60, overflow: 'hidden', background: v.paper, position: 'relative'}}>
          {/* screen 1: the scan page */}
          <div style={{position: 'absolute', inset: 0, padding: '64px 48px', opacity: 1 - toPick}}>
            <div style={{fontFamily: UI, fontWeight: 700, fontSize: 30, letterSpacing: 2, textTransform: 'uppercase', color: v.muted}}>
              {SHARED.scanLabel}
            </div>
            <div style={{...body(v, 52, 800), marginTop: 18, lineHeight: 1.16}}>{a.scanHeading}</div>
            <div style={{...btn(true), marginTop: 50}}>{SHARED.home}</div>
            <div style={{position: 'relative'}}>
              <div style={{...btn(false), transform: `scale(${1 - tap * 0.04})`, outline: tap ? `6px solid ${v.accent}` : 'none', outlineOffset: 6}}>
                {SHARED.away}
              </div>
              <div
                style={{
                  position: 'absolute',
                  right: 70,
                  top: '50%',
                  marginTop: -50,
                  width: 100,
                  height: 100,
                  borderRadius: '50%',
                  border: `8px solid ${v.accent}`,
                  opacity: tap,
                  transform: `scale(${0.6 + tap * 0.9})`,
                }}
              />
            </div>
          </div>
          {/* screen 2: pick a day and time */}
          <div style={{position: 'absolute', inset: 0, padding: '48px 48px', opacity: toPick}}>
            <div style={{...body(v, 50, 800), lineHeight: 1.16}}>{`When will you ${a.task}?`}</div>
            <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16, marginTop: 34}}>
              {[['Tonight', '7:00 p.m.'], ['Tomorrow', '7:00 p.m.'], ['Saturday', '10:00 a.m.'], ['Monday', '7:00 p.m.']].map(([day, at], i) => {
                const on = i === 2 && f > SWITCH + 40;
                return (
                  <div
                    key={day}
                    style={{
                      ...body(v, 34, 800),
                      padding: '20px 20px',
                      borderRadius: family === 'career' ? 18 : 0,
                      border: `4px solid ${on ? v.accent : v['rule-strong']}`,
                      background: on ? v['accent-soft'] : v.surface,
                    }}
                  >
                    {day}
                    <div style={{fontWeight: 600, fontSize: 30, color: v.muted, marginTop: 4}}>{at}</div>
                  </div>
                );
              })}
            </div>
            {(() => {
              const p = spring({frame: f - (SWITCH + 62), fps, config: {damping: 13, stiffness: 150}});
              return (
                <div style={{marginTop: 34, opacity: p, transform: `translateY(${(1 - p) * 60}px) scale(${0.9 + p * 0.1})`}}>
                  <div
                    style={{
                      padding: '34px 30px',
                      background: family === 'career' ? v.accent : v.tape || v.accent,
                      color: family === 'career' ? v['on-accent'] : v.ink,
                      borderRadius: family === 'career' ? 28 : 0,
                      border: family === 'career' ? 'none' : `5px solid ${family === 'students' ? v.ink : v.dark}`,
                      boxShadow: family === 'students' ? `8px 8px 0 ${v.ink}` : undefined,
                    }}
                  >
                    <div style={{fontFamily: DISPLAY[family], fontWeight: family === 'career' ? 800 : 400, fontSize: family === 'military' ? 44 : family === 'career' ? 52 : 58, whiteSpace: 'nowrap', textTransform: CAPS[family] ? 'uppercase' : 'none', lineHeight: 1}}>
                      {SHARED.when}
                    </div>
                    <div style={{...body(v, 34, 700), marginTop: 12, color: 'inherit'}}>{`You’ll ${a.task}.`}</div>
                  </div>
                  <div style={{...btn(true), marginTop: 22}}>{SHARED.addCal}</div>
                </div>
              );
            })()}
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

const Finish: React.FC<{a: Audience; v: Vars; family: Family}> = ({a, v, family}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const lines = [SHARED.offer, SHARED.noApp, SHARED.noEmail];
  const urlP = spring({frame: f - 52, fps, config: {damping: 12, stiffness: 150}});
  return (
    <AbsoluteFill style={{padding: `${SAFE.top}px ${SAFE.side}px ${SAFE.bottom}px`, justifyContent: 'center', gap: 34}}>
      <div>
        <Tag v={v} family={family}>Mr. Life Manager</Tag>
      </div>
      {lines.map((l, i) => {
        const p = spring({frame: f - 4 - i * 14, fps, config: {damping: 14, stiffness: 150}});
        return (
          <div key={l} style={{...headline(v, family, 108), opacity: p, transform: `translateX(${(1 - p) * -80}px)`}}>
            {l}
          </div>
        );
      })}
      <div
        style={{
          marginTop: 30,
          alignSelf: 'flex-start',
          opacity: urlP,
          transform: `scale(${0.85 + urlP * 0.15})`,
          background: v.accent,
          color: v['on-accent'],
          fontFamily: UI,
          fontWeight: 800,
          fontSize: 58,
          padding: '28px 40px',
          borderRadius: family === 'career' ? 28 : family === 'military' ? 4 : 0,
          border: family === 'career' ? 'none' : `5px solid ${family === 'students' ? v.ink : v.dark}`,
          boxShadow: family === 'students' ? `10px 10px 0 ${v.ink}` : undefined,
        }}
      >
        {a.url}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- the video ---------- */
export const Promo: React.FC<PromoProps> = ({audience}) => {
  useFonts();
  const {v, family} = getLook(audience.look);
  const scenes: {from: number; dur: number; node: React.ReactNode}[] = [
    {from: 0, dur: 100, node: <Hook a={audience} v={v} family={family} />},
    {from: 100, dur: 300, node: <Problems a={audience} v={v} family={family} />},
    {from: 400, dur: 280, node: <PhoneScene a={audience} v={v} family={family} />},
    {from: 680, dur: 120, node: <Finish a={audience} v={v} family={family} />},
  ];
  return (
    <AbsoluteFill>
      <Background v={v} family={family} />
      {scenes.map((s, i) => (
        <Sequence key={i} from={s.from} durationInFrames={s.dur}>
          <Fade duration={s.dur} outFrames={i === scenes.length - 1 ? 0 : 8}>{s.node}</Fade>
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};

void Easing;
