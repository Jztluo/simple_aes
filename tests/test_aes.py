import unittest
from src.aes import AES

from Crypto.Cipher import AES as CAES
from Crypto.Random import get_random_bytes
from binascii import b2a_hex, a2b_hex


class TestAes(unittest.TestCase):

    def test_encrypt_16str(self):
        key = '0000000000000000'
        text = "1234000000000000"
        key_bytes = key.encode('utf-8')
        text_bytes = text.encode('utf-8')

        encrypted = AES(key_bytes).encrypt(text_bytes)
        encrypted_text = b2a_hex(encrypted).decode('utf-8')
        self.assertEqual(encrypted_text, '9c7e62e8a3f02bd9df375a09950957fb')

        cipher = CAES.new(key_bytes, CAES.MODE_ECB)
        raw_text = cipher.decrypt(a2b_hex(encrypted_text.encode('utf-8'))).decode('utf-8')
        self.assertEqual(raw_text, text)

    def test_encrypt_text(self):
        key = get_random_bytes(16)
        text = 'Launching unittests with arguments python -m unittest test_aes.TestAes.test_encrypt'
        text_bytes = text.encode('utf-8')
        encrypted = AES(key).encrypt(text_bytes)
        encrypted_text = b2a_hex(encrypted).decode('utf-8')
        cipher = CAES.new(key, CAES.MODE_ECB)
        decrypted_bytes = cipher.decrypt(a2b_hex(encrypted_text.encode('utf-8'))).split(b'\0', 1)[0]
        raw_text = decrypted_bytes.decode('utf-8')
        self.assertEqual(text, raw_text)

    def test_encrypt_random_bytes(self):
        for i in range(20):
            key = get_random_bytes(16)
            text = get_random_bytes(100000).split(b'\0', 1)[0]
            if len(text) == 0:
                continue
            encrypted = AES(key).encrypt(text)
            cipher = CAES.new(key, CAES.MODE_ECB)
            raw = cipher.decrypt(encrypted).split(b'\0', 1)[0]
            self.assertEqual(len(text), len(raw))
            self.assertEqual(text, raw)


if __name__ == '__main__':
    unittest.main()
