from math import sqrt, ceil
import matplotlib.pyplot as plt


class RightTriangle(object):
    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError
        else:
            self.a = a
            self.b = b
            self.h = sqrt(self.a ** 2 + self.b ** 2)

    def plot_triangle(self):
        a_co = [self.a, 0]
        b_co = [0, self.b]

        # Drawing lines from the origin with lengths a and b:
        coordinates = [a_co, b_co]
        for co in coordinates:
            plt.plot([0, co[0]], [0, co[1]], 'b')

        # Line between a_co and b_co
        plt.plot(a_co, b_co, 'b')

        # Formatting
        plt.axis('equal')
        plt.xticks(range(ceil(self.a) + 1))
        plt.yticks(range(ceil(self.b) + 1))

        # Show
        plt.show()


def test_Right_Triangle():
    success = False
    try:
        triangle3 = RightTriangle(1, -1)
    except ValueError:
        success = True
    assert success


test_Right_Triangle()

triangle1 = RightTriangle(1, 1)
triangle2 = RightTriangle(3, 4)

print(triangle1.h)
print(triangle2.h)
triangle2.plot_triangle()

"""
Terminal>>python right_triangle.py
1.4142135623730951
5.0
"""
