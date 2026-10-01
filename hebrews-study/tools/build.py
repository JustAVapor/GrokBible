#!/usr/bin/env python3
"""Build the Hebrews study EPUB from the XHTML fragments in ../chapters.

Usage: python3 tools/build.py [output.epub]
"""
import os, re, sys, glob, uuid, zipfile, datetime, html, subprocess, tempfile
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, 'chapters')
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(ROOT), 'Hebrews - A Verse-by-Verse Study.epub')
XHTML_NS = 'http://www.w3.org/1999/xhtml'
TITLE = 'Hebrews'
SUBTITLE = 'A Verse-by-Verse Study from the Original Languages'
AUTHOR = 'Claude'
BOOK_ID = 'urn:uuid:' + str(uuid.uuid5(uuid.NAMESPACE_URL, 'grokbible/hebrews-verse-by-verse-study'))
MODIFIED = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')


def read(p):
    with open(p, encoding='utf8') as f:
        return f.read()


def text_of(el):
    return re.sub(r'\s+', ' ', ''.join(el.itertext())).strip()


def page(title, body, body_class=None):
    cls = f' class="{body_class}"' if body_class else ''
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en" lang="en">
<head>
<meta charset="utf-8"/>
<title>{html.escape(title)}</title>
<link rel="stylesheet" type="text/css" href="../styles/style.css"/>
</head>
<body{cls}>
{body}
</body>
</html>
'''


# ---------------------------------------------------------------- documents
def chapter_groups():
    """Return ordered list of (doc_id, [fragment files])."""
    groups = []
    for f in sorted(glob.glob(os.path.join(CH, 'front_*.html'))):
        groups.append((os.path.basename(f)[:-5], [f]))
    for c in range(1, 14):
        files = sorted(glob.glob(os.path.join(CH, f'c{c:02d}_s*.html')))
        if files:
            groups.append((f'hebrews{c:02d}', files))
    for f in sorted(glob.glob(os.path.join(CH, 'app_*.html'))):
        groups.append((os.path.basename(f)[:-5], [f]))
    for f in sorted(glob.glob(os.path.join(CH, 'zz_*.html'))):
        groups.append((os.path.basename(f)[:-5], [f]))
    return groups


def main():
    groups = chapter_groups()
    docs = []      # (id, filename, title, xhtml)
    toc = []       # (title, href, [(subtitle, href)])
    all_text = []
    errors = 0
    for doc_id, files in groups:
        body = '\n'.join(read(f) for f in files)
        try:
            root = ET.fromstring(f'<div xmlns="{XHTML_NS}">' + body + '</div>')
        except ET.ParseError as e:
            print(f'XML error in {doc_id} ({[os.path.basename(x) for x in files]}): {e}')
            if not os.environ.get('SKIP_BAD'):
                errors += 1
            continue
        fname = f'{doc_id}.xhtml'
        h1 = root.find(f'.//{{{XHTML_NS}}}h1')
        h1_title = text_of(h1) if h1 is not None else doc_id
        sub = None
        for p in root.iter(f'{{{XHTML_NS}}}p'):
            if p.get('class') == 'chapter-title':
                sub = text_of(p)
                break
        nav_title = f'{h1_title}: {sub}' if sub and doc_id.startswith(('hebrews', 'app_')) else h1_title
        h1_id = h1.get('id') if h1 is not None else None
        secs = []
        for h2 in root.iter(f'{{{XHTML_NS}}}h2'):
            if h2.get('id'):
                secs.append((text_of(h2), f'{fname}#{h2.get("id")}'))
        toc.append((nav_title, fname + (f'#{h1_id}' if h1_id else ''), secs))
        docs.append((doc_id, fname, nav_title, page(nav_title, body)))
        all_text.append(body)
    if errors:
        sys.exit('Build aborted: fix XML errors above.')

    # ------------------------------------------------ front pages
    title_body = f'''<div class="titlepage">
<p class="tp-greek"><span class="gk" lang="grc">ΠΡΟΣ ΕΒΡΑΙΟΥΣ</span></p>
<p class="tp-title">HEBREWS</p>
<p class="tp-orn">◆</p>
<p class="tp-sub">{SUBTITLE}</p>
<p>Translation, exposition, and historical background,<br/>verse by verse</p>
<p class="tp-author">Prepared by {AUTHOR}</p>
</div>'''
    epigraph_body = '''<div class="epigraph">
<p>“In many portions and in many ways God spoke long ago to the fathers by the prophets; in these last days he has spoken to us in a Son.”</p>
<p>Hebrews 1:1–2</p>
<p>◆</p>
<p>“Jesus Christ is the same yesterday and today and forever.”</p>
<p>Hebrews 13:8</p>
</div>'''
    year = datetime.date.today().year
    copyright_body = f'''<div class="copyright">
