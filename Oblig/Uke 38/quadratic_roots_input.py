from math import sqrt

def find_roots(a, b, c):
    """Function that takes a, b, c and returns the roots of a the polynomial ax^2 + bx + c"""
    x = (-b + sqrt(b*b - 4*a*c))/(2*a)
    y = (-b - sqrt(b*b - 4*a*c))/(2*a)
    return x, y

a, b, c = [float(x) for x in input("""Please provide values for a, b, c.
(They should be entered separated by commas as follows: a, b, c)
>> """).split(", ")]

r1, r2 = find_roots(a, b, c)

print(f"r1 = {r1} and r2 = {r2}.")

"""
Terminal>> python quadratic_roots_input.py
Please provide values for a, b, c.
(They should be entered separated by commas as follows: a, b, c)
>> 1, -5, 6
r1 = 3.0 and r2 = 2.0.
"""
