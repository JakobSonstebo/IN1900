from simple_ODE_class_ODESolver import ODESolver, ForwardEuler
import numpy as np
import matplotlib.pyplot as plt


class Midpoint(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t

        dt = t[n+1] - t[n]
        k_1 = f(u[n], t[n])
        k_2 = f(u[n] + dt/2 * k_1, t[n] + dt/2)
        u_new = u[n] + dt*k_2
        return u_new


class F(object):
    def __call__(self, u, t):
        return np.cos(t) - t*np.sin(t)


if __name__ == '__main__':
    # Initialize function
    f = F()

    # Midpoint
    solver1 = Midpoint(f)
    solver1.set_initial_conditions(0.1)
    t_sol1, u_sol1 = solver1.solve(np.linspace(0, 4 * np.pi, 20))
    plt.plot(t_sol1, u_sol1, label='Midpoint')

    # Forward Euler
    solver2 = ForwardEuler(f)
    solver2.set_initial_conditions(0.1)
    t_sol2, u_sol2 = solver2.solve(np.linspace(0, 4 * np.pi, 20))
    plt.plot(t_sol2, u_sol2, label='Euler')

    # Exact
    exact_t = np.linspace(0, 4 * np.pi, 1000)
    exact_sol = lambda t: t * np.cos(t)
    plt.plot(exact_t, exact_sol(exact_t), label='Exact')

    plt.legend()
    plt.show()

"""
Terminal>>python midpoint.py

"""