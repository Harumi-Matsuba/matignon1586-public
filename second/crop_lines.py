import sys, numpy as np
from PIL import Image
src, out, pre = sys.argv[1:4]; TH = float(sys.argv[4]) if len(sys.argv) > 4 else 0.25
c = Image.open(src).convert('L'); arr = np.asarray(c, dtype=float)
ink = (arr < 120).sum(1).astype(float)
sm = np.convolve(ink, np.ones(31)/31, mode='same')
pk = [i for i in range(46, len(sm)-46) if sm[i] == sm[i-45:i+46].max() and sm[i] > sm.max()*TH]
pk2 = []
for p in pk:
    if not pk2 or p-pk2[-1] > 40: pk2.append(p)
W = c.size[0]
for k, p in enumerate(pk2, 1):
    y0, y1 = max(0, p-95), min(c.size[1], p+85)
    band = arr[y0:y1]
    col = (band < 120).sum(0)
    mid = W//2; lo, hi = int(W*0.42), int(W*0.58)
    cut = lo + int(np.argmin(np.convolve(col[lo:hi], np.ones(15), mode='same')))
    for j, (a, b) in enumerate([(0, cut), (cut, W)]):
        cc = c.crop((a, y0, b, y1))
        cc = cc.resize((int(cc.size[0]*1.0), cc.size[1]))
        cc.save(f'{out}/{pre}_L{k:02d}{"ab"[j]}.jpg', quality=90)
print(pre, len(pk2))
