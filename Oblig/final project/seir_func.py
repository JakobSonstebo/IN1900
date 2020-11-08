import numpy as np
import matplotlib.pyplot as plt
from ODESolver import ODESolver, RungeKutta4


def SEIR(u, t):
    """Tells us how to calculate the derivative at time t"""
    # Assigning values to constants in the model
    beta = 0.5; r_ia = 0.1; r_e2 = 1.25;
    lmbda_1 = 0.33; lmbda_2 = 0.5; p_a = 0.4; mu = 0.2;

    # Decompose u into its components and calculate derivatives
    S, E1, E2, I, Ia, R = u
    N = sum(u)
    dS = -beta * S * I / N - r_ia * beta * S * Ia / N - r_e2 * beta * S * E2/N
    dE1 = beta * S * I / N + r_ia * beta * S * Ia / N + r_e2 * beta * S * E2 / N - lmbda_1*E1
    dE2 = lmbda_1 * (1 - p_a) * E1 - lmbda_2 * E2
    dI = lmbda_2 * E2 - mu * I
    dIa = lmbda_1 * p_a * E1 - mu * Ia
    dR = mu*(I + Ia)
    return [dS, dE1, dE2, dI, dIa, dR]


def test_SEIR():
    """Tests whether SEIR(u,t) calculates the correct derivatives"""
    SEIR_computed = SEIR([1, 1, 1, 1, 1, 1], 0)
    SEIR_expected = [-0.19583333333333333, -0.1341666666666666, -0.302, 0.3, -0.068, 0.40]
    tol = 10e-14

    for comp, ex in zip(SEIR_computed, SEIR_expected):
        success = abs(comp - ex) < tol
        assert success, f'Computed {comp} not equal to expected {ex}'


def solve_SEIR(T, dt, S_0, E2_0):
    """Solves the differential equation given initial conditions and time"""
    # Initial conditions and time
    initial_conditions = [S_0, 0, E2_0, 0, 0, 0]
    times = np.linspace(0, T, int(T / dt) + 1)

    # Uses RungeKutta4 to solve
    solver = RungeKutta4(SEIR)
    solver.set_initial_condition(initial_conditions)
    u, t = solver.solve(times)

    return u, t


def plot_SEIR(u, t):
    """Plots S, I, Ia and R against time"""
    u_plot =  [u[0], u[3], u[4], u[5]]
    equations = ['S', 'I', 'Ia', 'R']
    for eq_name, eq in zip(equations, u_plot):
        plt.plot(t, eq, label= f'{eq_name}')
    plt.xlabel('Days')
    plt.ylabel('People')
    plt.legend()
    plt.show()

# Test
test_SEIR()

# Solution
un, ti = solve_SEIR(100, 1, 5e6, 100)
plot_SEIR(un, ti)

"""
>>>python seir_func.py
"""

