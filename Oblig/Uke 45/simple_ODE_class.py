import numpy as np
import matplotlib.pyplot as plt


class ForwardEuler(object):
    def __init__(self, f, U0, T, N):
        self.f, self.U0, self.T, self.N = f, U0, T, N
        self.t = np.zeros(self.N + 1)
        self.u = np.zeros(self.N + 1)
        self.dt = self.T/self.N

    def solve(self):
        self.u[0] = self.U0
        for i in range(self.N):
            self.u[i+1] = self.advance(i)
            self.t[i+1] = self.t[i] + self.dt
        return self.t, self.u

    def advance(self, n):
        u, dt, f, t = self.u, self.dt, self.f, self.t
        u_next = u[n] + dt*f(u[n], t[n])
        return u_next


class F(object):
    def __call__(self, u, t):
        return u/5


f = F()
for n in [4, 8, 16, 32, 64, 128]:
    solver = ForwardEuler(f, 0.1, 20, n)
    t_sol, u_sol = solver.solve()
    plt.plot(t_sol, u_sol, label = f'dt = {20/n:.2f}')

plt.legend()
plt.show()

"""
Terminal>>python simple_ODE_class.py

"""