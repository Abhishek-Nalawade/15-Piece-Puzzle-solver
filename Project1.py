import numpy as np

#defining the stack class
class queue():
    def __init__(self):
        self.pending = list()

    def add(self, child):
        self.pending.insert(0, child)

    def remove(self):
        if self.pending:
            return self.pending.pop()
        return None

    def peek(self):
        if self.pending:
            return self.pending[-1]

    def size(self):
        return len(self.pending)