<p><strong>{TITLE}: {SUBTITLE}</strong></p>
<p>Prepared by {AUTHOR}, an AI model made by Anthropic, {year}. As with any study, readers are encouraged to test everything by the Scriptures themselves (Acts 17:11).</p>
<p>All quotations of Scripture are original translations made for this study from the Greek and Hebrew texts. They are not drawn from any published English version.</p>
<p>The Greek text of Hebrews is that of <cite>The Greek New Testament: SBL Edition</cite>, copyright © 2010 by the Society of Biblical Literature and Logos Bible Software, used under the Creative Commons Attribution 4.0 license; morphological data from the MorphGNT project. The Hebrew text of the Old Testament is the Westminster Leningrad Codex (public domain), with data from the Open Scriptures Hebrew Bible project (CC BY 4.0).</p>
<p>Embedded fonts: Gentium Plus (SIL International), Noto Serif Hebrew (Google), and Cinzel (Natanael Gama), all used under the SIL Open Font License.</p>
<p>Cover: an anchor before the parted curtain of the sanctuary, after Hebrews 6:19–20 and 10:19–20.</p>
</div>'''

    contents_items = []
    for title, href, secs in toc:
        inner = ''
        if secs:
            inner = '<ol>' + ''.join(f'<li class="sec"><a href="{h}">{html.escape(t)}</a></li>' for t, h in secs) + '</ol>'
        contents_items.append(f'<li class="ch"><a href="{href}">{html.escape(title)}</a>{inner}</li>')
    contents_body = '<h1 class="chapter" id="contents">Contents</h1>\n<div class="contents"><ol>' + '\n'.join(contents_items) + '</ol></div>'

    front = [
        ('cover', 'cover.xhtml', 'Cover', page('Cover', '<div style="text-align:center;margin:0;padding:0"><img class="cover" src="../images/cover.jpg" alt="Hebrews: A Verse-by-Verse Study from the Original Languages"/></div>', 'cover')),
        ('titlepage', 'titlepage.xhtml', 'Title Page', page('Title Page', title_body)),
        ('copyright', 'copyright.xhtml', 'Copyright', page('Copyright', copyright_body)),
        ('epigraph', 'epigraph.xhtml', 'Epigraph', page('Epigraph', epigraph_body)),
        ('contents', 'contents.xhtml', 'Contents', page('Contents', contents_body)),
    ]
    all_docs = front + docs

    # ------------------------------------------------ nav + ncx
    nav_items = []
    for title, href, secs in toc:
        inner = ''
        if secs:
            inner = '<ol>' + ''.join(f'<li><a href="text/{h}">{html.escape(t)}</a></li>' for t, h in secs) + '</ol>'
        nav_items.append(f'<li><a href="text/{href}">{html.escape(title)}</a>{inner}</li>')
    first_ch = next(h for t, h, s in toc if h.startswith('hebrews01'))
    nav = f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en" lang="en">
<head><meta charset="utf-8"/><title>Contents</title><link rel="stylesheet" type="text/css" href="styles/style.css"/></head>
<body>
<nav epub:type="toc" id="toc"><h1>Contents</h1>
<ol>
<li><a href="text/titlepage.xhtml">Title Page</a></li>
<li><a href="text/contents.xhtml">Contents</a></li>
{chr(10).join(nav_items)}
</ol></nav>
<nav epub:type="landmarks" id="landmarks" hidden="hidden"><h2>Landmarks</h2>
<ol>
<li><a epub:type="cover" href="text/cover.xhtml">Cover</a></li>
<li><a epub:type="toc" href="text/contents.xhtml">Contents</a></li>
<li><a epub:type="bodymatter" href="text/{first_ch}">Hebrews 1</a></li>
</ol></nav>
</body></html>
'''
    np = [0]

    def navpoint(title, src, children=''):
        np[0] += 1
        return f'<navPoint id="np{np[0]}" playOrder="{np[0]}"><navLabel><text>{html.escape(title)}</text></navLabel><content src="text/{src}"/>{children}</navPoint>'
    ncx_points = [navpoint('Title Page', 'titlepage.xhtml'), navpoint('Contents', 'contents.xhtml')]
    for title, href, secs in toc:
        # parent must be assigned its playOrder before its children
        np[0] += 1
        me = np[0]
        kids = ''.join(navpoint(t, h) for t, h in secs)
        ncx_points.append(f'<navPoint id="np{me}" playOrder="{me}"><navLabel><text>{html.escape(title)}</text></navLabel><content src="text/{href}"/>{kids}</navPoint>')
    ncx = f'''<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="{BOOK_ID}"/><meta name="dtb:depth" content="2"/><meta name="dtb:totalPageCount" content="0"/><meta name="dtb:maxPageNumber" content="0"/></head>
<docTitle><text>{TITLE}: {SUBTITLE}</text></docTitle>
<navMap>{''.join(ncx_points)}</navMap>
</ncx>
'''

    # ------------------------------------------------ fonts (subset to the characters used)
    from fontTools import subset as ftsubset
    text = '\n'.join(all_text) + title_body
    greek_chars = ''.join(sorted({ch for ch in text if 'Ͱ' <= ch <= 'Ͽ' or 'ἀ' <= ch <= '῿'})) + 'ΠΡΟΣΕΒΑΙΥ ’᾽·;,.'
    hebrew_chars = ''.join(sorted({ch for ch in text if '֐' <= ch <= '׿' or 'יִ' <= ch <= 'ﭏ'})) + ' '
    display_chars = ''.join(sorted(set(''.join(t for t, h, s in toc) + 'HEBREWSAPPENDIXCONTENTS0123456789 :–'))) + ''.join(chr(c) for c in range(32, 127))
    fdir = os.path.join(ROOT, 'fonts')
    tmp = tempfile.mkdtemp()
    fonts = {}
    for name, src, chars in [('greek', 'GentiumPlus-Regular.ttf', greek_chars),
                             ('hebrew', 'NSHeb-R.ttf', hebrew_chars),
                             ('display', 'CinzelSB.ttf', display_chars)]:
        out = os.path.join(tmp, name + '.ttf')
        opts = ftsubset.Options()
        opts.layout_features = ['*']
        opts.name_IDs = ['*']
        opts.notdef_outline = True
        f = ftsubset.load_font(os.path.join(fdir, src), opts)
        s = ftsubset.Subsetter(opts)
        s.populate(text=chars)
        s.subset(f)
        ftsubset.save_font(f, out, opts)
        fonts[name] = read_bin(out)

    # ------------------------------------------------ OPF
    manifest = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
        '<item id="css" href="styles/style.css" media-type="text/css"/>',
        '<item id="cover-img" href="images/cover.jpg" media-type="image/jpeg" properties="cover-image"/>',
    ] + [f'<item id="font-{n}" href="fonts/{n}.ttf" media-type="font/ttf"/>' for n in fonts]
    spine = []
    for did, fname, title, x in all_docs:
        manifest.append(f'<item id="d-{did}" href="text/{fname}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="d-{did}"/>')
    opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="en">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="bookid">{BOOK_ID}</dc:identifier>
