# Matignon to the King, camp before Monségur, May 1586: a provisional reading of the cipher

[日本語 README](README.md)

| | |
|---|---|
| Status | **Partial reading** (most of the three pages reads as French, but 28 signs have no value and some passages are unread). Grounds: control 0/1000 (all three pages) / at least one passage that makes sense / value agreement with the independent second transcription (lower of v3 and v4) f. 218r 72.1%, f. 218v 82.5%, f. 219r 73.9% (≥ 70%; below the 85% needed for a full reading) / calibration 74.8% (≥ 65%) |
| Relation to prior work | No earlier reading of this letter was found in the places searched on 19–20 Oct 2026 ([SOURCES.en.md](SOURCES.en.md)) (Tomokiyo: undeciphered; Bourdeau's ledger: never attempted). No search for prior work by a checker other than the decipherer, trying to refute novelty, has been done yet, so this is not claimed as a first. The table is Tomokiyo's reconstruction; some inferred values agree with Burford's key (see "What this reading adds" below) |
| Human checking | **No human has checked the transcription.** The first transcription is by an AI (Claude), the second by another AI (Codex); the review of the disagreements on ff. 218v and 219r against the images was also done by AI (Claude). Agreement between AIs is not a substitute for human checking |
| Figures | Control: shuffled keys scoring at or above the real key, 0 of 1,000 on each page / Calibration: 74.8% letter agreement on six lines with a contemporary decipherment / Independent second transcription (Codex, two runs without seeing the first; v3, v4), agreement (sign name / value): v3 f. 218r 82.6% / 83.7%, f. 218v 82.9% / 85.7%, f. 219r 77.7% / 81.7%; v4 68.6% / 72.1%, 79.4% / 82.5%, 70.9% / 73.9%. The figures of the two earlier runs used in the review (v1, v2) are in [docs/METHOD.en.md](docs/METHOD.en.md) |
| Use of AI | Transcription, inferred values, decoding, scripts and documents by Claude (Claude Opus 5.5); second transcription by OpenAI Codex. A person chose the target, saved the images and decided on publication (see "Use of AI" below) |

A reading of the enciphered part of a letter from Marshal Matignon to King Henri III, BnF Français 15572 ff. 218r–219r, with Mayenne–Forget's Cipher-2 as reconstructed by Satoshi Tomokiyo.

- Source: BnF Français 15572, Gallica ark:/12148/btv1b9061879d, views 225 (f. 218r) and 226 (ff. 218v–219r). f. 218r has 26 cipher lines after clear text, f. 218v is all cipher (34 lines), f. 219r has 19 cipher lines, then the clear closing and signature.
- Closing: « Du camp devant Monsegur ce [?] May 1586 », signed Matignon (checked on the image).
- Status before this work: Tomokiyo lists ff. 218–219 as Cipher-2, "undeciphered" ([Cryptiana](https://cryptiana.web.fc2.com/code/henryiii.htm)); D. Bourdeau's ledger (cyphersolver), item 12: "never attempted" (version of 18 Oct 2026). We found no reading of this letter in the places we searched on 19–20 Oct 2026 (listed in [SOURCES.en.md](SOURCES.en.md)).

## Status (partial)
| page | signs | given a value by Tomokiyo's table alone | with inferred values | shuffled-key controls (1,000) scoring at or above the real key |
|---|---|---|---|---|
| f. 218r | 713 | 92.1% | 98.7% | 0 |
| f. 218v | 926 | 90.3% | 99.5% | 0 |
| f. 219r | 498 | 89.6% | 97.4% | 0 |

- Most of all three pages reads as French ([docs/READING.en.md](docs/READING.en.md)). 28 signs have no value and a few short passages are unread ([docs/OPEN.en.md](docs/OPEN.en.md)).
- **Calibration**: six cipher lines of fr. 15573 f. 103v (same cipher, contemporary decipherment in the margin) were read blind with the same names and key. Against that decipherment the letter agreement is 74.8% (71.0% with Tomokiyo's table alone). Nearly half of the differences come from code signs missing from the key (a place name, a long word); the rest are mostly confusions of similar signs. Read the reading here with that in mind.

## Content (summary)
- A day's battery (about 1,200 shots) did less than hoped: the wall was stronger than expected. Three breaches were made.
- In the evening the sieur Sacramore de Birague went for the lodgement from the breach, was badly wounded and had to withdraw; the lodgement was not taken.
- From now on, less firing and a step-by-step approach. The army is worn out; payment of the troops matters most.
- The Duke of Mayenne has a fever, but the physicians are hopeful and there is no sign of danger.

## What this reading adds, and what it rests on
**It rests on**
- Tomokiyo's reconstruction of Cipher-2 ([henryiii_MayenneForget2.png](https://cryptiana.web.fc2.com/code/henryiii_MayenneForget2.png); not copied here).
- Tomokiyo's and Bourdeau's identification of this letter as Cipher-2 and unread.

**Added here**
1. A sign-by-sign transcription of the three pages (`data/transcription_*.txt`).
2. Values for signs not in the table, inferred from this letter (27 = d, 17 = tant, a hooked sign = tout, underlined gg = par, …; `inferred` in `data/key.tsv`). Ten of them agree with the key Brett Burford built for fr. 15573 f. 385 against decipherments of the time, but most were checked here after seeing his key ([docs/METHOD.en.md](docs/METHOD.en.md)).
3. The content of the letter.

## Use
```
python3 src/decode.py data/key.tsv data/transcription_f218r.txt
python3 src/decode.py data/key.tsv data/transcription_f218r.txt --table-only
python3 src/control.py data/key.tsv data/transcription_f218r.txt 1000   # needs wordfreq
python3 -m unittest discover -s tests
```

## Files
| path | contents |
|---|---|
| data/transcription_f218r.txt etc. | sign-by-sign transcription, line by line |
| data/key.tsv | sign name → value, with its source (table / inferred / unknown) and the shape and evidence in Japanese and English |
| data/decoded_*.txt | output of `src/decode.py` |
| docs/READING.en.md | the reading (French, with punctuation added) and a summary |
| docs/METHOD.en.md | method, figures, calibration, use of AI, limits |
| docs/OPEN.en.md | signs with no value, unread passages, facts not checked |
| calib/, src/calib.py | the calibration on fr. 15573 f. 103v |
| second/, src/compare2.py | second transcriptions (Codex v1–v4), prompts, run logs, comparison with the first, and the list of the image review (second/review_f218v_f219r.tsv) |
| SOURCES.en.md | sources and the search for earlier work |

Every document also has a Japanese version (the file name without `.en`).

## Changes
- **20 Oct 2026**: the transcription of ff. 218v and 219r was corrected in 19 places after rechecking on the images its disagreements with the second transcription (Codex); 178 places were left unchanged (list: `second/review_f218v_f219r.tsv`). Signs: f. 218v 927→926, f. 219r 499→498. Share valued by the table alone: f. 218v 90.4%→90.3%, f. 219r 89.8%→89.6% (with inferred values unchanged at 99.5% and 97.4%). After the review the independent second transcription by Codex was redone twice (v3, v4); the lower value agreement is f. 218r 72.1%, f. 218v 82.5%, f. 219r 73.9% (v1, before the review: 77.4%, 65.6%, 63.9%). The six χ° places were changed to xo, so the decoder output (`data/decoded_*.txt`) there changes from pour to q (the reading keeps pour; see [docs/OPEN.en.md](docs/OPEN.en.md)).

## Use of AI
Transcription, inferred values, decipherment, scripts and documents were done by Anthropic's Claude (Claude Code, Claude Opus 5.5). A person chose the target, saved the images and decided on publication. The second transcription was made four times by OpenAI's Codex (codex-cli 0.163.0-alpha.10.2, default model) without seeing the first transcription, the key or any values (v1–v4; the assessment uses v3 and v4, made after the review). No human has checked the transcription.

Licence: code MIT, own text and data CC BY 4.0 ([LICENSE](LICENSE)).
