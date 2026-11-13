import React, {useEffect, useState} from 'react';
import {AbsoluteFill, Img, Sequence, continueRender, delayRender, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {ActionCut, ActionKind} from './action-copy';
import {UI, Vars, getLook} from './look';

const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;

const useFont = () => {
  const [handle] = useState(() => delayRender('action-font'));
  useEffect(() => {
    const font = new FontFace('Archivo', `url(${staticFile('fonts/archivo.woff2')})`, {weight: '400 800'});
    font.load().then((f) => document.fonts.add(f)).finally(() => continueRender(handle));
  }, [handle]);
};

/** Stylized animated illustration: the same ordinary space before and after. */
const Room: React.FC<{kind: ActionKind; progress: number; v: Vars}> = ({kind, progress: p, v}) => {
  const clutter = 1 - p;
  const common = {stroke: v.ink, strokeWidth: 4, strokeLinejoin: 'round' as const};
  return (
    <svg viewBox="0 0 900 490" width="100%" height="100%" aria-label="Illustrated household task result">
      <rect x="5" y="5" width="890" height="480" rx="36" fill={v['accent-soft']} />
      <path d="M40 390H860" stroke={v['rule-strong']} strokeWidth="3" />
      <rect x="74" y="55" width="154" height="167" rx="8" fill={v.surface} {...common}/>
      <path d="M151 57V221M76 140H226" stroke={v['rule-strong']} strokeWidth="3"/>
      <path d="M92 198L138 148L173 179L207 122" fill="none" stroke={v.accent} strokeWidth="4" />
      {kind === 'table' ? <>
        <path d="M183 264L234 417M675 264L629 417" stroke={v.ink} strokeWidth="18" strokeLinecap="round"/>
        <rect x="135" y="235" width="610" height="58" rx="20" fill={v.second} {...common}/>
        <rect x="102" y="302" width="128" height="24" rx="8" fill={v.accent} {...common}/>
        <path d="M121 326V423M213 326V423M111 301V228" fill="none" stroke={v.ink} strokeWidth="9"/>
        <rect x="662" y="302" width="128" height="24" rx="8" fill={v.accent} {...common}/>
        <path d="M680 326V423M772 326V423M782 301V228" fill="none" stroke={v.ink} strokeWidth="9"/>
        <g opacity={p}>
          <ellipse cx="346" cy="236" rx="72" ry="25" fill={v.surface} {...common}/>
          <ellipse cx="535" cy="236" rx="72" ry="25" fill={v.surface} {...common}/>
          <path d="M321 234Q346 197 371 234" fill={v.second} stroke={v.ink} strokeWidth="3"/>
          <path d="M510 234Q535 197 560 234" fill={v.accent} stroke={v.ink} strokeWidth="3"/>
          <rect x="263" y="187" width="27" height="45" rx="4" fill={v['second-soft']} {...common}/>
          <rect x="612" y="187" width="27" height="45" rx="4" fill={v['second-soft']} {...common}/>
          <rect x="759" y="363" width="100" height="63" rx="10" fill={v['second-soft']} {...common}/>
          <path d="M765 382H851M765 401H851" stroke={v['rule-strong']} strokeWidth="4"/>
        </g>
        <g opacity={clutter} transform={`translate(0 ${-p * 80})`}>
          <rect x="242" y="152" width="110" height="76" rx="3" fill={v['second-soft']} {...common}/>
          <path d="M242 172H352M297 153V228" stroke={v.ink} strokeWidth="3"/>
          <rect x="386" y="185" width="130" height="34" rx="5" fill={v.accent} {...common}/>
          <rect x="405" y="157" width="130" height="30" rx="5" fill={v.surface} {...common}/>
          <path d="M562 198L606 150L651 170L627 219Z" fill={v['second-soft']} {...common}/>
          <path d="M145 273L194 255L213 307L166 314Z" fill={v['second-soft']} {...common}/>
        </g>
      </> : kind === 'first-night' ? <>
        <path d="M256 281L650 281L724 403H211Z" fill={v.surface} {...common}/>
        <rect x="242" y="193" width="424" height="100" rx="18" fill={v.accent} {...common}/>
        <path d="M211 403H724V427H211Z" fill={v.second} {...common}/>
        <g opacity={p}>
          <path d="M260 278H653L698 384H233Z" fill={v['accent-soft']} {...common}/>
          <rect x="285" y="252" width="136" height="48" rx="16" fill={v.surface} {...common}/>
          <rect x="459" y="252" width="136" height="48" rx="16" fill={v.surface} {...common}/>
          <path d="M238 370H694" stroke={v.accent} strokeWidth="12"/>
          <rect x="739" y="214" width="66" height="60" rx="6" fill={v.surface} {...common}/>
          <rect x="750" y="180" width="18" height="34" rx="4" fill={v.second} {...common}/>
          <path d="M773 194H793V212H773Z" fill={v.accent}/>
        </g>
        <g opacity={clutter} transform={`translate(${-p * 80} 0)`}>
          <path d="M280 294L364 271L474 335L628 295L682 377H246Z" fill={v['second-soft']} {...common}/>
          <rect x="610" y="302" width="103" height="84" fill={v['second-soft']} {...common}/>
          <path d="M610 324H713M661 302V386" stroke={v.ink} strokeWidth="3"/>
        </g>
        <rect x="62" y="318" width="106" height="101" fill={v['second-soft']} {...common}/>
        <path d="M62 339H168M115 318V419" stroke={v.ink} strokeWidth="3"/>
      </> : <>
        <rect x="226" y="240" width="406" height="132" rx="30" fill={v.accent} {...common}/>
        <rect x="253" y="210" width="161" height="125" rx="24" fill={v['accent-deep']} {...common}/>
        <rect x="433" y="210" width="171" height="125" rx="24" fill={v['accent-deep']} {...common}/>
        <rect x="196" y="283" width="65" height="101" rx="17" fill={v.accent} {...common}/>
        <rect x="606" y="283" width="65" height="101" rx="17" fill={v.accent} {...common}/>
        <path d="M251 384V410M615 384V410" stroke={v.ink} strokeWidth="12"/>
        <rect x="680" y="340" width="127" height="19" rx="8" fill={v.second} {...common}/>
        <path d="M700 359V409M788 359V409" stroke={v.ink} strokeWidth="8"/>
        <path d="M758 339V166M710 412H805" stroke={v.ink} strokeWidth="7"/>
        <path d="M716 174L736 108H780L806 174Z" fill={v.second} {...common}/>
        <g opacity={p}>
          <path d="M718 181L680 283H837L795 181" fill={v['second-soft']} opacity=".7"/>
          <rect x="284" y="250" width="92" height="77" rx="12" fill={v['second-soft']} {...common}/>
          <rect x="470" y="250" width="92" height="77" rx="12" fill={v.surface} {...common}/>
        </g>
        <g opacity={clutter} transform={`translate(0 ${-p * 70})`}>
          <path d="M281 303L320 250L370 276L401 327L372 345L339 311L312 348Z" fill={v['second-soft']} {...common}/>
          <rect x="458" y="270" width="112" height="82" rx="3" fill={v['second-soft']} {...common}/>
          <path d="M458 290H570M514 270V352" stroke={v.ink} strokeWidth="3"/>
          <path d="M355 390L410 360L450 404L399 417Z" fill={v.surface} {...common}/>
        </g>
      </>}
    </svg>
  );
};

type Stage = 'hook' | 'result' | 'proof' | 'plan' | 'close';
const Scene: React.FC<{cut: ActionCut; stage: Stage; v: Vars}> = ({cut, stage, v}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const p = stage === 'hook' ? 0 : interpolate(f, [0, 0.9 * fps], [0, 1], clamp);
  const title = {hook: cut.hook, result: cut.result, proof: cut.proof,
    plan: "Do it when\nyou're home.", close: cut.close}[stage];
  return <AbsoluteFill style={{padding: '230px 100px 430px 72px'}}>
    <div style={{fontSize: 29, fontWeight: 800, letterSpacing: 3, color: v.accent}}>MR. LIFE MANAGER</div>
    <div data-video-text="headline" style={{fontSize: stage === 'hook' ? 90 : 98, fontWeight: 800, lineHeight: 1.07,
      letterSpacing: -3, whiteSpace: 'pre-line', marginTop: 36, minHeight: 310}}>{title}</div>
    {stage === 'proof' ? <div style={{marginTop: 0}}>
      <div style={{fontSize: 30, fontWeight: 700, color: v.accent, marginBottom: 20}}>INSIDE THE FREE CHECKLIST</div>
      <div style={{border: `3px solid ${v['rule-strong']}`, borderRadius: 24, background: v.surface, padding: 24,
        height: 480, overflow: 'hidden'}}>
        <Img src={staticFile(`tasks/${cut.screenshot}`)} style={{width: '100%', display: 'block'}}/>
      </div>
      <div style={{fontSize: 32, marginTop: 20, color: v.muted}}>One step at a time on your phone.</div>
    </div> : <div style={{height: 470, margin: '4px -5px 0'}}><Room kind={cut.kind} progress={stage === 'result' ? p : stage === 'hook' ? 0 : 1} v={v}/></div>}
    {stage === 'hook' && <div data-video-text="support" style={{fontSize: 42, fontWeight: 700, lineHeight: 1.2, marginTop: 28}}>Open the free checklist at the profile link.</div>}
    {stage === 'result' && <div data-video-text="support" style={{fontSize: 42, fontWeight: 700, lineHeight: 1.2, marginTop: 28}}>
      {cut.kind === 'company' ? 'Clear seats. Clean bathroom. Empty sink.' : cut.kind === 'table' ? 'Clear the seats. Wipe the table. Sit down.' : 'Document the condition. Check the essentials.'}
    </div>}
    {stage === 'plan' && <div data-video-text="choices" style={{fontSize: 39, lineHeight: 1.3, marginTop: 24, display: 'grid', gap: 14}}>
      <div style={{color: v.accent, fontWeight: 800}}>{cut.home}</div>
      <div>{cut.away}</div>
    </div>}
    {stage === 'close' && <div data-video-text="cta" style={{marginTop: 24}}>
      <div style={{fontSize: 48, lineHeight: 1.15, fontWeight: 800, color: v.accent}}>Open the free checklist.</div>
      <div style={{fontSize: 35, marginTop: 14}}>Profile link → {cut.kind === 'company' ? 'company checklist' : cut.kind === 'table' ? 'table checklist' : 'first-night checklist'}</div>
      <div style={{fontSize: 30, marginTop: 16, color: v.muted}}>mrlifemanager.com/{cut.route}.html</div>
    </div>}
  </AbsoluteFill>;
};

export const ActionPromo: React.FC<{cut: ActionCut}> = ({cut}) => {
  useFont();
  const {fps} = useVideoConfig();
  const {v} = getLook('career-teal');
  return <AbsoluteFill style={{background: v.paper, color: v.ink, fontFamily: UI}}>
    <div style={{position: 'absolute', left: 0, top: 0, width: 20, height: '100%', background: v.accent}}/>
    <div style={{position: 'absolute', left: 72, right: 100, top: 194, height: 6, background: v.second}}/>
    <Sequence from={0} durationInFrames={3 * fps} premountFor={fps}><Scene cut={cut} stage="hook" v={v}/></Sequence>
    <Sequence from={3 * fps} durationInFrames={4 * fps} premountFor={fps}><Scene cut={cut} stage="result" v={v}/></Sequence>
    <Sequence from={7 * fps} durationInFrames={4 * fps} premountFor={fps}><Scene cut={cut} stage="proof" v={v}/></Sequence>
    <Sequence from={11 * fps} durationInFrames={4 * fps} premountFor={fps}><Scene cut={cut} stage="plan" v={v}/></Sequence>
    <Sequence from={15 * fps} durationInFrames={(cut.seconds - 15) * fps} premountFor={fps}><Scene cut={cut} stage="close" v={v}/></Sequence>
  </AbsoluteFill>;
};
