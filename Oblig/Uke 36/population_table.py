from math import exp

# Create list of times for population to be calculated
n = 12
times = [48/n*i for i in range(n+1)]


# Define a function that calculates the population at time t
def population(t):
    b = 50000
    k = 0.2
    c = 9.0
    return b / (1 + c*exp(-k*t))


# Use function to create a list of population values
pop_data = [population(t) for t in times]

# Print formatted table
n1 = "Times (hours)"
n2 = "Population"
print(f"{n1:<15} {n2:<10}")

for time, population_size in zip(times, pop_data):
    print(f'{round(time):<15} {round(population_size):<10}')
