import numpy as np
import matplotlib.pyplot as plt
from ODESolver import *
from SEIR import *

class RegionInteraction(Region):
	"""Subclass of region that adds distance functionality"""
	def __init__(self, name, S_0, E2_0, lat, long):
		"""Takes latitude and longitude information in degrees and converts it to radians"""
		self.lat = lat * np.pi / 180
		self.long = long * np.pi / 180

		# Uses the constructor of superclass Region
		super().__init__(name, S_0, E2_0)

	def distance(self, other):
		"""Uses arc length formula to calculate distance"""
		# This was wrong. It said 64 but I'm pretty sure it was supposed to be 640.
		R = 640
		sigma = np.sin(self.lat)*np.sin(other.lat) + np.cos(self.lat)*np.cos(other.lat)*np.cos(abs(self.long - other.long))

		# Since sigma calculated this way can get greater than 1 and yield an error, "neutralize to 1".
		if sigma > 1:
			raise ValueError('Sigma greater than 1')
		else:
			sigma = np.arccos(sigma)

		return R*sigma


class ProblemInteraction(ProblemSEIR):
	"""Extends ProblemSEIR to include the interaction between several regions"""
	def __init__(self, region, area_name, beta, r_ia = 0.1, r_e2=1.25, lmbda_1=0.33, lmbda_2=0.5, p_a=0.4, mu=0.2):
		"""Takes name of overarching area in addition to the same arguments as the constructor of ProblemSEIR does"""
		self.area_name = area_name
		super().__init__(region, beta, r_ia, r_e2, lmbda_1, lmbda_2, p_a, mu)

	def get_population(self):
		"""Calculates total area by summing all regions"""
		N = 0
		for r in self.region:
			N += r.population
		return N

	def set_initial_condition(self):
		"""Sets the inital conditions in all regions in a list"""
		self.initial_condition = []
		for r in self.region:
			self.initial_condition += [r.S_0, r.E1_0, r.E2_0, r.I_0, r.Ia_0, r.R_0]
		return self.initial_condition

	def __call__(self, u, t):
		"""Calculates the derivative at time t"""
		# Divides u into u for each region
		n = len(self.region)
		SEIR_list = [u[i:i+6] for i in range(0, len(u), 6)]

		# Gets E2 and Ia for each region
		E2_list = [u[i] for i in range(2, len(u), 6)]
		Ia_list = [u[i] for i in range(4, len(u), 6)]
		
		derivative = []
		for i in range(n):
			S, E1, E2, I, Ia, R = SEIR_list[i]
			N_i = sum(SEIR_list[i])

			# Calculates derivative for each u_region
			dS = - self.beta(t) * S * I / N_i

			# Loops over the other regions and calculates their contribution to change in susceptible population.
			for j in range(n):
				E2_other = E2_list[j]
				Ia_other = Ia_list[j]
				N_j = sum(SEIR_list[j])
				dS += -self.r_ia*self.beta(t)*S*Ia_other / N_j * np.exp(-self.region[i].distance(self.region[j]))
				dS += -self.r_e2*self.beta(t)*S*E2_other / N_j * np.exp(-self.region[i].distance(self.region[j]))

			# Rest of derivatives
			dE1 = -dS - self.lmbda_1*E1
			dE2 = self.lmbda_1 * (1 - self.p_a) * E1 - self.lmbda_2 * E2
			dI = self.lmbda_2 * E2 - self.mu * I
			dIa = self.lmbda_1 * self.p_a * E1 - self.mu * Ia
			dR = self.mu*(I + Ia)

			# Adds the derivatives from region i to a list of all the derivatives
			derivative += [dS, dE1, dE2, dI, dIa, dR]

		return derivative

	def solution(self, u, t):
		"""Assigns the solution to each region and calculates a total for each component"""
		# Calculates length of time-array and number of regions
		self.t = t
		n = len(self.t)
		n_reg = len(self.region)

		# Creates nested list consisting of solutions over time for each region
		SEIR_list = [u[i:i+6, :] for i in range(0, 6*n_reg, 6)]

		# Creates a matrix which will store all the total numbers
		sol = np.zeros((6, n))

		# Loops over each region in the region attribute and stores the solution in each of them
		for part, SEIR in zip(self.region, SEIR_list):
			part.set_SEIR_values(SEIR, t)

			# Adds numbers from each category and each region to total
			for i in range(6):
				sol[i] += SEIR[i]

		# Stores total solution as individual attributes
		self.S, self.E1, self.E2, self.I, self.Ia, self.R = sol

	def plot(self):
		"""Plots the total solutions against time"""
		solutions = [self.S, self.I, self.Ia, self.R]
		names = ['Susceptible', 'Infected', 'Asymptomatic', 'Recovered']
		for sol, name in zip(solutions, names):
			plt.plot(self.t, sol, label=f'{name}')
		plt.xlabel('Time(Days)')
		plt.ylabel('Population')
		plt.title(f'{self.area_name}')


if __name__ == '__main__':
	# Defines two regions
	innlandet = RegionInteraction('Innlandet', S_0=371385, E2_0=0, lat=60.7945, long=11.0680)
	oslo = RegionInteraction('Oslo', S_0=693494, E2_0=100, lat=59.9, long=10.8)
	# Prints distance between regions
	print(oslo.distance(innlandet))

	# Defines problem
	problem = ProblemInteraction([oslo, innlandet], 'Norway_east', beta=0.5)

	# Prints total population of regions
	print(problem.get_population())

	# Sets and prints initial conditions
	problem.set_initial_condition()
	print(problem.initial_condition)

	# Calculates derivative at initial conditon
	u = problem.initial_condition
	print(problem(u,0))

	# Solves problem
	solver = SolverSEIR(problem, T=100, dt=1.0)
	solver.solve()

	# Plots solution
	problem.plot()
	plt.legend()
	plt.show()

"""
>>>python SEIR_interaction.py
10.100809386280783
1064979
[693494, 0, 100, 0, 0, 0, 371385, 0, 0, 0, 0, 0]
[-62.49098896472576, 62.49098896472576, -50.0, 50.0, 0.0, 0.0, -0.0013736410771792993, 0.0013736410771792993, 0.0, 0.0, 0.0, 0.0]
"""