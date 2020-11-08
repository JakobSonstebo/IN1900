from midpoint import Midpoint
from simple_ODE_class_ODESolver import ODESolver
import numpy as np
import matplotlib.pyplot as plt


class Heun(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t

        dt = t[n+1] - t[n]
        k_1 = f(u[n], t[n])
        k_2 = f(u[n] + dt*k_1, t[n] + dt)
        u_next = u[n] + dt*(k_1/2 + k_2/2)
        return u_next


def f(u, t):
    return t*np.cos(t) - np.sin(t)


if __name__ == '__main__':
    # Exact
    exact_times = np.linspace(0, 8*np.pi, 1000)
    exact_sol = lambda t: t*np.sin(t) + 2*np.cos(t)

    # Heun
    solver_heun = Heun(f)
    solver_heun.set_initial_conditions(2)

    # Midpoint
    solver_midpoint = Midpoint(f)
    solver_midpoint.set_initial_conditions(2)

    # Plotting
    N = [20, 25, 50, 150]
    methods = [solver_heun, solver_midpoint]
    method_names = ['Heun\'s method', 'Midpoint']
    for i, method in enumerate(methods):
        plt.subplot(1, 2, i+1)
        plt.plot(exact_times, exact_sol(exact_times), label=f'Exact')
        for n in N:
            times = np.linspace(0, 8 * np.pi, n)
            t, u = method.solve(times)
            plt.plot(t, u, label=f'n = {n}')

        plt.xlabel('t')
        plt.title(f'{method_names[i]}')
        plt.legend()

    plt.show()

"""
Terminal>>python compare_methods.py

"""