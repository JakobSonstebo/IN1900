import numpy as np
import matplotlib.pyplot as plt


class Diff(object):
    def __init__(self, function):
        self.f = function

    def diff1(self, x, h):
        return (self.f(x + h) - self.f(x))/h

    def diff2(self, x, h):
        return (self.f(x + h) - self.f(x - h))/(2*h)

    def diff3(self, x, h):
        return (-self.f(x + 2*h) + 8*self.f(x + h) - 8*self.f(x - h) + self.f(x - 2*h))/(12*h)


def y_diff_exact(x):
    return 2*np.pi*np.cos(2*np.pi*x)


y_diff = Diff(lambda x: np.sin(2*np.pi * x))

# Plot
x_values = np.linspace(-1, 1, 1000)
h_values = [0.9, 0.6, 0.3, 0.1]

for h in h_values:
    plt.plot(x_values, y_diff_exact(x_values), label=f'exact derivative')
    plt.plot(x_values, y_diff.diff1(x_values, h), label=f'diff 1, h = {h}')
    plt.plot(x_values, y_diff.diff2(x_values, h), label=f'diff 2, h = {h}')
    plt.plot(x_values, y_diff.diff3(x_values, h), label=f'diff 3, h = {h}')
    plt.legend()
    plt.show()

"""
Terminal>>python class_diff.py
"""


