from math import sqrt
import sys

def find_roots(a, b, c):
    """Function that takes a, b, c and returns the roots of a the polynomial ax^2 + bx + c"""
    x = (-b + sqrt(b*b - 4*a*c))/(2*a)
    y = (-b - sqrt(b*b - 4*a*c))/(2*a)
    return x, y

a, b, c = [float(x) for x in sys.argv[1:]]

r1, r2 = find_roots(a, b, c)

print(f"r1 = {r1} and r2 = {r2}")

"""
Terminal>> python quadratic_roots_cml.py 1 -5 6
r1 = 3.0 and r2 = 2.0
"""
