# EN: Tests: the agreement figures of the second transcriptions in docs/METHOD.md (v1-v4), the assessment figures (lower of v3 and v4), the review list, and second/v4/diff_after_relabel.tsv up to date.
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))

import compare2  # noqa: E402

# 版ごと：ページ → （1回目の記号数, 2回目の記号数, 記号名の編集距離, 値の編集距離）
FIGURES = {
    'v1': {'f218r': (713, 710, 166, 161), 'f218v': (926, 934, 331, 312), 'f219r': (498, 507, 187, 176)},
    'v2': {'f218r': (713, 709, 183, 175), 'f218v': (926, 933, 154, 131), 'f219r': (498, 498, 90, 76)},
    'v3': {'f218r': (713, 708, 124, 116), 'f218v': (926, 930, 158, 132), 'f219r': (498, 508, 111, 91)},
    'v4': {'f218r': (713, 708, 224, 199), 'f218v': (926, 934, 191, 162), 'f219r': (498, 498, 145, 130)},
}


class TestSecond(unittest.TestCase):
    def test_figures_in_method(self):
        keep = compare2.VER
        try:
            for ver, want in FIGURES.items():
                compare2.VER = ver
                res, _ = compare2.compare()
                got = {p: (r['n1'], r['n2'], r['name_ed'], r['value_ed']) for p, r in res.items()}
                self.assertEqual(got, want, ver)
        finally:
            compare2.VER = keep

    def test_assessment(self):
        j = compare2.judge()
        self.assertEqual({p: (v, round(a * 1000)) for p, (v, a) in j.items()},
                         {'f218r': ('v4', 721), 'f218v': ('v4', 825), 'f219r': ('v4', 739)})
        self.assertTrue(all(a >= 0.70 for _, a in j.values()))

    def test_review_counts(self):
        rows = [ln.split('\t') for ln in open(os.path.join(ROOT, 'second', 'review_f218v_f219r.tsv'), encoding='utf-8')
                if not ln.startswith('#') and not ln.startswith('page')]
        self.assertEqual(sum(r[4].startswith('直した') for r in rows), 19)
        self.assertEqual(sum(r[4].startswith('直さない') for r in rows), 178)

    def test_diff_file_is_current(self):
        out = subprocess.run([sys.executable, os.path.join(ROOT, 'src', 'compare2.py'), '--ver', 'v4', '--diff'],
                             capture_output=True, text=True, check=True).stdout
        with open(os.path.join(ROOT, 'second', 'v4', 'diff_after_relabel.tsv'), encoding='utf-8') as f:
            self.assertEqual(out, f.read())


if __name__ == '__main__':
    unittest.main()
