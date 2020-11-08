from math import sqrt


class Coords(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x:.2f}, {self.y:.2f}, {self.z:.2f})'

    def __len__(self):
        return 3

    def __abs__(self):
        return round(sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2), 2)

    def __add__(self, other):
        return Coords(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Coords(self.x - other.x, self.y - other.y, self.z - other.z)


# Oppgave a
sqrt3 = sqrt(3)
close = Coords(1 / sqrt3, 1 / sqrt3, 1 / sqrt3)
far = Coords(3 / sqrt3, 15 / sqrt3, 21 / sqrt3)

print(close)
print(far)

# Oppgave b
print(f'The class represents coordinates in {len(close)} dimensions')
print(f'The distance from the center to the point close is {abs(close):.2f}')
print(f'The distance from the center to the point far is {abs(far):.2f}')

# Oppgave c
further = close + far
print(f'The coordinates further are at {further}')

distance = abs(far - close)
print(f'The distance from far to close is {distance}')

center = further - further
print(f'The coordinates at the center are {center}')

"""
Terminal>>python Coords.py
(0.58, 0.58, 0.58)
(1.73, 8.66, 12.12)
The class represents coordinates in 3 dimensions
The distance from the center to the point close is 1.00
The distance from the center to the point far is 15.00
The coordinates further are at (2.31, 9.24, 12.70)
The distance from far to close is 14.14
The coordinates at the center are (0.00, 0.00, 0.00)

"""