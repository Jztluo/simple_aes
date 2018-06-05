import unittest
from src.byte import Byte


class TestByte(unittest.TestCase):

    def test_eq(self):
        self.assertEqual(Byte('0x09'), 9)
        self.assertEqual(Byte('0x09'), Byte('9'))
        self.assertEqual(Byte('0x09'), Byte('0x09'))
        self.assertEqual(Byte('0x09'), Byte(9))

    def test_xor(self):
        self.assertEqual(Byte(10) ^ (Byte(15)), Byte(5))
        self.assertEqual(Byte(10) ^ (Byte(15)) ^ (Byte(15)), Byte(10))

    def test_setter(self):
        self.assertEqual(Byte(10).val, 10)
        with self.assertRaises(AttributeError):
            Byte(10).val = 11

    def test_sbox(self):
        self.assertEqual(Byte(0x12).sbox(), 0xC9)

        self.assertEqual(Byte(0).sbox(), 99)


if __name__ == '__main__':
    unittest.main()
