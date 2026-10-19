# EN: Compare a second transcription (second/<version>/transcription2_*.txt) with the first (data/transcription_*.txt), page by page.
#     Usage: python3 src/compare2.py [--ver v4] [--diff] | --judge
#     v3, v4 = independent second transcriptions made after the image review (the assessment uses the lower value of the two, page by page);
#     v1, v2 = earlier runs, used in the review and kept as records. --judge prints the per-page minimum of v3 and v4.
# 2回目の書き起こし（second/<版>/）と1回目（data/）を、ページごとに記号の列として比べる。
#   v3・v4＝画像での見直しの後の独立の2回目（判定はページごとに2つの低い方で行う）。
#   v1・v2＝前の実行で、見直しに使ったので記録として残したもの。--judge で v3・v4 の低い方を出す。
#   記号名の一致率 = 1 − 編集距離 / 1回目の記号数（区切りの | は除く）
#   値の一致率     = 同じことを data/key.tsv の値に置き換えてから行う（値が同じ別名は一致とみなす。値のない記号は名前のまま）
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'src'))
from decode import load_key  # noqa: E402

PAGES = ['f218r', 'f218v', 'f219r']


def load_map():
    m = {}
    for ln in open(ROOT / 'second' / 'names_map.tsv', encoding='utf-8'):
        if ln.startswith('#') or not ln.strip():
            continue
        a, b = ln.rstrip('\n').split('\t')
        m[a] = b
    return m


def norm(tok, nmap=None):
    t = tok.lstrip('^')
    t = t.split('/')[0]
    if len(t) > 1 and t.endswith('?'):
        t = t[:-1]
    if nmap:
        t = nmap.get(t, t)
        m = re.fullmatch(r'\.(W\d+)\.', t)
        if m:
            t = nmap.get(m.group(1), t)
        if re.fullmatch(r'\d{2,}', t) and t not in ('27', '40'):
            t = '.' + t + '.'
    if t == '=si':
        t = 'cd'
    return t


def first(page):
    toks = []
    for ln in open(ROOT / 'data' / f'transcription_{page}.txt', encoding='utf-8'):
        m = re.match(r'c\d+:\s*(.*)', ln)
        if m:
            toks += [norm(t) for t in m.group(1).split() if t != '|']
    return toks


VER = 'v4'
JUDGE = ('v3', 'v4')


def second(page, nmap, ver=None):
    toks = []
    for ln in open(ROOT / 'second' / (ver or VER) / f'transcription2_{page}.txt', encoding='utf-8'):
        m = re.match(r'L\d+:\s*(.*)', ln)
        if m:
            body = re.sub(r'\?\{[^}]*\}', '?', m.group(1))
            toks += [norm(t, nmap) for t in body.split() if t not in ('|', '[plain]')]
    return toks


def edit(a, b):
    prev = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        cur = [i]
        for j, y in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (x != y)))
        prev = cur
    return prev[-1]


def relabel_map(data, min_count=5):
    # 2回目の名前ごとに、1回目で最も多く対応した名前を取る（同じ記号に別の名前を付けたずれを見るため）。
    # min_count 回以上対応したものだけを使う。
    import collections
    import difflib
    pair = collections.Counter()
    for a, b in data.values():
        for t, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            if t in ('equal', 'replace') and i2 - i1 == j2 - j1:
                for x, y in zip(a[i1:i2], b[j1:j2]):
                    pair[(y, x)] += 1
    best = {}
    for (y, x), n in pair.items():
        if n > best.get(y, (None, 0))[1]:
            best[y] = (x, n)
    return {y: x for y, (x, n) in best.items() if x != y and n >= min_count}


def judge():
    # ページごとに、独立の2回目（v3・v4）の値の一致率の低い方
    global VER
    keep, out = VER, {}
    for v in JUDGE:
        VER = v
        res, _ = compare()
        for p, r in res.items():
            a = 1 - r['value_ed'] / r['n1']
            if p not in out or a < out[p][1]:
                out[p] = (v, a)
    VER = keep
    return out


def compare():
    nmap = load_map()
    key, _ = load_key(ROOT / 'data' / 'key.tsv')

    def val(t):
        v = key.get(t)
        return t if v in (None, '?') else v

    data = {p: (first(p), second(p, nmap)) for p in PAGES}
    ren = relabel_map(data)
    res = {}
    for p, (a, b) in data.items():
        en, ev = edit(a, b), edit([val(t) for t in a], [val(t) for t in b])
        er = edit(a, [ren.get(t, t) for t in b])
        res[p] = dict(n1=len(a), n2=len(b), name_ed=en, value_ed=ev, relabel_ed=er)
    return res, ren


def residual_diff():
    # 名前のずれを補正した後に残る食い違い（ページ、1回目の位置、1回目、2回目）
    import difflib
    nmap = load_map()
    data = {p: (first(p), second(p, nmap)) for p in PAGES}
    ren = relabel_map(data)
    rows = []
    for p, (a, b) in data.items():
        b2 = [ren.get(t, t) for t in b]
        for t, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b2, autojunk=False).get_opcodes():
            if t != 'equal':
                rows.append((p, i1, ' '.join(a[i1:i2]), ' '.join(b2[j1:j2])))
    return rows


if '--ver' in sys.argv:
    VER = sys.argv[sys.argv.index('--ver') + 1]

if __name__ == '__main__' and '--judge' in sys.argv:
    for p, (v, a) in judge().items():
        print(f'{p}\tlowest value agreement {a:.1%} ({v})')
elif __name__ == '__main__' and '--diff' in sys.argv:
    print(f'# EN: Disagreements with second/{VER} left after relabelling (python3 src/compare2.py --ver {VER} --diff). page, index of the sign in the 1st transcription (from 0, dividers not counted), 1st, 2nd (relabelled). Not yet reviewed on the images.')
    print(f'# second/{VER} との、名前のずれを補正した後に残る食い違い。ページ、1回目の何番目の記号か（0から、区切りの | は数えない）、1回目、2回目（補正後）。画像ではまだ見直していない。')
    print('page\tindex\tfirst\tsecond')
    for r in residual_diff():
        print('\t'.join(map(str, r)))
elif __name__ == '__main__':
    res, ren = compare()
    tot = dict(n1=0, n2=0, name_ed=0, value_ed=0, relabel_ed=0)
    print('page\tsigns(1st)\tsigns(2nd)\tname agreement\tvalue agreement\tname agreement after relabelling')
    rows = list(res.items())
    for p, r in rows:
        for k in tot:
            tot[k] += r[k]
    for p, r in rows + [('all', tot)]:
        print(f"{p}\t{r['n1']}\t{r['n2']}\t{1 - r['name_ed'] / r['n1']:.1%} (ed {r['name_ed']})\t"
              f"{1 - r['value_ed'] / r['n1']:.1%} (ed {r['value_ed']})\t{1 - r['relabel_ed'] / r['n1']:.1%} (ed {r['relabel_ed']})")
    print('relabelling (2nd -> 1st):', ', '.join(f'{k}->{v}' for k, v in sorted(ren.items())))
