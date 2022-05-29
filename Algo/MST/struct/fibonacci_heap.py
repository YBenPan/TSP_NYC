# Fibonacci Heap Implementation
from node import Node


class FibonacciHeap:
    # Constructor
    def __init__(self):
        self.min = None
        self.n = 0

    # Insert method
    def insert(self, node):
        node.left = node
        node.right = node
        node.degree = 0
        node.mark = False
        self.link(node)
        if self.min is None:
            self.min = node
        elif node.key < self.min.key:
            self.min = node

    # Link method
    def link(self, y):
        x = self.min
        if x is None:
            self.min = y
        elif x.key > y.key:
            self.min = y
            x, y = y, x
        y.left = y.left.right = y
        y.parent = x
        y.mark = False
        x.degree += 1
        y.child = x.child if x.child is not None else y
        x.child = y

    # Cascading Cut method
    def cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if y.mark is False:
                y.mark = True
            else:
                self.cut(y, z)
                self.cascading_cut(z)

    # Cut method
    def cut(self, x, y):
        x.left.right = x.right
        x.right.left = x.left
        y.degree -= 1
        if y.child is x:
            y.child = x.right if x.right is not x else None
        if y.degree == 0:
            y.child = None
        x.left = x
        x.right = x
        x.parent = None
        x.mark = False
        self.link(y)

    # Decrease Key method
    def decrease_key(self, x, k):
        if k > x.key:
            return
        x.key = k
        y = x.parent
        if y is not None and x.key < y.key:
            self.cut(x, y)
            self.cascading_cut(y)
        if x.key < self.min.key:
            self.min = x

    # Extract Minimum method
    def extract_min(self):
        z = self.min
        if z is not None:
            if z.child is not None:
                x = z.child
                y = x.right
                x.left = x.right = x
                self.min = x
                self.consolidate()
                self.min = self.meld(self.min, y)
            self.min = z.right if z.right is not z else None
            z.left.right = z.right
            z.right.left = z.left
        return z

    # Consolidate method
    def consolidate(self):
        A = [None] * self.n
        w = self.min
        while w is not None:
            x = w
            d = x.degree
            while A[d] is not None:
                y = A[d]
                if x.key > y.key:
                    x, y = y, x
                self.link(y)
                A[d] = None
                d += 1
            A[d] = x
            w = w.right
            w = self.min if w is x else w
            d += 1

    # Meld method
    def meld(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1
        if h1.key > h2.key:
            h1, h2 = h2, h1
        h1.right.left = h1.left
        h1.left.right = h1.right
        h1.left = h1.right = h1
        self.link(h2)
        if h1.key < self.min.key:
            self.min = h1
        return h1

    # Delete method
    def delete(self, x):
        self.decrease_key(x, float("-inf"))
        self.extract_min()

    # Empty method
    def empty(self):
        return self.min is None

    # Size method
    def size(self):
        return self.n

    # Print method
    def print(self):
        w = self.min
        while w is not None:
            print(w.key)
            w = w.right
            w = self.min if w is x else w

# Test
if __name__ == "__main__":
    fh = FibonacciHeap()
    # Create nodes
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    # Insert nodes
    fh.insert(n1)
    fh.insert(n2)
    fh.insert(n3)
    fh.insert(n4)
    fh.insert(n5)