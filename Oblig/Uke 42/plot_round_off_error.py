import matplotlib.pyplot as plt
import numpy as np


def errors(file):
    with open(file, 'r') as reader:
        # Arrays
        delta_x = np.zeros(19)
        abs_error = np.zeros(19)
        n = range(1, 20)

        # Adds values to arrays
        for i, line in enumerate(reader):
            entries = line.split(',')                           # Splits the line into each delta_x, df_approx etc..
            del entries[-1]                                     # Last entry in entries is always ' \n'

            # Creates a dictionary with delta_x etc
            # as keys and the corresponding values as values.
            values = {}
            for entry in entries:
                key = entry.split(': ')[0].strip()
                value = entry.split(': ')[1].strip()
                values[key] = value

            delta_x[i] = values['delta_x']
            abs_error[i] = values['abs_error']

            reader.readline()                                   # Skips every other line
    return delta_x, abs_error, n


def plotter(dx, error, n):
    plt.semilogy(n, dx)
    plt.semilogy(n, error)
    # Formatting
    plt.ylabel("Error and dx")
    plt.xlabel("n")
    plt.xticks(n)
    plt.show()


x, e, N = errors('approx_derivative_sine.txt')
plotter(x, e, N)

"""
Den økende absolutte feilen kommer av at vi trekker fra
hverandre de to svært like tallene sin(pi/3 + dx) og sin(pi/3) i telleren når vi estimerer
den deriverte, og da blir feilen stor. 
"""
