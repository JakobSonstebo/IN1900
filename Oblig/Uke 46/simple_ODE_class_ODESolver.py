import numpy as np
import matplotlib.pyplot as plt


class ODESolver(object):
    def __init__(self, f):
        self.f = f

    def advance(self):
        raise NotImplementedError

    def set_initial_conditions(self, U0):
        self.U0 = U0

    def solve(self, time_points):
        self.t = np.asarray(time_points)
        N = len(self.t)
        self.u = np.zeros(N)
        self.u[0] = self.U0

        for n in range(N-1):
            self.n = n
            self.u[n+1] = self.advance()

        return self.t, self.u


class ForwardEuler(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t

        dt = t[n+1] - t[n]
        u_new = u[n] + dt*f(u[n], t[n])
        return u_new


class F(object):
    def __call__(self, u, t):
        return u/5


if __name__ == '__main__':
    # Function
    f = F()

    # Solver
    solver = ForwardEuler(f)
    solver.set_initial_conditions(0.1)
    for n in [4, 8, 16, 32, 64, 128]:
        t_sol, u_sol = solver.solve(np.linspace(0, 20, n))
        plt.plot(t_sol, u_sol, label = f'dt = {20/n:.2f}')

    plt.legend()
    plt.show()

"""
Terminal>>python simple_ODE_class_ODESolver.py
"""