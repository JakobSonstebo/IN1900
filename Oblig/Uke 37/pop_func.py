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
