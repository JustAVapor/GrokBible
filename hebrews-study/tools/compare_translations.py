#!/usr/bin/env python3
"""Compare each section's translation block with the per-verse translation lines."""
import re,glob,os,collections
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def clean(x): return re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',x)).strip().strip('“”‘’ ')
for c in range(1,14):
    s=''.join(open(f,encoding='utf8').read() for f in sorted(glob.glob(f'{ROOT}/chapters/c{c:02d}_s*.html')))
    blocks=re.findall(r'<div class="translation">(.*?)</div>',s,re.S)
    tv={}
    for b in blocks:
        segs=re.split(r'<sup class="vn">(\d+)</sup>',b)
        for i in range(1,len(segs),2): tv[int(segs[i])]=clean(segs[i+1])
    for m in re.finditer(rf'id="v{c}-(\d+)".*?<p class="vtext">(.*?)</p>',s,re.S):
        v=int(m.group(1)); a=tv.get(v); b=clean(m.group(2))
        if a is None: print(f'{c}:{v} not in any translation block')
        elif a!=b: print(f'{c}:{v}\n  BLOCK: {a}\n  VTEXT: {b}')
