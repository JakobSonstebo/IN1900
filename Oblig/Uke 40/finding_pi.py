from numpy import pi, sin, cos


def newton(f, f_prime, x0, n):
    """Function that approximates the closest root from an intial guess x0 of a function given its derivative in n iterations"""
    approximations = [x0]

    xnm1 = x0
    for i in range(1, n):
        xn = xnm1 - f(xnm1) / f_prime(xnm1)
        approximations.append(xn)
        xnm1 = xn

    for n in range(len(approximations)):
        print(f'Approximation {n + 1}: {approximations[n]:<17.13f} Exact: {pi:<17.13f} Difference: {abs(pi - approximations[n]):.13e}')

newton(lambda x: sin(x), lambda x: cos(x), 3, 3)

"""
Terminal>>python finding_pi.py
Approximation 1: 3.0000000000000   Exact: 3.1415926535898   Difference: 1.4159265358979e-01
Approximation 2: 3.1425465430743   Exact: 3.1415926535898   Difference: 9.5388948448472e-04
Approximation 3: 3.1415926533005   Exact: 3.1415926535898   Difference: 2.8931612661154e-10
"""
