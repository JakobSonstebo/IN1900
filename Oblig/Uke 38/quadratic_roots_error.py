from math import sqrt
import sys

def find_roots(a, b, c):
    """Function that takes a, b, c and returns the roots of a the polynomial ax^2 + bx + c"""
    x = (-b + sqrt(b*b - 4*a*c))/(2*a)
    y = (-b - sqrt(b*b - 4*a*c))/(2*a)
    return x, y

coeff = ['a', 'b', 'c']                                                                         # Prepares a list coeff consisting of 3 elements

try:                                                                                            # Tries to assign the cmd-line arguments
    for i in range(len(coeff) + 1):                                                             # to the corresponding a, b, c in coeff.
        coeff[i] = float(sys.argv[i + 1])                                                       # If not enough arguments are provided, the
except IndexError:                                                                              # list index will go out of range, provoking an
    for i in range(len(coeff)):                                                                 # IndexError. The program will now check whether
        if isinstance(coeff[i], str):                                                           # a given element is still a string and prompt the user for
            coeff[i] = float(input(f"You forgot to input a value for {coeff[i]}, try again: ")) # the missing coefficient if yes.

a, b, c = coeff
r1, r2 = find_roots(a, b, c)
print(f"r1 = {r1}, r2 = {r2}")

"""
Terminal>>python quadratic_roots_error.py 1
You forgot to input a value for b, try again: -5
You forgot to input a value for c, try again: 6
r1 = 3.0, r2 = 2.0
"""
