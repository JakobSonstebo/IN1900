import numpy as np


class ODESolver(object):
    def __init__(self, f):
        self.f = lambda u, t: np.asarray(f(u, t), float)

    def set_initial_condition(self, U0):
        if isinstance(U0, (float, int)):
            self.neq = 1
        else:
            U0 = np.asarray(U0)
            self.neq = U0.size
        self.U0 = U0

    def solve(self, time_points):
        self.t = np.asarray(time_points)
        N = len(self.t)
        if self.neq == 1:
            self.u = np.zeros(N)
        else:
            self.u = np.zeros([N, self.neq])

        self.u[0] = self.U0

        for n in range(N-1):
            self.n = n
            self.u[n+1] = self.advance()
        
        return self.u.transpose(), self.t                       # Transposed u so that I would get u on the form [u_0, u_1, ..., u_n].


class RungeKutta4(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = t[n+1] - t[n]
        dt2 = dt/2.0
        k1 = f(u[n], t[n])
        k2 = f(u[n] + dt2 * k1, t[n] + dt2)
        k3 = f(u[n] + dt2 * k2, t[n] + dt2)
        k4 = f(u[n] + dt * k3, t[n] + dt)
        unew = u[n] + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        return unew

