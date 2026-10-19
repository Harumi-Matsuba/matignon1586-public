# Method and checks

[日本語](METHOD.md)

## Steps
1. **Images**: Gallica, BnF fr. 15572 (ark:/12148/btv1b9061879d), view 225 (f. 218r) and view 226 (ff. 218v–219r). Each page was deskewed (f. 218r −3.5°, f. 218v −0.7°, f. 219r −2.6°) and every line cut into three enlarged pieces. The images are not in this repository.
2. **Transcription**: each sign was given a name (`data/key.tsv`, column 1) and each line written as a row of sign names (`data/transcription_*.txt`). The vertical strokes of the manuscript (word dividers) are kept as `|`. A sign whose shape is uncertain carries `?`.
3. **Key**: Satoshi Tomokiyo's reconstruction (Cryptiana) of Mayenne–Forget's Cipher-2. Signs not in his table were given values that fit several words within this letter; they are marked `inferred`. The words they were checked on are in column 4 of `data/key.tsv`.
4. **Decoding**: `src/decode.py` applies the key to the transcription (`data/decoded_*.txt`). The reading ([READING.en.md](READING.en.md)) is that output with word division and punctuation added.

## Figures (`src/decode.py`, `src/control.py`, run on 20 Oct 2026)
### Share of signs given a value
| page | signs | valued by Tomokiyo's table alone | valued with inferred values |
|---|---|---|---|
| f. 218r | 713 | 657 (92.1%) | 704 (98.7%) |
| f. 218v | 927 | 838 (90.4%) | 922 (99.5%) |
| f. 219r | 499 | 448 (89.8%) | 486 (97.4%) |

### Shuffled-key controls (1,000 each)
The same transcription was decoded with keys in which the values of the letter signs were permuted, and its "Frenchness" compared with that of the real key. Frenchness is the mean log-likelihood of letter trigrams (built from the top 50,000 French words of `wordfreq`, with j→i and v→u). Code signs are left out of the score.

| page | condition | real key | shuffled keys (min / median / max) | shuffled ≥ real |
|---|---|---|---|---|
| f. 218r | with inferred values | −2.352 | −5.665 / −5.072 / −4.139 | 0 / 1000 |
| f. 218r | table signs only | −2.363 | −5.580 / −4.879 / −4.180 | 0 / 1000 |
| f. 218v | with inferred values | −2.590 | −5.626 / −5.045 / −4.492 | 0 / 1000 |
| f. 218v | table signs only | −2.620 | −5.721 / −4.871 / −4.124 | 0 / 1000 |
| f. 219r | with inferred values | −2.442 | −5.712 / −5.068 / −4.308 | 0 / 1000 |
| f. 219r | table signs only | −2.401 | −5.589 / −4.927 / −4.095 | 0 / 1000 |

This shows only that the table's values give text far closer to French than chance assignments do. It does not show that any single sign is read right.

### Inferred values that agree with another study's key
The values inferred here were compared with the key Brett Burford built for another Cipher-2 letter, fr. 15573 f. 385, against decipherments of the time (`data/key-cipher2.json` in BravoBravoIX/mayenne-forget-1586-cipher-reading, version of 19 Oct 2026). Sign names differ between the two studies, so signs were matched by shape.

| inferred here | Burford's key | when the value was found here |
|---|---|---|
| 17 = tant | 17 = tant (F) | before seeing his key (f. 218r) |
| underlined gg = par | gg = par (T?) | before seeing his key (f. 218r) |
| barred x = s | xbar = s / ss (T+E) | s before; ss (necessaire) after |
| 13 = tre | 13 = tre (F?) | after |
| ϕ = en | phi = en (T+E) | after |
| barred h (Qh) = armée | Qh = armee (F) | after (checked on « ladicte armée au partir de ce siege ») |
| ɞ with a stroke (curl) = pour | curl = pour (T+E-eye) | after |
| long rectangle (rect) = icy | rect = icy (E-eye?) | after |
| N-shape = ée | N = ee (F) | after |
| ꝶ-shape (zk) = p | zk = p (E-eye) | after |

ff. 218v and 219r were transcribed after seeing Burford's key. The "after" values were checked to fit their contexts in this letter, but they were not found independently.

## Calibration (a letter with a decipherment of the time, 20 Oct 2026)
- Letter: BnF fr. 15573 f. 103v (Mayenne to the King, September 1586, same Cipher-2; Gallica ark:/12148/btv1b90618780, view 212). Its left margin carries the decipherment made at the time.
- Procedure: cipher lines 1–6 (157 signs) were transcribed with the same sign names and the same key **before** the decipherment was looked at (`calib/transcription_f103v_l1-6.txt`). Fragments of the margin decipherment show at the left edge of the line cuts; they were not read. The decode was then compared letter by letter (`src/calib.py`) with the decipherment of the time: Brett Burford's eye reading, checked on view 212, with one abbreviation corrected (« lad[icte] riviere ») (`calib/ref_f103v_l1-6.txt`).
- Result: against 214 reference letters, edit distance 54 (21 substitutions, 24 letters missing, 9 extra). **Letter agreement 74.8%** (71.0% with the table alone).
- What the differences are (sorted by eye):
  - code signs with no value in the key, for a place name and a long word: Dordoigne, extremement (its "extreme"). Most of the missing letters are these;
  - confusions of similar signs: ϖ with two humps (il) and three (est); # and barred tt (les); round ℒ (n);
  - key values that do not fit here: χ° stands where the decipherment has « pour » (q in the key); the barred h stands where it has « tous » (armée in the key);
  - the first three signs misread (Nous).
