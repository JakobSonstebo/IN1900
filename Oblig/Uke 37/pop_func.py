from math import exp


def population(t, k, B, C):
    return B/(1 + C*exp(-k*t))


time = [48/12 * i for i in range(13)]
pop = [population(t, 0.2, 50000, 9.0) for t in time]

h1 = "Times (hours)"
h2 = "Population"
print(f"{h1:<15} {h2:<10}")

for t, p in zip(time, pop):
    print(f'{round(t):<15} {round(p):<10}')

"""
Terminal >> python pop_func.py
Times (hours)   Population
0               5000
4               9913
8               17749
12              27526
16              36580
20              42924
24              46552
28              48390
32              49263
36              49666
40              49849
44              49932
48              49970
"""
