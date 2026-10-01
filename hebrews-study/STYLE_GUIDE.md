# Style Guide — *Hebrews: A Verse-by-Verse Study from the Original Languages*

This guide governs every chapter file of the study. Read all of it before writing.

## 1. Purpose and reader

The reader wants an **in-depth, verse-by-verse study of Hebrews** grounded in the Bible itself, **prioritizing the original languages** (Greek NT; Hebrew OT; the Greek Septuagint where Hebrews quotes it). The reader **does not read Greek or Hebrew but defers to their authority**. So:

- Every Greek or Hebrew word you cite must be followed by a **transliteration** and an **English gloss**, and any grammatical point (tense, voice, mood, case, participle, word order, article) must be explained in plain English along with **why it matters for meaning**. No unexplained jargon.
- Incorporate **historical and cultural context** where it helps the reader understand the text (Second Temple Judaism, tabernacle/temple ritual, Day of Atonement, priesthood, Melchizedek traditions, Roman social world, persecution, honor and shame, patronage, athletics, education/discipline, inheritance and wills, oaths, anchors, cities, hospitality, prisons, etc.).
- Use **authoritative commentary** to illuminate the text and the **author's intent**, but **Scripture is the judge of every commentary**: never adopt or lean on an interpretation that the Scriptures contradict. (See §6.)
- All Bible quotations — Hebrews and every cross-reference — are **your own translation from the original language**, never copied from a published English version (no ESV/NIV/KJV/NASB wording reproduced as a quotation).

Tone: reverent, clear, warm, exegetically careful, pastorally aware. Write for an intelligent lay reader; depth without pedantry. American spelling.

## 2. Source texts (use these)

- **Greek text of Hebrews** (SBLGNT, which agrees with NA28 in nearly all places):
  `/home/user/GrokBible/hebrews-study/sources/hebrews_sblgnt.txt` — one verse per line (`1:1 Πολυμερῶς ...`).
  Morphology with lemmas: `/home/user/GrokBible/hebrews-study/sources/79-Heb-morphgnt.txt`
  (columns: BBCCVV, part of speech, parsing code, text, word, normalized, lemma).
  **Copy Greek words exactly from this file** (accents and breathings included). Cite lexical forms (lemmas) from the morphology file when giving dictionary forms.
- **Hebrew (Masoretic) text** of OT passages: run
  `python3 /home/user/GrokBible/hebrews-study/tools/wlc.py <Book> <Chapter> <Verse or Range>`
  Books available: Gen Exod Lev Num Deut Josh 2Sam 1Chr Ps Prov Isa Jer Hab Hag Zech Mal.
  **Note: Psalms use Hebrew versification** (superscriptions count as verse 1), so English Ps 40:6 = Hebrew Ps 40:7, English Ps 45:6 = Hebrew 45:7, Ps 95:7 = 95:7 (no superscription), Ps 102:25 = Hebrew 102:26, Ps 22:22 = Hebrew 22:23, Ps 8:4 = Hebrew 8:5, Ps 104:4 = 104:4. Check by reading neighboring verses. Copy Hebrew exactly from the tool output.
- **Septuagint (LXX)**: Hebrews almost always quotes the OT in Greek. Where the LXX differs from the Hebrew in a way that matters (e.g., Ps 40:6 "a body" vs. Hebrew "ears"; Ps 8:5 "angels" vs. Hebrew *elohim*; Deut 32:43; Ps 95:8 "rebellion/testing" vs. Massah/Meribah; Ps 102:25–27; Ps 104:4; Hab 2:3–4; Prov 3:11–12; Gen 47:31 "staff" vs. "bed"; Hag 2:6; Jer 31:31–34 [LXX 38:31–34]), explain the difference, show the Hebrew, translate both, and explain how Hebrews' reading relates to the Hebrew meaning. Quote LXX Greek only when you are certain of the wording; otherwise describe it in English.

## 3. Translation conventions (all quotations are your own translation)

