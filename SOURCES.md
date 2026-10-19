# 出典

## 一次資料（リポジトリには含めていない）
- **BnF, Français 15572**（1586年1月〜7月の書簡集）
  - Gallica ark:/12148/btv1b9061879d
  - 225コマ：f. 217v（左）と f. 218r（右）。f. 218r の暗号部分を読んだ。https://gallica.bnf.fr/ark:/12148/btv1b9061879d/f225.item
  - 226コマ：f. 218v（左）と f. 219r（右）。https://gallica.bnf.fr/ark:/12148/btv1b9061879d/f226.item
  - 227コマ：f. 219v（宛名と封。暗号はない）。

- **BnF, Français 15573**（較正に使った）
  - Gallica ark:/12148/btv1b90618780 の212コマ：f. 103v（Mayenne から国王へ、1586年9月）。暗号1〜6行目と、左余白の当時の解読。https://gallica.bnf.fr/ark:/12148/btv1b90618780/f212.item

画像は再配布していません。コマ番号で参照してください。Source gallica.bnf.fr / BnF.

## 鍵
- 友清理士（Satoshi Tomokiyo）, *Henry III's Cipher with Ambassadors*（Cryptiana）
  - https://cryptiana.web.fc2.com/code/henryiii.htm （Last-Modified 2023-09-23）
  - Mayenne-Forget's Cipher-2 の節：使用例の一覧に ff. 218-219 を挙げ、« This cipher was used not only by Forget but also by Matignon (ff.218-219, undeciphered) » とする。
  - 表の画像：https://cryptiana.web.fc2.com/code/henryiii_MayenneForget2.png （このリポジトリには含めていない。`data/key.tsv` の table の値は、この表を記号名に置き換えたもの）

## 照らした研究
- Brett Burford, *First reading of the whole cipher letter BnF fr. 15573 f. 385 (Mayenne-Forget Cipher-2, 1586)*
  - https://github.com/BravoBravoIX/mayenne-forget-1586-cipher-reading （2026-10-19 10:23 UTC の版、CC BY 4.0）
  - `data/key-cipher2.json` の値と、この書簡の推定を比べた（[docs/METHOD.md](docs/METHOD.md)）。
  - 較正の参照には、同リポジトリの `data/known-text/f103v-decipherment.txt`（当時の解読の目読み）の冒頭を使った（`calib/ref_f103v_l1-6.txt`。出典を明記）。ほかのファイルは含めていない。

## 先行の確かめ（2026-10-19〜20）
見つからないことは、手を付けた人がいないことの証明にはなりません。

| 調べた先 | 結果 |
|---|---|
| D. Bourdeau, cyphersolver（https://github.com/dbourdeau/cyphersolver 、origin/main 0258b8ab、2026-10-18） | 台帳12番。targets/matignon1586/NOTES.md に « The genuine Cipher-2 leaves, fr. 15572 ff. 218–219, were never attempted and are in no entry »。PR・issue の全件にも、この書簡の読みはない |
| Cryptiana（henryiii.htm、unsolved.htm 2026-10-13、ai.htm 2026-10-19、verification.htm 2026-10-15、ブログの最近50件） | henryiii.htm で « undeciphered »。ほかに言及なし |
| BravoBravoIX の2つのリポジトリ（f. 385、ff. 379–381） | ff. 218–219 は「台帳12番、not attempted、自分たちの対象ではない」とあるだけ |
| NoAutopilot/cipher-lab（ciphers/matignon-mayenne-1586、コミット検索） | fr. 15572 の Cipher-1 の作業のみ。ff. 218–219 の記述なし |
| pangoleen/cipher-readings | 該当するフォルダなし |
| Cryptoole（https://cryptoole.satoru.net/ 、API で全854件） | この書簡の項目なし |
| GitHub のリポジトリ検索、ウェブ検索 | 関係するのは上の BravoBravoIX だけ |

調べていない先：DECODE の検索画面、Lasry 氏の論文一覧。

## 人名
- Fugger 新聞の人名索引「Birago, Sagamoro † 1587」：https://fuggerzeitungen.univie.ac.at/en/personen/birago-sagamoro
