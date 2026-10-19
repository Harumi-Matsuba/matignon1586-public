# Prior-work check (the reading of BnF fr. 15572 ff. 218r–219r)

[日本語](PRIOR_CHECK.md)

A checker who did not do the decipherment received the reading, the transcriptions and the earlier prior-work notes ([SOURCES.en.md](../SOURCES.en.md)), and searched for prior work with the aim of refuting the claim below. The search was done on 20 October 2026 (Japan time). Not finding something does not prove that nobody has worked on it.

## Claim checked
That the cipher part (ff. 218r–219r, Mayenne–Forget's Cipher-2) of Matignon's letter to King Henri III (camp before Monségur, May 1586) has been read here.

## Conclusion
- Category: **not found**. In the places below (20 October 2026), no earlier decipherment of this cipher part was found: no contemporary deciphered copy, no print, no reading in another project.
- Plaintext accounts of the same siege exist (Aubigné's *Histoire universelle*, another report on f. 221r–v of the same volume, and others). None of them is the plaintext of this letter, and none corresponds to this ciphertext. They can serve to check the content of the reading.
- It should not be called "first"; it should be described as "no earlier decipherment was found in (places checked, date)".

## Places checked (20 October 2026)
| Place | Version or date | Result |
|---|---|---|
| 1. S. Tomokiyo, *Henry III's Cipher with Ambassadors*, https://cryptiana.web.fc2.com/code/henryiii.htm | Last-Modified 23 Sep 2023 | Section on Mayenne-Forget's Cipher-2: "This cipher was used not only by Forget but also by Matignon (ff.218-219, undeciphered)". No reading |
| Same site, unsolved.htm, ai.htm, verification.htm | 13 Oct, 19 Oct, 15 Oct 2026 | No mention of ff. 218–219 or Monségur |
| 2. D. Bourdeau, cyphersolver, https://github.com/dbourdeau/cyphersolver | origin/main 0258b8ab (18 Oct 2026) | catalogue.json, item 12: "Narrowed 14 Oct 2026 … to the Cipher-2 leaves, the only part of the item not taken up". targets/matignon1586/NOTES.md: "The genuine Cipher-2 leaves, fr. 15572 ff. 218–219, were never attempted". Of all issues and PRs from 17 October 2026 on, those on Matignon are #44 (BravoBravoIX, fr. 15573 ff. 379–381), #46 (same, f. 385) and #49, which is this repository's own report |
| 3. BravoBravoIX/mayenne-forget-1586-cipher-reading and BravoBravoIX/matignon-1586-cipher-reading | cc0daf7, e5e6fc0 (19 Oct 2026) | Their subjects are fr. 15573 f. 385 and ff. 379–381. PRIOR-ART.md calls ff. 218–219 "not attempted" and not their leaf |
| 4. NoAutopilot/cipher-lab | version of 19 Oct 2026, issues | Only the Cipher-1 work on fr. 15572. For ff. 218–219 there is only a copy of Tomokiyo's "undeciph.". Issue #29 (fr. 15572 leads) says nothing on them. #72 is this repository's own report |
| 5. pangoleen/cipher-readings | 820fb4e (14 Oct 2026) | Nothing relevant |
| 6. GitHub repository search (15572, Matignon cipher, Monsegur, Mayenne-Forget) | — | Only item 3 and this repository are related |
| 7. archive.org full-text search (Sacremore with Monségur; Monségur with Matignon and 1586; fr. 15572; etc.) | — | Accounts of the siege were found. Aubigné's *Histoire universelle* (de Ruble's edition, vol. 7, book 11, ch. 8, "Siège de Monségur") gives three batteries from twenty-two guns, 1,500 shots on the second day, the assault led by Sacremore's regiment and Mayenne's illness. The chapter's notes cite de Thou book 85, and a note in chapter 4 of the same volume cites Caillière's *Histoire du mareschal de Matignon*. A note in the *Mémoires du vicomte de Turenne* dates the siege from 24 April and the surrender to 10 May. No print of this letter and no work citing fr. 15572 ff. 218–219 was found |
| 8. The neighbouring views of BnF fr. 15572 (Gallica ark:/12148/btv1b9061879d, f222–f224 and f227–f232, fetched through BnF's IIIF service) | — | No contemporary deciphered copy. The faint signs at the foot of the right-hand page of view 227 look like show-through of the cipher on the other side. Ff. 221r–v (views 228–229) are a separate plaintext report ending "Du 9me May 1586", which refers to Matignon in the third person; it is not a decipherment of this ciphertext (it was not read in full) |
| 9. Web search (Matignon, Monségur, Sacremore, 1586, chiffre; fr. 15572; Lasry's papers) | — | Nothing relevant. Lasry's papers found concern other letters (Sennecey and others) |

## Not checked, or could not be checked
- Could not be checked: Gallica full-text search (SRU) stopped at a Cloudflare bot check (not bypassed). Google Books search stopped with 429 from the API. GitHub code search did not return even this repository, so it is not exhaustive.
- Not checked: the text of Caillière's *Histoire du mareschal de Matignon* (1661), the text of de Thou book 85, the *Lettres de Henri III* (Société de l'histoire de France), the Matignon papers in the Archives of the Prince's Palace in Monaco, the *Archives historiques de la Gironde*, the DECODE database, HathiTrust full-text search, and Cryptoole.
