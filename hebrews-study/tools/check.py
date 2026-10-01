#!/usr/bin/env python3
"""Validate study fragment files.  Usage: check.py file1.html [file2.html ...]
Checks XML well-formedness, forbidden entities, duplicate ids; reports word count and verse ids."""
import sys,re
import xml.etree.ElementTree as ET
ok=True
for fn in sys.argv[1:]:
    s=open(fn,encoding='utf8').read()
    ents=set(re.findall(r'&([A-Za-z0-9#]+);',s))-{'amp','lt','gt','quot','apos'}
    ents={e for e in ents if not e.startswith('#')}
    if ents: print(f'{fn}: FORBIDDEN named entities {ents} — use literal Unicode characters'); ok=False
    try:
        root=ET.fromstring('<div xmlns="http://www.w3.org/1999/xhtml">'+s+'</div>')
    except ET.ParseError as e:
        print(f'{fn}: XML ERROR {e} (line numbers are relative to the file)'); ok=False; continue
    ids=re.findall(r'\bid="([^"]+)"',s)
    d={i for i in ids if ids.count(i)>1}
    if d: print(f'{fn}: DUPLICATE ids {d}'); ok=False
    text=re.sub(r'<[^>]+>',' ',s)
    verses=re.findall(r'id="v(\d+-\d+)"',s)
    print(f'{fn}: OK  words={len(text.split())}  verse-entries={len(verses)}  [{", ".join(verses)}]')
sys.exit(0 if ok else 1)
