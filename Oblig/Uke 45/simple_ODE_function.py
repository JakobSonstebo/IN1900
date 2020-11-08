import numpy as np
import matplotlib.pyplot as plt


def ForwardEuler(f, U0, T, N):
    t = np.zeros(N + 1)
    u = np.zeros(N + 1)

    u[0] = U0
    t[0] = 0
    dt = T/N

    for i in range(N):
        u[i + 1] = u[i] + dt*f(u[i], t[i])
        t[i + 1] = t[i] + dt
    return t, u


def f(u, t):
    return u/5


if __name__ == '__main__':
    # Exact
    exact_times = np.linspace(0, 20, 1000)
    exact_sol = lambda t: 0.1 * np.exp(0.2 * t)
    plt.plot(exact_times, exact_sol(exact_times))

    for n in [4, 8, 16, 32, 64, 128]:
        t_sol, u_sol = ForwardEuler(f, 0.1, 20, n)
        plt.plot(t_sol, u_sol, label=f'dt = {20 / n:.2f}')

    # Formatting
    plt.legend()
    plt.show()

"""
Terminal>>python simple_ODE_function.py
"""
