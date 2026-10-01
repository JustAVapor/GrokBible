#!/usr/bin/env python3
"""Whole-book checks: verse coverage, duplicate ids, integrity heuristics."""
import os,re,glob,collections
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files=sorted(glob.glob(os.path.join(ROOT,'chapters','*.html')))
expected=[]
for l in open(os.path.join(ROOT,'sources','hebrews_sblgnt.txt'),encoding='utf8'):
    c,v=l.split()[0].split(':'); expected.append(f'{c}-{v}')
ids=collections.Counter(); verses=collections.Counter(); per_file={}
for f in files:
    s=open(f,encoding='utf8').read()
    for i in re.findall(r'\bid="([^"]+)"',s): ids[i]+=1
    vs=re.findall(r'id="v(\d+-\d+)"',s)
    for v in vs: verses[v]+=1
    per_file[os.path.basename(f)]=len(re.sub(r'<[^>]+>',' ',s).split())
missing=[v for v in expected if v not in verses]
dups=[v for v,n in verses.items() if n>1]
print('missing verses:',missing or 'none')
print('duplicate verse entries:',dups or 'none')
print('duplicate ids:',[i for i,n in ids.items() if n>1] or 'none')
names=r"(Westcott|Delitzsch|Moffatt|Bruce|Hughes|Kistemaker|Lane|Ellingworth|Attridge|Hagner|Guthrie|Koester|Johnson|deSilva|Cockerill|Schreiner|Vos|Harris|Metzger|Spicq|O[’']Brien)"
for f in files:
    s=re.sub(r'<[^>]+>','',open(f,encoding='utf8').read())
    for m in re.finditer(names+r"[^.“]{0,60}?(writes|says|puts it|calls it|remarks|comments|observes|states|notes)[,:]?\s*“",s):
        print('POSSIBLE QUOTE',os.path.basename(f),':',s[m.start():m.start()+160].replace('\n',' '))
    if re.search(r"O[’']Brien",s): print('O’Brien cited in',os.path.basename(f))
tot=0
for c in range(1,14):
    w=sum(n for k,n in per_file.items() if k.startswith(f'c{c:02d}_')); tot+=w
    nv=sum(1 for v in verses if v.startswith(f'{c}-'))
    print(f'ch{c:2d}: {w:7,} words, {nv} verse entries')
print(f'chapters total: {tot:,} words; all files: {sum(per_file.values()):,}')
