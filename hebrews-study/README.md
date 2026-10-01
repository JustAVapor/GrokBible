# Hebrews: A Verse-by-Verse Study from the Original Languages

Source files for `../Hebrews - A Verse-by-Verse Study.epub`.

- `chapters/` — XHTML fragments: front matter, one or more files per section of each chapter (`cNN_s*.html`), appendices, bibliography.
- `STYLE_GUIDE.md` — translation conventions, markup, and integrity rules the study follows.
- `sources/` — SBL Greek New Testament text of Hebrews (with MorphGNT morphology).
- `tools/wlc.py` — prints the Masoretic Hebrew (Westminster Leningrad Codex, via Open Scriptures) of an OT passage.
- `tools/check.py`, `tools/verify_book.py`, `tools/compare_translations.py` — validation helpers.
- `tools/build.py` — builds the EPUB (requires `fonttools`): `python3 hebrews-study/tools/build.py`
- `cover/` — cover artwork (SVG source and rendered JPEG).
