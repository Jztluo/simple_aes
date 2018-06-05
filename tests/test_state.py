import unittest
from src.byte import Byte
from src.state import State


class TestState(unittest.TestCase):

    def test_eq(self):
        a = [1, 2, 3, 4 ,5, 6, 7, 8,9, 10, 11, 12, 13, 14, 15, 16]
        b = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', '10']
        c = [int(s, 16) for s in b]
        self.assertEqual(State(a), State(c))
        self.assertEqual(State(a), State(b))

    def test_sub_stypes(self):
        a = [[0x12, 0x24, 0x48, 0x81] for i in range(4)]
        b = [[0xC9, 0x36, 0x52, 0xC] for i in range(4)]
        self.assertEqual(State(a).sub_bytes(), State(b))

    def test_shift_rows(self):
        a = [[0x0f, 0x15, 0x71, 0xc9], [0x47, 0xd9, 0xe8, 0x59], [0x0c, 0xb7, 0xad, 0xd6], [0xaf, 0x7f, 0x67, 0x98]]
        b = [[0x0f, 0x15, 0x71, 0xc9], [0xd9, 0xe8, 0x59, 0x47], [0xad, 0xd6, 0x0c, 0xb7], [0x98, 0xaf, 0x7f, 0x67]]
        s = State(a)
        s = s.shift_rows()
        self.assertNotEqual(s, State(a))
        self.assertEqual(s, State(b))
        s = s.shift_rows().shift_rows().shift_rows()
        self.assertEqual(s, State(a))

    def test_mix_columns(self):
        a = [[118, 160, 254, 121], [53, 169, 210, 89], [149, 133, 163, 155], [70, 221, 203, 246]]
        b = [[96, 227, 226, 116], [254, 160, 116, 139], [184, 100, 55, 12], [182, 118, 229, 190]]
        self.assertEqual(State(a).mix_columns(), State(b))

    def test_shift_rows2(self):
        a = [[0x01, 0x02, 0x03, 0x04], [0x05, 0x06, 0x07, 0x08], [0x09, 0x0a, 0x0b, 0x0c], [0x0d, 0x0e, 0x0f, 0x10]]
        b = [[0x01, 0x02, 0x03, 0x04], [0x06, 0x07, 0x08, 0x05], [0x0b, 0x0c, 0x09, 0x0a], [0x10, 0x0d, 0x0e, 0x0f]]
        s = State(a)
        s = s.shift_rows()
        self.assertEqual(s, State(b))

    def test_shift_rows2(self):
        a = ['0xb1', '0x33', '0xb1', '0x33', '0x5b', '0x85', '0x5b', '0x85', '0x5b', '0x85', '0x5b', '0x85', '0x5b', '0x85', '0x5b', '0x85']
        b = [[0x01, 0x02, 0x03, 0x04], [0x06, 0x07, 0x08, 0x05], [0x0b, 0x0c, 0x09, 0x0a], [0x10, 0x0d, 0x0e, 0x0f]]
        s = State(a)
        s = s.shift_rows()
        self.assertEqual(s, State(b))

if __name__ == '__main__':
    unittest.main()
