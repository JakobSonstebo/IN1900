import numpy as np
import matplotlib.pyplot as plt


def heuns_method(f, U0, T, N):
    t = np.zeros(N + 1)
    u = np.zeros(N + 1)

    u[0] = U0
    dt = T/N

    for i in range(N):
        k_1 = f(u[i], t[i])
        k_2 = f(u[i] + k_1*dt, t[i] + dt)
        u[i+1] = u[i] + dt*(k_1/2 + k_2/2)
        t[i+1] = t[i] + dt
    return t, u


def f(u, t):
    return u


def test_heuns_against_hand_calculations():
    hand_calcs = [2.5, 6.25]
    t_test, u_test = heuns_method(f, 1, 2, 2)
    computed = [u_test[1], u_test[2]]
    tol = 10e-14
    success = abs(computed[0] - hand_calcs[0]) < tol and abs(computed[1] - hand_calcs[1]) < tol
    assert success, f'Heun\'s method failed. Computed = {computed}'


if __name__ == '__main__':
    test_heuns_against_hand_calculations()

    # Plots

    # Exact
    exact_t = np.linspace(0, 5, 1000)
    exact_sol = lambda t: np.exp(t)
    plt.plot(exact_t, exact_sol(exact_t), label=f'exact')

    # Heun's method
    for n in [4, 8, 16, 32, 64, 128]:
        t_sol, u_sol = heuns_method(f, 1, 5, n)
        plt.plot(t_sol, u_sol, label=f'dt = {5/n:.2f}')

    plt.legend()
    plt.show()

"""
Terminal>>python heuns_method.py

"""