import math

class Vector:
    def __init__(self, components):
        if not isinstance(components, list) or len(components) == 0:
            raise ValueError("Components must be a non-empty list")
        for c in components:
            if not isinstance(c, (int, float)):
                raise ValueError("Components must be a list of numbers")
        self.components = components

    def add(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Cannot add vectors with different lengths")
        return Vector([self_c + other_c for self_c, other_c in zip(self.components, other.components)])

    def subtract(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Cannot subtract vectors with different lengths")
        return Vector([self_c - other_c for self_c, other_c in zip(self.components, other.components)])

    def dot(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Cannot compute dot product of vectors with different lengths")
        return sum(self_c * other_c for self_c, other_c in zip(self.components, other.components))

    def norm(self):
        return math.sqrt(sum(c**2 for c in self.components))

    def toString(self):
        return "({})".format(",".join(str(c) for c in self.components))

    def __str__(self):
        return self.toString()

    def equals(self, other):
        if not isinstance(other, Vector):
            return False
        if len(self.components) != len(other.components):
            return False
        return all(self_c == other_c for self_c, other_c in zip(self.components, other.components)) or \
               all(self_c == other_c for self_c, other_c in zip(map(str, self.components), map(str, other.components)))

def strip(s):
    return ''.join(filter(None, s.split()))