- Translate from the Greek above: essentially literal, yet readable, natural English. Preserve the author's emphases, sentence structure, and key-word repetitions where English allows (these are part of the argument). Explain in the commentary where a more literal rendering would help.
- Divine pronouns lowercase (he, him, his).
- Hebrew YHWH = "the LORD" written as `the <span class="lord">Lord</span>` (renders in small caps). Greek *kyrios* in Hebrews = "Lord" (note when it stands for YHWH).
- **Fixed renderings** for key terms (so the whole book is consistent; you may explain nuances in comments):
  - ἀρχηγός *archēgos* = "pioneer" (2:10; 12:2)
  - τελειόω *teleioō* = "make perfect / bring to perfection"; τέλειος = "mature" (5:14) / "perfect"
  - ὑπόστασις *hypostasis* = "essential being" (1:3), "confidence" (3:14), "assurance" (11:1) — discuss
  - παρρησία *parrēsia* = "boldness"; ὁμολογία *homologia* = "confession"
  - κατάπαυσις *katapausis* = "rest"; σαββατισμός *sabbatismos* = "Sabbath-rest"
  - διαθήκη *diathēkē* = "covenant" (discuss "will" at 9:16–17)
  - ἱλάσκομαι *hilaskomai* (2:17) = "make propitiation for"; ἱλαστήριον (9:5) = "mercy seat" (place of atonement)
  - σκηνή *skēnē* = "tabernacle" (or "tent" when the context is the outer/first tent: "the first tent"); τὰ ἅγια = "the sanctuary" / "the holy places" as context requires; καταπέτασμα = "curtain"
  - ἀρχιερεύς = "high priest"; λειτουργός = "minister"; μεσίτης = "mediator"
  - ἐφάπαξ / ἅπαξ = "once for all" / "once"
  - ὑπομονή = "endurance"; πίστις = "faith"; ἐπαγγελία = "promise"; ἁγιάζω = "sanctify"; συνείδησις = "conscience"
  - πρωτότοκος = "firstborn"; κληρονόμος = "heir"; υἱός for Christ = "Son"
  - ἀπιστία = "unbelief"; ἀπείθεια = "disobedience"; νωθρός = "sluggish"
  - παράκλησις = "exhortation/encouragement" (13:22 "word of exhortation")
- Transliteration (SBL general-purpose style):
  - Greek: η = ē, ω = ō, υ = y (but u in diphthongs: au, eu, ou, ui), rough breathing = h, initial ρ = rh, γγ = ng, γκ = nk, χ = ch, θ = th, φ = ph, ψ = ps, ξ = x. No accents. E.g., ἀπαύγασμα *apaugasma*, ὑπόστασις *hypostasis*.
  - Hebrew: simple general-purpose (no diacritics needed): בְּרִית *berit*, חֶסֶד *chesed*, מְנוּחָה *menuchah*, כִּפֶּר *kipper*, מַלְכִּי־צֶדֶק *Malki-tsedeq*.

## 4. File layout and markup (XHTML fragments)

Write **body-level XHTML fragments only** (no `<html>`, `<head>`, `<body>`). The build wraps them. Write **one file per section** into
`/home/user/GrokBible/hebrews-study/chapters/`, named:

- `cNN_s0.html` — chapter opening (only the agent assigned the chapter opening writes this)
- `cNN_s1.html`, `cNN_s2.html`, … — sections in order (NN = two-digit chapter). A long section may be split across files `cNN_s1a.html`, `cNN_s1b.html`, … (files are concatenated in filename order).

Files are concatenated in sorted filename order to form the chapter, so headings must flow correctly across files.

### Allowed markup

