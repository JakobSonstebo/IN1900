import numpy as np
import matplotlib.pyplot as plt
from ODESolver import *

class Region(object):
    """Class that defines a region"""
    def __init__(self, name, S_0, E2_0):
        """Takes name of region together with initial susceptible population and infected"""
        self.name = name
        self.S_0 = S_0; self.E1_0 = 0; self.E2_0 = E2_0; self.I_0 = 0; self.Ia_0 = 0; self.R_0 = 0
        self.population = self.S_0 + self.E1_0 + self.E2_0 + self.I_0 + self.Ia_0 + self.R_0

    def set_SEIR_values(self, u, t):
        """Decomposes solution into individual components"""
        self.S, self.E1, self.E2, self.I, self.Ia, self.R = u
        self.t = t

    def plot(self):
        """Plots S, I, Ia and R against time"""
        solutions = [self.S, self.I, self.Ia, self.R]
        names = ['Susceptible', 'Infected', 'Asymptomatic', 'Recovered']
        for sol, name in zip(solutions, names):
            plt.plot(self.t, sol, label=f'{name}')
        plt.xlabel('Time(days)')
        plt.ylabel('Population')
        plt.title(f'{self.name}')


class ProblemSEIR(object):
    """Defines problem and tells us how to calculate derivative"""
    def __init__(self, region, beta, r_ia=0.1, r_e2=1.25, lmbda_1=0.33, lmbda_2=0.5, p_a=0.4, mu=0.2):
        """Takes information about the problem and stores it as attributes"""
        if isinstance(beta, (float, int)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta
        self.region, self.r_ia, self.r_e2 = region, r_ia, r_e2
        self.lmbda_1, self.lmbda_2, self.p_a, self.mu = lmbda_1, lmbda_2, p_a, mu

    def set_initial_condition(self):
        """Sets initial condition for the problem by extracting it from region"""
        self.initial_condition = [self.region.S_0, self.region.E1_0, self.region.E2_0, self.region.I_0, self.region.Ia_0, self.region.R_0]

    def get_population(self):
        """Gets population from region attribute"""
        return self.region.population

    def solution(self, u, t):
        """Assigns the solution to be stored in region attribute"""
        self.region.set_SEIR_values(u, t)

    def __call__(self, u, t):
        """Calculates the derivative at time t"""
        S, E1, E2, I, Ia, R = u

        # Total population
        N = sum(u)

        # Derivatives
        dS = -self.beta(t) * S * I / N - self.r_ia * self.beta(t) * S * Ia / N - self.r_e2 * self.beta(t) * S * E2/N
        dE1 = self.beta(t) * S * I / N + self.r_ia * self.beta(t) * S * Ia / N + self.r_e2 * self.beta(t) * S * E2 / N - self.lmbda_1*E1
        dE2 = self.lmbda_1 * (1 - self.p_a) * E1 - self.lmbda_2 * E2
        dI = self.lmbda_2 * E2 - self.mu * I
        dIa = self.lmbda_1 * self.p_a * E1 - self.mu * Ia
        dR = self.mu*(I + Ia)

        return [dS, dE1, dE2, dI, dIa, dR]


class SolverSEIR(object):
    """Solves SEIR problem by calling the RungeKutta4 method"""
    def __init__(self, problem, T, dt):
        """Takes the problem and time information"""
        self.problem, self.T, self.dt = problem, T, dt
        self.total_population = problem.get_population()

    def solve(self, method=RungeKutta4):
        """Solves the problem with RungeKutta4"""
        solver = method(self.problem)
        solver.set_initial_condition(self.problem.initial_condition)
        t = np.linspace(0, self.T, round(self.T / self.dt) + 1)
        u, t = solver.solve(t)
        self.problem.solution(u, t)


if __name__ == '__main__':
    # Region = Norway
    nor = Region('Norway', S_0=5e6, E2_0=100)

    # Prints information about Norway
    print(nor.name, nor.population)
    S_0, E1_0, E2_0 = nor.S_0, nor.E1_0, nor.E2_0
    I_0, Ia_0, R_0 = nor.I_0, nor.Ia_0, nor.R_0
    print(f'S_0 = {S_0}, E1_0 = {E1_0}, E2_0 = {E2_0}')
    print(f'I_0 = {I_0}, Ia_0 = {Ia_0}, R_0 = {R_0}')

    # Defines initial conditions in Norway
    u = np.array([S_0, E1_0, E2_0, I_0, Ia_0, R_0])
    nor.set_SEIR_values(u, 0)
    print(nor.S, nor.E1, nor.E2, nor.I, nor.Ia, nor.R)

    # Defines problem and sets initial condition
    problem = ProblemSEIR(nor,beta=0.5)
    problem.set_initial_condition()

    # Prints information about problem
    print(problem.initial_condition)
    print(problem.get_population())
    print(problem([1,1,1,1,1,1],0))

    # Solves problem
    solver = SolverSEIR(problem,T=100,dt=1.0)
    solver.solve()

    # Plots problem
    nor.plot()
    plt.legend()
    plt.show()

"""
>>>python SEIR.py
Norway 5000100.0
S_0 = 5000000.0, E1_0 = 0, E2_0 = 100
I_0 = 0, Ia_0 = 0, R_0 = 0
5000000.0 0.0 100.0 0.0 0.0 0.0
[5000000.0, 0, 100, 0, 0, 0]
5000100.0
[-0.19583333333333333, -0.13416666666666668, -0.302, 0.3, -0.068, 0.4]
"""