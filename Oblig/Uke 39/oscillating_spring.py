import numpy as np
import matplotlib.pyplot as plt
from math import exp, cos, sqrt
k = 4
g = 0.15
m = 9
A = 0.3

# Non-vectorized version
"""
t_array = np.zeros(101)
y_array = np.zeros(101)

for i in range(101):
    t_array[i] = 25/100 * i
    y_array[i] = A*exp(-g*t_array[i])*cos(sqrt(k/m)*t_array[i])
"""

# Vectorized version
t_array = np.linspace(0, 25, 101)
y_array = A*np.exp(-g*t_array)*np.cos(sqrt(k/m)*t_array)

# Plot
plt.plot(t_array, y_array, label = r'$Ae^{-\gamma t}cos(\sqrt{\frac{k}{m}}t)$')
plt.legend()

plt.title("Oscillating spring")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.savefig("oscillating_spring.png")
plt.show()

"""
"""