```html
<!-- cNN_s0.html: chapter opening -->
<h1 class="chapter" id="ch1">Hebrews 1</h1>
<p class="chapter-title">God Has Spoken in His Son</p>
<div class="chapter-intro">
  <p>… 400–800 words: where the chapter sits in the argument of Hebrews, its structure, key themes,
     key Greek terms that recur, and what to watch for …</p>
</div>

<!-- cNN_sK.html: a section -->
<h2 class="section" id="sec-1-1">God Has Spoken in His Son <span class="ref">(1:1–4)</span></h2>
<p class="continues">This section continues in chapter 4.</p>   <!-- only where a section crosses a chapter boundary -->

<div class="translation">
  <p class="tr-head">Translation</p>
  <p><sup class="vn">1</sup>In many portions and in many ways … <sup class="vn">2</sup>…</p>
  <blockquote class="oq"><p>“You are my Son; today I have begotten you.”</p></blockquote>  <!-- OT quotations set off -->
  <p>…</p>
</div>

<h3 class="sub">Setting and Structure</h3>
<p>… 400–900 words: literary context, flow of thought, structure (inclusio, chiasm, key-word links),
   historical/cultural setting relevant to the whole section …</p>

<h3 class="sub">Verse by Verse</h3>

<div class="verse" id="v1-1">
  <h4 class="vhead">1:1</h4>
  <p class="vtext">In many portions and in many ways, long ago God spoke to the fathers by the prophets,</p>
  <p>Commentary paragraphs …</p>

  <div class="wordstudy">
    <p class="box-title">Word Study: <span class="gk" lang="grc">πολυμερῶς</span> <i class="tl">polymerōs</i></p>
    <p>…</p>
  </div>

  <div class="background">
    <p class="box-title">Historical Background: The Prophets and the Fathers</p>
    <p>…</p>
  </div>

  <div class="ot">
    <p class="box-title">Old Testament Text: Psalm 2:7</p>
    <p>Hebrew: <span class="hb" lang="he" dir="rtl">בְּנִי אַתָּה אֲנִי הַיּוֹם יְלִדְתִּיךָ</span> — <i class="tl">beni attah, ani hayyom yelidtika</i>, “You are my son; I today have begotten you.”</p>
    <p>…comparison with the Greek of Hebrews/LXX…</p>
  </div>

  <div class="textnote">
    <p class="box-title">Textual Note</p>
    <p>… significant manuscript variants (e.g., 2:9 “by the grace of God” vs. “apart from God”) …</p>
  </div>

  <div class="views">
    <p class="box-title">Interpretive Options</p>
    <ul><li><b>View 1.</b> …</li><li><b>View 2.</b> …</li></ul>
    <p>Evaluation from the text …</p>
  </div>
</div>

<h3 class="sub">For Reflection</h3>   <!-- at the end of each section (end of the section's last file) -->
<ol class="reflect"><li>…</li></ol>
```

Inline conventions:
- Greek: `<span class="gk" lang="grc">λόγος</span> <i class="tl">logos</i>, “word”`
- Hebrew: `<span class="hb" lang="he" dir="rtl">דָּבָר</span> <i class="tl">davar</i>, “word”`
- Emphasis: `<em>`; strong: `<strong>`; book titles `<cite>`.
- Sub-groupings inside a long section (e.g., Hebrews 11): `<h3 class="sub" id="…">Abraham and the Patriarchs (11:8–22)</h3>`.
- Scripture references in plain text: (Ps 110:1), (Lev 16:14–15), (Rom 3:25). Use standard abbreviations: Gen, Exod, Lev, Num, Deut, Josh, Judg, 1 Sam, 2 Sam, 1 Kgs, 2 Kgs, 1 Chr, 2 Chr, Neh, Ps (plural Pss), Prov, Isa, Jer, Ezek, Dan, Hos, Hab, Hag, Zech, Mal, Matt, Mark, Luke, John, Acts, Rom, 1 Cor, 2 Cor, Gal, Eph, Phil, Col, 1 Thess, 2 Tim, Jas, 1 Pet, 2 Pet, 1 John, Rev. Apocrypha/other: Sir, Wis, 1 Macc, 2 Macc, 4 Macc. Josephus: *Ant.*, *J.W.*; Philo by treatise; Mishnah: m. Yoma 5:1 etc.

### XHTML rules (strict — the build will fail otherwise)
- Must be well-formed XML. Close every tag. Void elements self-close: `<br/>`.
- **No named HTML entities** (`&nbsp;`, `&mdash;`, `&rsquo;` etc. are forbidden). Use literal Unicode: “ ” ‘ ’ — – … Only `&amp;` `&lt;` `&gt;` are allowed.
- Use curly quotes “ ” and apostrophes ’. En dash for ranges (1:1–4), em dash for breaks.
- ids must be unique across the whole book: chapter `ch{c}`, section `sec-{c}-{firstverse}`, verse `v{c}-{v}`, other subheads `sub-{c}-{v}`.
- After writing each file, **run** `python3 /home/user/GrokBible/hebrews-study/tools/check.py <file>` and fix any error it reports.

## 5. Depth and length

- **Every verse gets its own `div.verse` entry** in order, with its own translation line (`p.vtext`) — do not merge verses.
- Typical verse entry: **400–900 words**; theologically dense or disputed verses (e.g., 1:3, 2:9, 2:17, 4:12, 4:15, 5:7–8, 6:4–6, 7:25, 9:14, 9:16–17, 10:14, 10:26, 11:1, 11:3, 12:2, 12:17, 13:8) may go to **1,000–1,600 words**. Short transitional verses may be 250–400.
- Each verse entry should normally contain: careful exposition of what the verse says and how it advances the argument; key Greek words/grammar explained; OT background (with Hebrew where relevant); historical/cultural background where it genuinely illuminates; cross-references that let Scripture interpret Scripture (quote them in your own translation when short); views of commentators where they help; and (briefly, not every verse) pastoral significance. Use the boxed `div`s when they help, not mechanically in every verse.
- "Setting and Structure" per section: 400–900 words. "For Reflection": 3–6 thoughtful questions per section.
- Do not pad. Depth means insight, not length.

