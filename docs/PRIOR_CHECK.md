# 先行の確かめ（BnF fr. 15572 ff. 218r–219r の読み）

[English](PRIOR_CHECK.en.md)

解読した者とは別の検証役が、読み・書き起こし・これまでの先行調査の記録（[SOURCES.md](../SOURCES.md)）を受け取り、先行を否定するつもりで探した記録です。調べたのは 2026-10-20（日本時間）です。見つからなかったことは、誰も手を付けていないことの証明にはなりません。

## 確かめた主張
Matignon から国王アンリ3世への書簡（Monségur の前の陣、1586年5月）の暗号部分（ff. 218r–219r、Mayenne–Forget の Cipher-2）を読んだこと。

## 結論
- 区分：**見つからない**。下の調べた先（2026-10-20）では、この暗号部分の先行の解読（当時の解読文の写し、刊本、他のプロジェクトの読み）が見当たらない。
- 同じ包囲を書いた平文の記録はある（Aubigné『世界史』、同じ巻の f. 221r–v の別の報告など）。ただし、どれもこの書簡の平文ではなく、この暗号文との対応はない。読みの内容と照らす材料にはなる。
- 「初めて」とは言い切らず、「（調べた先と日付）では先行の解読が見当たらない」と書くのがよい。

## 調べた先（2026-10-20）
| 調べた先 | 版・日付 | 結果 |
|---|---|---|
| 1. 友清理士 *Henry III's Cipher with Ambassadors* https://cryptiana.web.fc2.com/code/henryiii.htm | Last-Modified 2023-09-23 | Mayenne-Forget's Cipher-2 の節に「This cipher was used not only by Forget but also by Matignon (ff.218-219, undeciphered)」。読みはない |
| 同 unsolved.htm・ai.htm・verification.htm | 2026-10-13・2026-10-19・2026-10-15 | ff. 218–219、Monségur への言及はない |
| 2. D. Bourdeau, cyphersolver https://github.com/dbourdeau/cyphersolver | origin/main 0258b8ab（2026-10-18） | catalogue.json の12番は「Narrowed 14 Oct 2026 … to the Cipher-2 leaves, the only part of the item not taken up」。targets/matignon1586/NOTES.md に「The genuine Cipher-2 leaves, fr. 15572 ff. 218–219, were never attempted」。issue・PR（2026-10-17 以降の全件）で Matignon を扱うのは #44（BravoBravoIX、fr. 15573 ff. 379–381）、#46（同、f. 385）、#49 で、#49 はこのリポジトリの報告 |
| 3. BravoBravoIX/mayenne-forget-1586-cipher-reading、BravoBravoIX/matignon-1586-cipher-reading | cc0daf7・e5e6fc0（2026-10-19） | 対象は fr. 15573 f. 385 と ff. 379–381。PRIOR-ART.md は ff. 218–219 を「not attempted、自分たちの対象ではない」とする |
| 4. NoAutopilot/cipher-lab | 2026-10-19 の版、issue | fr. 15572 の Cipher-1 の作業だけ。ff. 218–219 は、友清氏の「undeciph.」の写しがあるだけ。issue #29（fr. 15572 の手がかり）にも記述はない。#72 はこのリポジトリの報告 |
| 5. pangoleen/cipher-readings | 820fb4e（2026-10-14） | 該当なし |
| 6. GitHub のリポジトリ検索（15572、Matignon cipher、Monsegur、Mayenne-Forget） | — | 関係するのは上の3と、このリポジトリだけ |
| 7. archive.org の全文検索（Sacremore と Monségur、Monségur と Matignon と 1586、fr. 15572 など） | — | 包囲の叙述が見つかった：Aubigné『Histoire universelle』（de Ruble 版 t. 7、第11巻 第8章「Siège de Monségur」）は、22門の大砲で三つの砲台、2日目に1500発、Sacremore の連隊の突撃、Mayenne の病気を書く。この章の注は de Thou 第85巻を引き、同じ巻の第4章の注は Caillière『Histoire du mareschal de Matignon』を引く。『Mémoires du vicomte de Turenne』の注は、4月24日に包囲、5月10日に降伏とする。この書簡を載せた刊本や、fr. 15572 ff. 218–219 を引く文献は見つからない |
| 8. BnF fr. 15572 の前後のコマ（Gallica ark:/12148/btv1b9061879d、f222〜f224、f227〜f232。BnF の IIIF で取得） | — | 当時の解読文の写しは見当たらない。f227 の右ページ下の薄い記号は、裏の暗号の透けとみられる。f. 221r–v（f228・f229）は別の平文の報告で「Du 9me May 1586」と結び、Matignon を三人称で書く。この暗号文の解読ではない（全文は読んでいない） |
| 9. ウェブ検索（Matignon・Monségur・Sacremore・1586・chiffre、fr. 15572、Lasry 氏の論文） | — | 該当なし。Lasry 氏の論文で見つかったのは別の書簡（Sennecey など） |

## 調べていない先・確かめられなかった先
- 確かめられなかった：Gallica の全文検索（SRU）は Cloudflare のボット確認で止まった（回避はしていない）。Google Books の検索は API が 429 で止まった。GitHub のコード検索は、このリポジトリ自身も出てこなかったので、網羅できていない。
- 調べていない：Caillière『Histoire du mareschal de Matignon』（1661）の本文、de Thou 第85巻の本文、*Lettres de Henri III*（Société de l'histoire de France）、モナコ宮殿文書館の Matignon 文書、Archives historiques de la Gironde、DECODE のデータベース、HathiTrust の全文検索、Cryptoole。
