from .lookup_tables import MULTIPLY_BY_2, MULTIPLY_BY_3, RCON, SBOX


def value_of(obj):
    if Byte == type(obj):
        return obj.val

    if str == type(obj):
        return int(obj, 0) if obj.startswith('0x') else int(obj, 16)

    if int == type(obj):
        return obj


def mb2(val):
    return Byte(MULTIPLY_BY_2[val])


def mb3(val):
    return Byte(MULTIPLY_BY_3[val])


def sbox(val):
    return Byte(SBOX[val])


def rcon(val):
    return [Byte(RCON[val]), Byte(0), Byte(0), Byte(0)]


class Byte:

    def __init__(self, val):
        if val is None:
            raise AttributeError
        self.__val = value_of(val)

    def __repr__(self):
        return '<Byte: %s>' % hex(self.__val)

    def __eq__(self, other):
        return self.__val == value_of(other)

    def __xor__(self, other):
        return Byte(self.__val ^ value_of(other))

    def sbox(self):
        return sbox(self.__val)

    @property
    def val(self):
        return self.__val

    def __index__(self):
        return self.val
