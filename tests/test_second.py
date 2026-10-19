# EN: Tests: the agreement figures for the second transcription in docs/METHOD.md, and second/diff_after_relabel.tsv up to date.
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))

import compare2  # noqa: E402


class TestSecond(unittest.TestCase):
    def test_figures_in_method(self):
        res, ren = compare2.compare()
        self.assertEqual({p: (r['n1'], r['n2'], r['name_ed'], r['value_ed'], r['relabel_ed']) for p, r in res.items()},
                         {'f218r': (713, 710, 166, 161, 113),
                          'f218v': (927, 934, 341, 319, 139),
                          'f219r': (499, 507, 192, 180, 116)})
        self.assertEqual(len(ren), 13)

    def test_diff_file_is_current(self):
        out = subprocess.run([sys.executable, os.path.join(ROOT, 'src', 'compare2.py'), '--diff'],
                             capture_output=True, text=True, check=True).stdout
        with open(os.path.join(ROOT, 'second', 'diff_after_relabel.tsv'), encoding='utf-8') as f:
            self.assertEqual(out, f.read())


if __name__ == '__main__':
    unittest.main()
