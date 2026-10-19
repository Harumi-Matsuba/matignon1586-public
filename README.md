# Matignon から国王への暗号書簡（Monségur の前の陣、1586年5月）の第一の読み

[English README](README.en.md)

| | |
|---|---|
| 版 | **v0.1**（2026-10-20） |
| 状態 | **部分的な読み**（3ページの大半が文として通るが、値の分からない記号28か所と読めない箇所がある） |
| 先行との関係 | 先行の読みは見つかっていない（友清氏は undeciphered、Bourdeau 氏の台帳は never attempted）。表は友清氏の復元、推定した値の一部は Burford 氏の鍵と一致（下の「先行研究の成果」） |
| 人の確認 | **人は書き起こしを確かめていない。** 書き起こしは2回とも AI（1回目 Claude、2回目 Codex）によるもの。AI どうしの一致は、人の確認の代わりにならない |
| 数字 | 対照：鍵をかき混ぜた1000回で本物以上は3ページとも0回／較正：当時の解読がある6行で文字の一致率74.8%／2回目の書き起こし（Codex、1回目を見せずに）との記号名の一致率67.3%（同じ記号に別の名前を付けたずれを補正すると82.8%）。詳しくは [docs/METHOD.md](docs/METHOD.md) |
| AI の使用 | 書き起こし・鍵の補い・解読・スクリプト・文書は Claude（Claude Opus 5.5）、2回目の書き起こしは OpenAI Codex。人は対象の選定・画像の保存・公開の判断（下の「AI の使用」） |

フランス国立図書館 BnF fr. 15572 ff. 218r–219r にある、Matignon 元帥（Jacques de Goyon de Matignon）から国王アンリ3世への書簡の暗号部分を、友清理士氏が復元した Mayenne–Forget の Cipher-2 で読んだ記録です。

- 資料：BnF Français 15572、Gallica ark:/12148/btv1b9061879d の225コマ（f. 218r）と226コマ（f. 218v–219r）。f. 218r は平文の後に暗号26行、f. 218v は全面が暗号34行、f. 219r は暗号19行の後に平文の結びと署名。
- 結び：« Du camp devant Monsegur ce [?] May 1586 »、署名 Matignon（画像で確かめた）。
- 先行：友清理士氏は ff. 218–219 を Cipher-2 の書簡として挙げ、「undeciphered」としている（[Cryptiana](https://cryptiana.web.fc2.com/code/henryiii.htm)）。D. Bourdeau 氏の台帳（cyphersolver）の12番も「never attempted」（2026-10-18 の版）。2026-10-19〜20 に調べた範囲では、この書簡の読みは見つかっていない（調べた先は [SOURCES.md](SOURCES.md)）。

## 現状（v0.1、部分的）
| ページ | 記号の数 | 表の記号だけで値が付いた割合 | 推定も合わせた割合 | 鍵をかき混ぜた対照（1000回）で本物以上 |
|---|---|---|---|---|
| f. 218r | 713 | 92.1% | 98.7% | 0回 |
| f. 218v | 927 | 90.4% | 99.5% | 0回 |
| f. 219r | 499 | 89.8% | 97.4% | 0回 |

- 3ページとも、大半がフランス語の文として通ります（[docs/READING.md](docs/READING.md)）。値の分からない記号は28か所、読めない短い箇所が数か所あります（[docs/OPEN.md](docs/OPEN.md)）。
- **較正**：同じ暗号で当時の解読がある書簡（fr. 15573 f. 103v）の6行を、答えを見ずに同じ方法で読むと、当時の解読との文字の一致率は74.8%でした（[docs/METHOD.md](docs/METHOD.md) の「較正」）。この読みも、細部には誤りを含みうる前提で使ってください。

## 内容（要約）
- 夜明けから日没までの砲撃（約1200発）は、城壁が予想より堅く、効果が小さかった。三つのブレッシュを開けた。
- 夕方、Sacramore de Birague がブレッシュの側から陣地を取りに行き、重傷を負って退いた。陣地は取れなかった。
- 以後は砲撃を控え、陣地を取って一歩ずつ進む方針。軍は疲れており、救援と給料の支払いがいちばん大事だと訴える。
- Mayenne 公は熱を出しているが、命の危険はない。

詳しくは [docs/READING.md](docs/READING.md)。

## 先行研究の成果と、この読みで加えたこと
**前提にしたもの**
- Cipher-2 の表：友清理士氏の復元（[henryiii_MayenneForget2.png](https://cryptiana.web.fc2.com/code/henryiii_MayenneForget2.png)）。表の画像はこのリポジトリに含めていません。
- この書簡が Cipher-2 で、未解読であること：友清理士氏、D. Bourdeau 氏。

**この読みで加えたこと**
1. 3ページの記号を、記号名で行ごとに書き起こした（`data/transcription_*.txt`）。
2. 表にない記号の値を、この書簡の文脈から補った（27＝d、17＝tant、Ꝭ 形＝tout、gg に下線＝par など。`data/key.tsv` の inferred）。うち10個は、Brett Burford 氏が fr. 15573 の別の書簡で当時の解読と照らして作った鍵と一致する。ただし、多くは同氏の鍵を見た後に確かめたもの（[docs/METHOD.md](docs/METHOD.md)）。
3. 書簡の内容（Monségur の包囲、Sacramore de Birague の負傷、軍の窮状、Mayenne の病気）。

## 使い方
```
python3 src/decode.py data/key.tsv data/transcription_f218r.txt               # 推定も使う
python3 src/decode.py data/key.tsv data/transcription_f218r.txt --table-only  # 表の記号だけ
python3 src/control.py data/key.tsv data/transcription_f218r.txt 1000         # 対照実験（wordfreq が必要）
python3 -m unittest discover -s tests
```

## AI の使用
書き起こし・鍵の補い・解読・スクリプト・文書は、Anthropic の Claude（Claude Code、Claude Opus 5.5）が行いました。対象の選定、画像の保存、公開の判断は人が行いました。2回目の書き起こしは、OpenAI の Codex（codex-cli 0.163.0-alpha.10.2、既定のモデル）に、1回目・鍵・値を見せずに行わせました。人は書き起こしを確かめていません。詳しくは [docs/METHOD.md](docs/METHOD.md)。

## ファイル
| 場所 | 中身 |
|---|---|
| data/transcription_f218r.txt ほか | 記号名での書き起こし（行ごと） |
| data/key.tsv | 記号名→値。出典を table（友清氏の表）・inferred（推定）・unknown で区別 |
| data/decoded_*.txt | `src/decode.py` の出力 |
| docs/READING.md | 読み（句読点を補ったもの）と要約 |
| docs/METHOD.md | 方法、数字、AI の使用、限界 |
| docs/OPEN.md | 値の分からない記号、読めない箇所、確かめていないこと |
| second/、src/compare2.py | 2回目の書き起こし（Codex）、依頼文、実行記録、1回目との突き合わせ |
| CITATION.cff | 引用の情報（版・日付） |
| calib/、src/calib.py | 較正（fr. 15573 f. 103v の6行）の書き起こし・参照・突き合わせ |
| SOURCES.md | 出典と、先行の確かめ |

どの文書にも英語版があります（ファイル名に `.en` が付いたもの。例：docs/METHOD.en.md）。data/key.tsv には英語の説明の列があります。

ライセンス：コードは MIT、自作の文書とデータは CC BY 4.0（[LICENSE](LICENSE)）。
