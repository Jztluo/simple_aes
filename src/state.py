from .byte import Byte, mb2, mb3


def is_acceptable_matrix(matrix):
    if list != type(matrix):
        return False
    if 4 != len(matrix):
        return False
    for l in matrix:
        if list != type(l):
            return False
        if 4 != len(l):
            return False
    return True


def is_acceptable_array(array):
    t = type(array)
    if (t != list) and (t != bytes):
        return False
    if 16 != len(array):
        return False
    return True


def empty_matrix(dimension=4, default=0):
    return [[default for i in range(dimension)] for i in range(dimension)]


def mix_column(column):
    b0, b1, b2, b3 = column
    d0 = mb2(b0) ^ mb3(b1) ^ b2 ^ b3
    d1 = b0 ^ mb2(b1) ^ mb3(b2) ^ b3
    d2 = b0 ^ b1 ^ mb2(b2) ^ mb3(b3)
    d3 = mb3(b0) ^ b1 ^ b2 ^ mb2(b3)
    return [d0, d1, d2, d3]


class State:

    def __init__(self, matrix):
        tmp = empty_matrix()
        if is_acceptable_array(matrix):
            for n in range(0, 16):
                i = int(n / 4)
                j = n % 4
                tmp[j][i] = Byte(matrix[n])

        elif is_acceptable_matrix(matrix):
            for i in range(0, 4):
                for j in range(0, 4):
                    tmp[i][j] = Byte(matrix[i][j])

        else:
            raise AttributeError("bytes length must be 16, (%d bytes)" % len(array))

        self.__matrix = tmp

    def __eq__(self, other):
        if State != type(other):
            return False
        return self.matrix == other.matrix

    def __repr__(self):
        return '<State: %s>' % self.__matrix

    def sub_bytes(self):
        return self.map(lambda i, j: self.matrix[i][j].sbox())

    def shift_rows(self):
        return self.map(lambda i, j: self.matrix[i][(j + i) % 4])

    def mix_columns(self):
        tmp = empty_matrix()
        for j in range(0, 4):
            column = [self.matrix[i][j] for i in range(0, 4)]
            mixed = mix_column(column)
            for i in range(0, 4):
                tmp[i][j] = mixed[i]
        return State(tmp)

    def map(self, func):
        tmp = empty_matrix()
        for i in range(0, 4):
            for j in range(0, 4):
                tmp[i][j] = func(i, j)

        return State(tmp)

    def __getitem__(self, index):
        return self.__matrix[index][:]

    @property
    def matrix(self):
        return self.__matrix

    def add_round_key(self, key):
        return self.map(lambda i, j: self.matrix[i][j] ^ key[i][j])

    def reverse(self):
        return self.map(lambda i, j: self.matrix[j][i])

    def to_a(self):
        tmp = []
        for i in range(0, 4):
            for j in range(0, 4):
                tmp.append(self.matrix[j][i].val)
        return tmp

    def to_h(self):
        tmp = []
        for i in range(0, 4):
            for j in range(0, 4):
                tmp.append(hex(self.matrix[j][i].val))
        return tmp

