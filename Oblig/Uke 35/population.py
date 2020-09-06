import math


B = 50000
k = 0.2     # h^-1
N0 = 5000

C = B/N0 - 1


def N(t):
    return B/(1 + C*math.exp(-k*t))


print(round(N(24)))
