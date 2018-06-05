import unittest
from src.key import Key
from src.state import State


class TestKey(unittest.TestCase):

    def test_expanded_keys(self):
        a = '00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f'.split(' ')
        b = 'd6 aa 74 fd d2 af 72 fa da a6 78 f1 d6 ab 76 fe'.split(' ')
        c = '54 99 32 d1 f0 85 57 68 10 93 ed 9c be 2c 97 4e'.split(' ')
        self.assertEqual(Key(a).round(1), State(b))
        self.assertEqual(Key(a).round(9), State(c))

        a = '3C A1 0B 21 57 F0 19 16 90 2E 13 80 AC C1 07 BD'.split(' ')
        b = '45 64 71 B0 12 94 68 A6 82 BA 7B 26 2E 7B 7C 9B'.split(' ')
        self.assertEqual(Key(a).round(1), State(b))


if __name__ == '__main__':
    unittest.main()
