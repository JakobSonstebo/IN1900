from SEIR_interaction import *
import matplotlib.pyplot as plt
from datetime import *


def read_file(filename):
	"""Takes file with information about regionns and and creates list of RegionInteraction instances"""
	with open(filename) as reader:

		regions = []
		for line in reader:
			# Creates a list of info about region but ignores first part of line.
			fylke_info = line.split(';')[1:]

			# Stores name of region in the variable name and strips it for extra spaces
			name = fylke_info.pop(0).strip()

			# Converts the rest of the line to floats and stores them in fitting variables
			S_0, E2_0, lat, long = [float(info) for info in fylke_info]

			# Appends RegionInteraction instance based on information from line
			regions.append(RegionInteraction(name, S_0, E2_0, lat, long))

	return regions


def B(t):
	"""Piece-wise function for beta"""
	# Initializes start-date as 15.02.2020
	d = date(2020, 2, 15)
	t = d + timedelta(t)

	# Calculates R based on time passed after start-date
	if t < date(2020, 3, 15):
		R = 4.0
	elif t < date(2020, 4, 21):
		R = 0.5
	elif t < date(2020, 5, 11):
		R = 0.4
	elif t < date(2020, 7, 1):
		R = 0.8
	elif t < date(2020, 8, 1):
		R = 0.9
	elif t < date(2020, 9, 1):
		R = 1.0
	else:
		R = 1.1

	# Other variables
	r_e2 = 1.25
	lmbda_2 = 0.5
	r_ia = 0.1
	mu = 0.2

	# Returns B based on formula
	return R / (r_e2 / lmbda_2 + r_ia / mu + 1 / mu)


def covid19_Norway(beta, filename, num_days, dt):
	"""Defines covid19 problem in Norway and models how it develops over a certain number of days"""
	# Creates list of regions
	regions = read_file(filename)

	# Defines problem
	problem = ProblemInteraction(regions, 'Norway', beta)
	problem.set_initial_condition()

	# Solves problem
	solver = SolverSEIR(problem, num_days, dt)
	solver.solve()
	
	# Plotting
	plt.figure(figsize=(9,12))
	index = 1
	for region in problem.region:
		plt.subplot(4,3,index)
		region.plot()
		index += 1
	plt.subplot(4,3,index)
	plt.subplots_adjust(hspace = 0.75, wspace=0.5)
	problem.plot()
	plt.legend()
	plt.show()


if __name__ == '__main__':
	covid19_Norway(beta=B, filename='fylker.txt', num_days=100, dt=1.0)

"""
>>>python covid19.py

"""