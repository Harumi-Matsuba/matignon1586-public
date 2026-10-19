# EN: Tests: key sources, the --table-only switch, data/decoded_*.txt up to date, and known words present.
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))

from decode import load_key, load_lines, decode  # noqa: E402

PAGES = ['f218r', 'f218v', 'f219r']


class TestDecode(unittest.TestCase):
    def setUp(self):
        self.key, self.src = load_key(os.path.join(ROOT, 'data', 'key.tsv'))

    def test_key_sources(self):
        # 出典は table・inferred・unknown のどれか
        self.assertTrue(set(self.src.values()) <= {'table', 'inferred', 'unknown'})

    def test_table_only_drops_inferred(self):
        key_t, _ = load_key(os.path.join(ROOT, 'data', 'key.tsv'), table_only=True)
        self.assertNotIn('27', key_t)
        self.assertEqual(key_t['9'], 'd')

    def test_decoded_files_are_current(self):
        # data/decoded_*.txt が、いまの鍵と書き起こしから作り直したものと一致する
        for p in PAGES:
            out = subprocess.run(
                [sys.executable, os.path.join(ROOT, 'src', 'decode.py'),
                 os.path.join(ROOT, 'data', 'key.tsv'),
                 os.path.join(ROOT, 'data', f'transcription_{p}.txt')],
                capture_output=True, text=True, check=True).stdout
            with open(os.path.join(ROOT, 'data', f'decoded_{p}.txt'), encoding='utf-8') as f:
                self.assertEqual(out, f.read(), p)

    def test_known_words(self):
        # 文脈で確かめた語が出ること（鍵の取り違えの検出用）
        lines = load_lines(os.path.join(ROOT, 'data', 'transcription_f218r.txt'))
        text = ' '.join(s for _, s in decode(lines, self.key))
        for w in ['sacramore', 'birague', 'bresche', 'muraile', 'soldats']:
            self.assertIn(w, text)


if __name__ == '__main__':
    unittest.main()