- Following this, the sign written as il in f. 218r lines 9–10 was corrected to tt (les): « pour veoir les ennemis », « de les empescher ». The key was not tuned on the six calibration lines.
- Meaning: the reading, transcription and key together, may be wrong in about one letter in four. In this letter, values of ambiguous signs were chosen by context, so errors are expected to be fewer than in the six calibration lines (read without context). That has not been checked.

## Second transcription (independent reading, 20 Oct 2026)
- Reader: OpenAI's Codex CLI (codex-cli 0.163.0-alpha.10.2, bundled with the ChatGPT app; default model, whose name does not appear in the run log).
- Input: only the line images of the three pages (each line cut into a left and a right half; f. 218r 27 lines, f. 218v 34, f. 219r 19; cut by `second/crop_lines.py` from the same deskewed images as the first pass) and the prompt (`second/PROMPT.md`). The prompt gives only sign names and shape descriptions — no values, no first transcription, no key, no decoded text. Names that reveal a value (=que, =pour, par2 …) were replaced by neutral names such as W01–W18 (mapping in `second/names_map.tsv`).
- Runs: one run per page, each started separately from an empty folder with `codex exec --ephemeral -s read-only`. The run logs (`second/codex_events_*.jsonl`) contain a single reply each, with no commands and no file reads. The output is `second/transcription2_*.txt`, unedited.
- Comparison with the first pass (`src/compare2.py`: edit distance between the sign sequences of each page, divided by the number of signs in the first pass; dividers `|` left out):

| page | signs (1st / 2nd) | sign-name agreement | value agreement | sign-name agreement after relabelling |
|---|---|---|---|---|
| f. 218r | 713 / 710 | 76.7% | 77.4% | 84.2% |
| f. 218v | 927 / 934 | 63.2% | 65.6% | 85.0% |
| f. 219r | 499 / 507 | 61.5% | 63.9% | 76.8% |
| all | 2,139 / 2,151 | 67.3% | 69.1% | 82.8% |

- Most differences are signs of the same shape to which the second reader consistently gave another name. Taking, for each name of the second pass, the first-pass name it was most often aligned with (5 times or more) gives 13 pairs: f→fi, fn→f, fi→dl, nu→dl, 2→4, g2→J, phi→th, pl→zk, Ln→A<, .2.→.3., sl→=la, co→en2, ?→=que. The written shape descriptions apparently did not tie the names to the shapes. On the images of the left half of f. 218v line 6 and the right half of line 5 we checked that the second reader calls the δ-shape (dl), the 4 with a slanting stroke and the sign after ꝗ (J) fi, 2 and g2 respectively. The other pairs were not checked on the images. The last column applies this relabelling to the second pass; because the relabelling is fitted to the same data, it overstates the agreement.
- Of the disagreements left after relabelling (`second/diff_after_relabel.tsv`, 283 places), the main ones that change a value are: 4H (e) read as 4 (a), 18 places; fn read as y2, 15; 8 (t) read as dl (e), 11; 2 (m) read as J, 9. The first pass chose between similar signs by context in places (see Limits). These have not yet been rechecked on the images ([OPEN.en.md](OPEN.en.md)).
- Decoding the second transcription with the same key and running the shuffled-key control (1,000 each): the real key scores −3.095 (f. 218r), −3.910 (f. 218v), −3.480 (f. 219r), above the best shuffled key (−3.952, −4.275, −4.360); shuffled ≥ real 0/1000 on all three pages. The scores are lower than for the first pass (−2.35 to −2.59) because of the naming differences and misreadings above.
- The key and the reading were not changed after the second transcription.

## Use of AI
- Transcription of the images, inferred values, decoding, scripts and documents were done by Anthropic's Claude (Claude Code, model Claude Opus 5.5). A person (the owner of this repository) chose the target, saved the images and decided on publication.
- In the first pass each line was transcribed into sign names once, without voting. A second transcription by another AI (Codex) is described in the section above.
- **No human has checked the transcription.** Both transcriptions were made by AI; agreement between AIs is not a substitute for human checking.
- For ff. 218v and 219r, the plain text was first read from the images, and only then were the lines transcribed into sign names. The transcription may have been pulled toward that first reading.

## Limits
- The calibration covers six lines (157 signs) only, and the accuracy of the transcription alone (sign by sign) was not measured separately.
- Similar signs (f / long f / ƒ; δ / 8 / ɣ; ꝗ / 4; the hooked ʃ family; ∝ and ∝ with a loop below; round ℒ and angular ∠) were chosen by context in places. This favours the real key in the controls.
- Most inferred values were checked on only two or three places in this letter. Those checked on one place only say so in `data/key.tsv`.
- Signs with no value and unread passages are in [OPEN.en.md](OPEN.en.md).
