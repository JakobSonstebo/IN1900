import numpy as np
import matplotlib.pyplot as plt

def abs_approx(x, N):
    """Approximates the value of |x| at x"""
    n = np.linspace(1, N, N)
    series = np.cos((2*n - 1)*x)/(2*n - 1)**2
    return np.pi/2 - 4/np.pi * np.sum(series)

# Stores 4 approximations as a list of arrays
approximations = []
x = np.linspace(-np.pi, np.pi, 1000)
for n in range(1, 5):

    approx = np.zeros(1000)
    for i in range(0, len(approx)):
        approx[i] = abs_approx(x[i], n)

    approximations.append(approx)

# Plots |x| and the 4 approximations
plt.plot(x, np.abs(x), label = r"$|x|$")
for i in range(len(approximations)):
    plt.plot(x, approximations[i], label = f"N = {i+1}")

# Plot specifications
plt.xlim(-np.pi, np.pi)
plt.ylim(0, np.pi)

plt.title("4 approximations to |x|")
plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()

"""
Du finner plottet av approksimasjonene i png filen 4_approximations.png.
"""
