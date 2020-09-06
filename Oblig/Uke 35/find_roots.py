from math import sqrt


def find_roots(a, b, c):
    x = (-b + sqrt(b*b - 4*a*c))/(2*a)
    y = (-b - sqrt(b*b - 4*a*c))/(2*a)
    return x, y


x1, x2 = find_roots(6, -5, 1)

print(f"{x1:.2f}, {x2:.2f}")
