import numpy as np
import matplotlib.pyplot as plt

def population(r_0, f_0, N = 500, a = 0.04, b = 0.1, c = 0.005, e = 0.2):
    """Simulates number foxes and rabbits over time"""
    r = np.zeros(N + 1)
    r[0] = r_0
    f = np.zeros(N + 1)
    f[0] = f_0

    i = 1
    while i <= N:
        r[i] = r[i-1] + a*r[i-1] - c*r[i-1]*f[i-1]
        f[i] = f[i-1] + e*c*r[i-1]*f[i-1] - b*f[i-1]
        i += 1
    return r, f

# Plot
r, f = population(100, 20)
w = np.linspace(0, 500, 501)
plt.plot(w, r, f)
plt.show()

"""
Terminal>>python Lotka_Volterra.py
"""