<dc:title id="t1">{TITLE}: {SUBTITLE}</dc:title>
<dc:creator id="c1">{AUTHOR}</dc:creator>
<dc:language>en</dc:language>
<dc:subject>Bible. Hebrews -- Commentaries</dc:subject>
<dc:description>An in-depth, verse-by-verse study of the Epistle to the Hebrews, with fresh translation from the Greek, attention to the Hebrew and Greek Old Testament, historical and cultural background, and the insights of the church's great commentators tested by Scripture.</dc:description>
<dc:date>{datetime.date.today().isoformat()}</dc:date>
<meta property="dcterms:modified">{MODIFIED}</meta>
<meta name="cover" content="cover-img"/>
</metadata>
<manifest>
{chr(10).join(manifest)}
</manifest>
<spine toc="ncx">
{chr(10).join(spine)}
</spine>
<guide>
<reference type="cover" title="Cover" href="text/cover.xhtml"/>
<reference type="toc" title="Contents" href="text/contents.xhtml"/>
<reference type="text" title="Hebrews 1" href="text/{first_ch.split('#')[0]}"/>
</guide>
</package>
'''
    container = '''<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>
'''
    # ------------------------------------------------ zip
    if os.path.exists(OUT):
        os.remove(OUT)
    with zipfile.ZipFile(OUT, 'w') as z:
        z.writestr(zipfile.ZipInfo('mimetype'), 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
        def w(name, data):
            z.writestr(name, data, compress_type=zipfile.ZIP_DEFLATED)
        w('META-INF/container.xml', container)
        w('OEBPS/content.opf', opf)
        w('OEBPS/nav.xhtml', nav)
        w('OEBPS/toc.ncx', ncx)
        w('OEBPS/styles/style.css', read(os.path.join(ROOT, 'tools', 'style.css')))
        w('OEBPS/images/cover.jpg', read_bin(os.path.join(ROOT, 'cover', 'cover.jpg')))
        for n, data in fonts.items():
            w(f'OEBPS/fonts/{n}.ttf', data)
        for did, fname, title, x in all_docs:
            w(f'OEBPS/text/{fname}', x)
    words = len(re.sub(r'<[^>]+>', ' ', '\n'.join(all_text)).split())
    print(f'Wrote {OUT}  ({os.path.getsize(OUT)//1024} KB, {len(all_docs)} documents, ~{words:,} words)')


def read_bin(p):
    with open(p, 'rb') as f:
        return f.read()


if __name__ == '__main__':
    main()
