#!/usr/bin/env python3
"""Long-form Lobster TTS: paragraph-aware segmented synthesis + silence.

Canonical text is never rewritten. This wrapper only controls synthesis boundaries.
Baseline restored from the proven Lobster SOP: 240-420 chars/segment, 350 ms between segments.
Requires ffmpeg for concatenation.
"""
import argparse, os, re, subprocess, tempfile
from xfyun_super_official_run import load_profile, run_once

SENTENCE = re.compile(r'(?<=[。！？!?])')

def split_text(text, target_min=240, target_max=420):
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n+', text.strip()) if p.strip()]
    out = []
    for p in paragraphs:
        if len(p) <= target_max:
            out.append(p); continue
        sentences = [s.strip() for s in SENTENCE.split(p) if s.strip()]
        buf = ''
        for s in sentences:
            if buf and len(buf) + len(s) > target_max:
                out.append(buf); buf = s
            else:
                buf += s
        if buf: out.append(buf)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--text-file', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--profile', default='default')
    ap.add_argument('--pause-ms', type=int, default=350)
    ap.add_argument('--min-chars', type=int, default=240)
    ap.add_argument('--max-chars', type=int, default=420)
    ap.add_argument('--url', default='wss://cbm01.cn-huabei-1.xf-yun.com/v1/private/mcd9m97e6')
    args = ap.parse_args()
    for key in ('XFYUN_APPID','XFYUN_API_KEY','XFYUN_API_SECRET'):
        if not os.environ.get(key): raise RuntimeError(f'Missing {key}')
    with open(args.text_file, encoding='utf-8') as f: text=f.read().strip()
    segs=split_text(text,args.min_chars,args.max_chars)
    if not segs: raise RuntimeError('No text to synthesize')
    p=load_profile(args.profile)
    voice=p.get('voice','x6_lingyuyan_pro'); speed=p.get('speed',50); volume=p.get('volume',52); pitch=p.get('pitch',50)
    with tempfile.TemporaryDirectory() as d:
        parts=[]
        # Hard preflight: synthesize the first segment before the batch.
        first=os.path.join(d,'000.mp3'); run_once(args.url,first,voice,segs[0],speed,volume,pitch); parts.append(first)
        for i,s in enumerate(segs[1:],1):
            path=os.path.join(d,f'{i:03d}.mp3'); run_once(args.url,path,voice,s,speed,volume,pitch); parts.append(path)
        silence=os.path.join(d,'silence.mp3')
        subprocess.run(['ffmpeg','-y','-f','lavfi','-i','anullsrc=r=24000:cl=mono','-t',str(args.pause_ms/1000),'-q:a','9',silence],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        concat=os.path.join(d,'concat.txt')
        with open(concat,'w') as f:
            for i,path in enumerate(parts):
                f.write(f"file '{path}'\n")
                if i < len(parts)-1: f.write(f"file '{silence}'\n")
        subprocess.run(['ffmpeg','-y','-f','concat','-safe','0','-i',concat,'-c:a','libmp3lame','-ar','24000','-ac','1',args.out],check=True)
    print(f'OK: {args.out} | segments={len(segs)} pause={args.pause_ms}ms profile={args.profile}')
if __name__=='__main__': main()
