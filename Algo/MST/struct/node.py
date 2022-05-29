# Fibonacci Heap Node
import math


class Node:
    def __init__(self, key):
        self.key = key
        self.child = None
        self.parent = None
        self.left = self
        self.right = self
        self.mark = False
        self.degree = 0

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __eq__(self, other):
        return self.key == other.key

    def __le__(self, other):
        return self.key <= other.key

    def __ge__(self, other):
        return self.key >= other.key

    def __ne__(self, other):
        return self.key != other.key

    def __add__(self, other):
        return self.key + other.key

    def __sub__(self, other):
        return self.key - other.key

    def __mul__(self, other):
        return self.key * other.key

    def __truediv__(self, other):
        return self.key / other.key

    def __floordiv__(self, other):
        return self.key // other.key

    def __mod__(self, other):
        return self.key % other.key

    def __pow__(self, other):
        return self.key ** other.key

    def __and__(self, other):
        return self.key & other.key

    def __or__(self, other):
        return self.key | other.key

    def __xor__(self, other):
        return self.key ^ other.key

    def __lshift__(self, other):
        return self.key << other.key

    def __rshift__(self, other):
        return self.key >> other.key

    def __neg__(self):
        return -self.key

    def __pos__(self):
        return +self.key

    def __invert__(self):
        return ~self.key

    def __abs__(self):
        return abs(self.key)

    def __int__(self):
        return int(self.key)

    def __float__(self):
        return float(self.key)

    def __complex__(self):
        return complex(self.key)

    def __round__(self):
        return round(self.key)

    def __floor__(self):
        return math.floor(self.key)

    def __ceil__(self):
        return math.ceil(self.key)

    def __trunc__(self):
        return math.trunc(self.key)

    def __index__(self):
        return self.key.__index__()

    def __len__(self):
        return len(self.key)

    def __contains__(self, item):
        return item in self.key

    def __getitem__(self, key):
        return self.key[key]

    def __setitem__(self, key, value):
        self.key[key] = value

    def __delitem__(self, key):
        del self.key[key]

    def __iter__(self):
        return iter(self.key)

    def __reversed__(self):
        return reversed(self.key)

    def __getattr__(self, name):
        return getattr(self.key, name)

    def __call__(self, *args, **kwargs):
        return self.key(*args, **kwargs)