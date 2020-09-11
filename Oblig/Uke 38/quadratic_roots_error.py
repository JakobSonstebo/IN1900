from math import sqrt
import sys

def find_roots(a, b, c):
    x = (-b + sqrt(b*b - 4*a*c))/(2*a)
    y = (-b - sqrt(b*b - 4*a*c))/(2*a)
    return x, y

try:
    a, b, c = [float(x) for x in sys.argv[1:]]
except:
    a, b, c = [float(x) for x in input("You forgot to input all of the values, try again: ").split()]

r1, r2 = find_roots(a, b, c)
print(f"Roots are: {r1} and {r2}")
