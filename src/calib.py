# 較正：当時の解読がある行で、書き起こし＋鍵から出した文字列と、当時の解読を文字の単位で突き合わせる。
# 使い方: python3 src/calib.py data/key.tsv calib/transcription_f103v_l1-6.txt calib/ref_f103v_l1-6.txt [--table-only]
# 参照の平文は、1行目から書き起こしの最後の行までに当たる当時の解読（# で始まる行は読まない）。
# 文字は小文字にし、アクセントを外し、j→i、v→u に寄せ、文字以外を除いて比べる。
import sys, re, unicodedata
from decode import load_key, load_lines, norm

def letters(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('j', 'i').replace('v', 'u')
    return re.sub(r'[^a-z?]', '', s)

def decoded_stream(lines, key):
    out = []
    for _, toks in lines:
        for t in toks:
            if t == '|':
                continue
            v = key.get(norm(t))
            out.append('?' if v is None or v == '?' else v)
    return letters(''.join(out))

def align(a, b):
    # レーベンシュタイン距離と、置換・脱落・挿入の内訳
    n, m = len(a), len(b)
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): d[i][0] = i
    for j in range(m + 1): d[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + (a[i-1] != b[j-1]))
    i, j, sub, dele, ins, ops = n, m, 0, 0, 0, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and d[i][j] == d[i-1][j-1] + (a[i-1] != b[j-1]):
            if a[i-1] != b[j-1]:
                sub += 1; ops.append((i-1, a[i-1], b[j-1]))
            i, j = i - 1, j - 1
        elif i > 0 and d[i][j] == d[i-1][j] + 1:
            dele += 1; ops.append((i-1, a[i-1], '-')); i -= 1
        else:
            ins += 1; ops.append((i, '-', b[j-1])); j -= 1
    return d[n][m], sub, dele, ins, ops[::-1]

if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if not x.startswith('--')]
    key, _ = load_key(args[0], '--table-only' in sys.argv)
    hyp = decoded_stream(load_lines(args[1]), key)
    ref = letters(''.join(l for l in open(args[2], encoding='utf-8') if not l.startswith('#')))
    dist, sub, dele, ins, ops = align(ref, hyp)
    print(f'参照の文字数 {len(ref)}、解読の文字数 {len(hyp)}')
    print(f'編集距離 {dist}（置換 {sub}、解読側の脱落 {dele}、解読側の余分 {ins}）')
    print(f'文字の一致率 1−距離/参照 = {1 - dist/len(ref):.1%}')
    print('違い（参照の位置、参照、解読）:', ' '.join(f'{p}:{r}>{h}' for p, r, h in ops))
