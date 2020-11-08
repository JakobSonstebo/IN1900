from simple_ODE_class_ODESolver import ForwardEuler
import numpy as np
import matplotlib.pyplot as plt


class Cooling(object):
    def __init__(self, h, T_s):
        self.h = h
        self.T_s = T_s

    def __call__(self, T, t):
        return -self.h*(T - self.T_s)


def estimate_h(t1, T_s, T0, T1):
    return (T1 - T0)/(t1*(T_s - T0))


def test_Cooling():
    h = estimate_h(15, 25, 95, 92)
    dT_exact = -h*(95 - 25)
    cool = Cooling(h, 25)
    dT_cool = cool(95, 0)
    tol = 10e-14
    success = abs(dT_cool - dT_exact) < tol
    assert success, 'Cooling doesn\'t work'


if __name__ == '__main__':
    # Test
    test_Cooling()

    # Solving coffee problem
    t0 = 15
    T0 = 95
    T1 = 92
    for t_s in [20, 25]:
        h = estimate_h(t0, t_s, T0, T1)
        cool = Cooling(h, t_s)
        solver = ForwardEuler(cool)
        solver.set_initial_conditions(T0)
        time = np.linspace(0, 1500, 10000)
        t, T = solver.solve(time)
        plt.plot(t, T, label=f'T_s = {t_s}')

    # Plot formatting
    plt.xlabel('Time in seconds')
    plt.ylabel('Temperatures in degrees celsius')
    plt.legend()
    plt.show()

