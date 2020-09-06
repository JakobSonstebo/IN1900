from math import exp

# Line 3 through 17 is copied from population_table.py
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

# Make two nested lists
pop_and_time = [times, pop_data]
pop_at_time = [[time, pop] for time, pop in zip(times, pop_data)]

# Loop over the first list (pop_and_time)
headers = ["Times (hours)", "Population"]
print(f"{headers[0]:<15} {headers[1]:<10}")

for i in range(n + 1):
    print(f"{round(pop_and_time[0][i]):<15} {round(pop_and_time[1][i]):<10}")

print("-"*35)

# Loop over the second list (pop_at_time)
print(f"{headers[0]:<15} {headers[1]:<10}")

for i in range(n+1):
    print(f'{round(pop_at_time[i][0]):<15} {round(pop_at_time[i][1]):<10}')
