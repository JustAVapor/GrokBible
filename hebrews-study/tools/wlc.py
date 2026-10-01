#!/usr/bin/env python3
"""Usage: wlc.py Book Chapter Verse[-Verse]   e.g.  wlc.py Ps 2 7   or  wlc.py Jer 31 31-34
Prints the Westminster Leningrad Codex (Masoretic) Hebrew text. Books: Gen Exod Lev Num Deut Josh 2Sam 1Chr Ps Prov Isa Jer Hab Hag Zech Mal"""
import sys,re,os
import xml.etree.ElementTree as ET
d=os.path.dirname(os.path.abspath(__file__))
b,c,vr=sys.argv[1],sys.argv[2],sys.argv[3]
a,_,z=vr.partition('-'); z=z or a
ns='{http://www.bibletechnologies.net/2003/OSIS/namespace}'
fp=f'{d}/wlc/{b}.xml'
if not os.path.exists(fp):  # fetch the Open Scriptures WLC book on first use
    import urllib.request; os.makedirs(f'{d}/wlc',exist_ok=True)
    urllib.request.urlretrieve(f'https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/{b}.xml',fp)
root=ET.parse(fp).getroot()
want={f'{b}.{c}.{v}' for v in range(int(a),int(z)+1)}
for ve in root.iter(ns+'verse'):
    if ve.get('osisID') in want:
        out=''
        for w in ve:
            if w.tag==ns+'w': out+=(w.text or '').replace('/','')+' '
            elif w.tag==ns+'seg':
                t=w.text or ''
                if t=='־': out=out.rstrip()+'־'
                elif t=='׃': out=out.rstrip()+'׃'
        out=re.sub('[\u0591-\u05AF\u05BD\u05C0]','',out)  # strip cantillation marks, keep vowels
        print(ve.get('osisID'), out.strip())
