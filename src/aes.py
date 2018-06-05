from .key import Key
from .state import State

SUFFIX = 0


class AES:

    def __init__(self, key):
        self.key = Key(key)

    def encrypt(self, data):
        if bytes != type(data):
            raise AttributeError
        if 0 == len(data):
            raise AttributeError

        encrypted_bytes = bytes()

        parts = self.fix_with_suffix(self.split_bytes(data))

        for part in parts:
            state = self.key.encrypt(State(part))
            encrypted_bytes += bytes(state.to_a())

        return encrypted_bytes

    @staticmethod
    def split_bytes(data):
        return [data[i:i + 16] for i in range(0, len(data), 16)]

    @staticmethod
    def fix_with_suffix(parts):
        if len(parts[-1]) < 16:
            parts[-1] = parts[-1] + bytes([SUFFIX for i in range(0, 16 - len(parts[-1]))])
        return parts