## 6. Commentary, sources, and integrity (non-negotiable)

Authoritative commentators you may draw on (attribute by name in the text, e.g., “Westcott observes …”, “Lane argues …”):
- Ancient/Reformation: John Chrysostom (*Homilies on Hebrews*), Augustine, Thomas Aquinas, Martin Luther, John Calvin (*Commentary on Hebrews*), John Owen (*Exposition of Hebrews*), Matthew Poole, Matthew Henry.
- Modern: B. F. Westcott, Franz Delitzsch, James Moffatt, F. F. Bruce (NICNT), Philip E. Hughes, Simon Kistemaker, William L. Lane (WBC), Paul Ellingworth (NIGTC), Harold Attridge (Hermeneia), Donald Hagner, George H. Guthrie (NIVAC; and his chapter in Beale & Carson, *Commentary on the NT Use of the OT*), Craig Koester (Anchor Bible), Luke Timothy Johnson, David A. deSilva (*Perseverance in Gratitude*), Gareth Lee Cockerill (NICNT), Thomas R. Schreiner, Geerhardus Vos, Murray J. Harris (*Jesus as God*, on 1:8), Bruce M. Metzger (*Textual Commentary*), BDAG (lexicon).
- **Do not cite Peter T. O'Brien's Hebrews commentary** (withdrawn by its publisher).
- Primary historical sources: Josephus, Philo, the Mishnah (esp. Yoma, Tamid, Middot), Dead Sea Scrolls (11QMelchizedek, 1QS, 4QDeut^q), 1–4 Maccabees, Sirach, Wisdom of Solomon, 1 Enoch, 1 Clement, Eusebius, Tertullian, Origen, Suetonius, Tacitus.

Integrity rules:
1. **Never fabricate quotations.** Do not put words in quotation marks attributed to any modern commentator. Paraphrase their view and attribute it **only when you are confident the scholar actually holds it**; otherwise say “some interpreters,” “many commentators,” etc. No page numbers.
2. Short direct quotations of ancient/Reformation writers or primary sources only when you are **highly confident** of the wording (and they must be your own rendering or a public-domain rendering); otherwise paraphrase.
3. **Scripture is the final authority.** Use only commentary that coheres with the text of Hebrews and the whole of Scripture. If a well-known interpretation is contradicted by Scripture, either omit it or, if the reader needs to know of it, briefly show from Scripture why it cannot stand. Do not present speculation as fact.
4. On genuinely disputed questions, present the major views fairly, weigh them from the Greek text, the immediate context, the argument of Hebrews, and the wider canon, and state a reasoned conclusion with appropriate humility.
5. Do not invent historical "facts." If uncertain, say so or leave it out.
6. Keep the Christ-centered argument of Hebrews in view: the better word, the better priest, the better covenant, the better sacrifice, the better sanctuary, the better hope — and the urgent call to hold fast, draw near, and go out to him.

## 7. Overall book context (for consistency; do not repeat at length — the Introduction covers it)

The Introduction will take these positions; stay consistent with them:
- Author: anonymous (the writer does not name himself; 2:3 places him among second-generation hearers). Ancient candidates (Paul, Barnabas, Luke, Apollos, Clement) are noted; the study does not depend on a name. Refer to him as “the author,” “the writer,” or “the preacher.”
- Genre: a written sermon, “word of exhortation” (13:22), alternating exposition and exhortation, sent with a brief letter-ending.
- Audience: a congregation of Jewish Christians (likely with some Gentiles), probably in or connected to Rome (13:24 “those from Italy”), second-generation believers (2:3), who had endured earlier persecution (10:32–34) and were now tempted to drift, grow sluggish, and draw back toward the old covenant’s securities.
- Date: before AD 70 (the Levitical ritual is spoken of as still functioning, 8:4–5; 9:6–9; 10:1–3; 10:11; the destruction of the temple would have been decisive for the argument yet is never mentioned) — likely the mid-60s.
- Key theme: God has spoken finally in his Son, who is the superior revealer and the eternal high priest after the order of Melchizedek, whose once-for-all sacrifice inaugurates the new covenant and opens access to God; therefore hold fast, draw near, and persevere in faith.
