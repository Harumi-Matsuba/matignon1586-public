# Matignon to the King, camp before Monségur, May 1586: a first reading of the cipher

[日本語 README](README.md)

A reading of the enciphered part of a letter from Marshal Matignon to King Henri III, BnF Français 15572 ff. 218r–219r, with Mayenne–Forget's Cipher-2 as reconstructed by Satoshi Tomokiyo.

- Source: BnF Français 15572, Gallica ark:/12148/btv1b9061879d, views 225 (f. 218r) and 226 (ff. 218v–219r). f. 218r has 26 cipher lines after clear text, f. 218v is all cipher (34 lines), f. 219r has 19 cipher lines, then the clear closing and signature.
- Closing: « Du camp devant Monsegur ce [?] May 1586 », signed Matignon (checked on the image).
- Status before this work: Tomokiyo lists ff. 218–219 as Cipher-2, "undeciphered" ([Cryptiana](https://cryptiana.web.fc2.com/code/henryiii.htm)); D. Bourdeau's ledger (cyphersolver), item 12: "never attempted" (version of 18 Oct 2026). We found no reading of this letter in the places we searched on 19–20 Oct 2026 (listed in [SOURCES.md](SOURCES.md), in Japanese).

## Status (v0.1, partial)
| page | signs | given a value by Tomokiyo's table alone | with inferred values | shuffled-key controls (1,000) scoring at or above the real key |
|---|---|---|---|---|
| f. 218r | 713 | 92.1% | 98.7% | 0 |
| f. 218v | 927 | 90.4% | 99.5% | 0 |
| f. 219r | 499 | 89.8% | 97.4% | 0 |

- Most of all three pages reads as French ([docs/READING.md](docs/READING.md); the reading is in French, the notes in Japanese). 28 signs have no value and a few short passages are unread ([docs/OPEN.md](docs/OPEN.md)).
- **Calibration**: six cipher lines of fr. 15573 f. 103v (same cipher, contemporary decipherment in the margin) were read blind with the same names and key. Against that decipherment the letter agreement is 74.8% (71.0% with Tomokiyo's table alone). Nearly half of the differences come from code signs missing from the key (a place name, a long word); the rest are mostly confusions of similar signs. Read the reading here with that in mind.

## Content (summary)
- A day's battery (about 1,200 shots) did less than hoped: the wall was stronger than expected. Three breaches were made.
- In the evening the sieur Sacramore de Birague went for the lodgement from the breach, was badly wounded and had to withdraw; the lodgement was not taken.
- From now on, less firing and a step-by-step approach. The army is worn out; payment of the troops matters most.
- The Duke of Mayenne has a fever, but the physicians are hopeful and there is no sign of danger.

## What is new here, and what it rests on
**It rests on**
- Tomokiyo's reconstruction of Cipher-2 ([henryiii_MayenneForget2.png](https://cryptiana.web.fc2.com/code/henryiii_MayenneForget2.png); not copied here).
- Tomokiyo's and Bourdeau's identification of this letter as Cipher-2 and unread.

**New here**
1. A sign-by-sign transcription of the three pages (`data/transcription_*.txt`).
2. Values for signs not in the table, inferred from this letter (27 = d, 17 = tant, a hooked sign = tout, underlined gg = par, …; `inferred` in `data/key.tsv`). Ten of them agree with the key Brett Burford built for fr. 15573 f. 385 against decipherments of the time, but most were checked here after seeing his key ([docs/METHOD.md](docs/METHOD.md)).
3. The content of the letter.

## Use
```
python3 src/decode.py data/key.tsv data/transcription_f218r.txt
python3 src/decode.py data/key.tsv data/transcription_f218r.txt --table-only
python3 src/control.py data/key.tsv data/transcription_f218r.txt 1000   # needs wordfreq
python3 -m unittest discover -s tests
```

## Use of AI
Transcription, inferred values, decipherment, scripts and documents were done by Anthropic's Claude (Claude Code, Claude Opus 5.5). A person chose the target, saved the images and decided on publication.

Licence: code MIT, own text and data CC BY 4.0 ([LICENSE](LICENSE)).
