# 未解決の点

[English](OPEN.en.md)

## 値が分からない記号（28か所、3ページの記号2,137個のうち）
`src/decode.py` で値が付かない記号。行番号は `data/transcription_*.txt` の c 番号。

| 記号 | 回数 | 場所 | 文脈・候補 |
|---|---|---|---|
| 点つきの K | 2 | f.219r c12、c14 | l'avantaig[e] の語末、je sceu の前 |
| 15 | 1 | f.218v c13 | je ne vous diray [15] de la necessité |
| 19 | 1 | f.219r c14 | [ϕ][19] a la disposition dudict s[ieu]r du Mayne（Quant の類か） |
| 30 | 1 | f.219r c15 | il n'a [÷] … [30] encore … a sa fievre |
| 36 | 1 | f.218v c29 | est que les [36] qu'il sera tres mal aysé de recouvrer（糧食の類か） |
| 9 に点 | 1 | f.218v c05 | volée de canons pour [9] |
| 点つきの E | 1 | f.219r c12 | je sceu que [E] vous … souvent |
| 点つきの χ°、ꝛC | 1 | f.219r c01 | car les [χ°][ꝛC] de [?] qui ne sont du pais |
| ∻ | 1 | f.219r c15 | il n'a [∻] … |
| 横線つきの ℒ | 1 | f.219r c08 | gue[?]e（guerre）の中 |
| 名前を付けていない記号 | 17 | f.218r c10・c12・c21・c25・c26 など | 下の「読めない箇所」 |

## 読めない箇所・読みが割れる箇所
- f.218r 10〜12行：« par derriere [?] de [les] empescher de defendre ladicte bresche, sus qui que le par [?] pretendions [nous] loger [? ? qui ? u] sur le soir »。記号の形（gg に下線、ꞵ 形、f＋、m に下線、σσ）の読みが定まらない。
- f.218r 22行：« [?f ocaase] que par [là] n'avons peu avoir ledit logis »（« fut occasion » か）。
- f.218r 25〜26行：« des [. θ . ʃ . 9 f 3 // T 27 ɓ θ ꝓ δ] soldats »。
- f.218v 9〜10行：« ces [srge] en [?] … »。
- f.218v 21〜22行：« pas grand service [?] pour [?]hommes aprendant d'heure a aultre que le[?] resolution »。
- f.219r 1〜2・4〜5・12〜17行：上の表の記号を含む箇所と、« et seil yeront par moy »（4〜5行）、« bon[? ?]einion »（17行、bonne opinion か）。
- f.219r 11行の上に、点で挟んだ行間の書き込み（s δ a r δ n #）がある。読めていない。

## 似た形で取り違えやすい記号
- f（横線つき、s）／長い f（i）／ƒ（n）：同じ語の中でも文脈で選んだ。
- 鉤つきの ʃ の仲間：J（s）、rh（r）、Th（tout）。
- ∝（t）と、下に輪のある ∝（en）：ledict・quant・auantaige では t、qui en auoit・en garde・il y en eust では en。
- 丸い ℒ：necessaire・faire・fault では a（書き起こしでは A<）、enployer・reconois では n（Ln）。Burford 氏の鍵でも a／n の両方。
- ɍ 形：perdirent・aussy perdu では p、meilleurs・hommes では s と読むと合う。
- 4H（e）と #（r）：necessaire・medecins の e は、形が # に近いので 4H? と書いた。
- # と横線つきの tt（les）、ϖ の山2つ（il）と3つ（est）：較正で取り違えが見つかった。f. 218r の2か所は直したが、ほかにも残っている可能性がある。
- χ°（鍵では q）と、横線つきの h（鍵では armée）：較正の行では pour、tous と読むと合った。この書簡の該当箇所（f. 218v 9行の χ°、f. 219r 1行の .χ°.）は確かめ直していない。

## 2回目の書き起こし（Codex）との食い違い
- f. 218v・f. 219r は、v1 との食い違い197か所を画像で見直し、19か所を直した（`second/review_f218v_f219r.tsv`、[METHOD.md](METHOD.md) の「画像での見直し」）。直さなかった178か所の多くは、画像では見分けられない似た形（4H／#／4、fn／y2、2／J など）で、どちらが正しいかは決まっていない。
- f. 218r は見直していない。
- 見直しの後の独立の2回目（v4）との食い違いは、名前のずれを補正した後も `second/v4/diff_after_relabel.tsv` に残る。画像ではまだ見直していない。
- **χ° の記号（xo）**：直した6か所（f. 218v の 17・19（2か所）・30・32 行目、f. 219r 7行目）。鍵（友清氏の表）では q だが、文脈ではどれも pour が合う。較正の行（fr. 15573 f. 103v）でも同じ形が pour の位置に出る。この書簡では xo＝pour と読むのが自然だが、鍵は変えていない（鍵の更新は別の作業に任せた）。読み（[READING.md](READING.md)）は pour のまま。

## 人名・地名で確かめていないこと
- **Sacramore de Birague**：Fugger 新聞の人名索引に「Birago, Sagamoro † 1587」（軍人）がある（https://fuggerzeitungen.univie.ac.at/en/personen/birago-sagamoro ）。Monségur の包囲での負傷を書いた刊本は見つけていない。Burford 氏の fr. 15573 f. 385 の読みにも « sacramor[e] » が出る。
- **sieur de Saly／Saily**：f.218v で2回（綴りが違う）。人物は調べていない。
- 日付：f. 219r 下の平文の結びは « Du camp devant Monsegur ce [?] May 1586 » と読める（日の数字は読み切れていない）。署名は Matignon と読める（画像を目で見て確かめた）。
