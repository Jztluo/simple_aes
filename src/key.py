from .state import State
from .byte import rcon, sbox


def xor(vector1, vector2):
    return [vector1[i] ^ vector2[i] for i in range(len(vector1))]


def rotate(ary, n=1):
    return ary[n - len(ary):] + ary[:n - len(ary)]


def column_of(matrix, index):
    return [matrix[i][index] for i in range(4)]


class Key(State):

    def __init__(self, key):
        super(Key, self).__init__(key)
        self.cache = {}

    def round(self, turn):
        key = self.cache.get(turn)
        if key:
            return key
        else:
            key = self.expand_key(turn)
            self.cache[turn] = key
            return key

    def expand_key(self, turn):
        if turn == 0:
            return self.first_round()
        last_round = self.round(turn - 1)
        k0 = xor(column_of(last_round, 0), self.generate_k0(column_of(last_round, 3), turn))  # 243 107 111 123
        k1 = xor(column_of(last_round, 1), k0)
        k2 = xor(column_of(last_round, 2), k1)
        k3 = xor(column_of(last_round, 3), k2)
        key = State([k0, k1, k2, k3]).reverse()
        return key

    @staticmethod
    def generate_k0(last_k3, turn):
        key = [sbox(e) for e in rotate(last_k3)]
        return xor(key, rcon(turn))

    def first_round(self):
        return State(self.matrix)

    def encrypt(self, state):
        state = state.add_round_key(self.round(0))
        for turn in range(1, 10):
            state = state.sub_bytes().shift_rows().mix_columns().add_round_key(self.round(turn))
        return state.sub_bytes().shift_rows().add_round_key(self.round(10))
