from simple_ODE_function import ForwardEuler
import numpy as np
import matplotlib.pyplot as plt


def f(x, t):
    return np.cos(6*t)/(1 + t + x)


for n in [20, 30, 35, 40, 50, 100, 1000, 10000]:
    t_sol, x_sol = ForwardEuler(f, 0, 10, n)
    plt.plot(t_sol, x_sol, label = f'n = {n}')

plt.legend()
plt.show()

"""
Terminal>>python decrease_dt.py
"""