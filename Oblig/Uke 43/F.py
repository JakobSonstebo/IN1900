from numpy import sin, cos, linspace, pi
import matplotlib.pyplot as plt


class F(object):
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def __call__(self, x):
        return sin(self.n*x)*cos(self.m*x)


# Instances
u = F(1, 2)
v = F(2, 3)

# Plot
x_values = linspace(0, 2*pi, 1000)
plt.plot(x_values, u(x_values))
plt.plot(x_values, v(x_values))
plt.show()

"""
Terminal>>python F.py

"""
