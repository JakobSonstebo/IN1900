from math import sqrt

def find_roots(a, b, c):
    """Function that takes as input numbers a, b, c and returns the roots of a the polynomial ax^2 + bx + c"""
    disc = b*b - 4*a*c
    if disc < 0:
        raise ValueError(f"Roots are complex, try again with different coefficients.")
    else:
        x = (-b + sqrt(b*b - 4*a*c))/(2*a)
        y = (-b - sqrt(b*b - 4*a*c))/(2*a)
    return x, y

a, b, c = [float(x) for x in input("""Please provide values for a, b, c.
(They should be entered separated by commas as follows: a, b, c)
>> """).split(", ")]


r1, r2 = find_roots(a, b, c)


print(f"Roots are: {r1} and {r2}.")

"""
Terminal>>python quadratic_roots_error2.py
Please provide values for a, b, c.
(They should be entered separated by commas as follows: a, b, c)
>> 1, 1, 1
Traceback (most recent call last):
  File "quadratic_roots_error2.py", line 18, in <module>
    r1, r2 = find_roots(a, b, c)
  File "quadratic_roots_error2.py", line 7, in find_roots
    raise ValueError(f"Roots are complex, try again with different coefficients.")
ValueError: Roots are complex, try again with different coefficients.

Terminal>>python quadratic_roots_error2.py
Please provide values for a, b, c.
(They should be entered separated by commas as follows: a, b, c)
>> 1, 0, -1
Roots are: 1.0 and -1.0.
"""
