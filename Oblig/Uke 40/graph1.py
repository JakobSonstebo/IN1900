import matplotlib.pyplot as plt
from math import sqrt

def plot_line(p1, p2):
    """Plots line from p1 to p2"""
    x = [p1[0], p2[0]]
    y = [p1[1], p2[1]]
    plt.plot(x, y, 'b')


# Vertical
points1 = [(0, 0), (0, 1)]
plot_line(points1[0], points1[1])

# Horizontal
points2 = [(1, 1), (2, 1)]
plot_line(points2[0], points2[1])

# Show plot
plt.yticks([])                                                  # Removes y - ticks
plt.show()

def complete_graph(points):
    """Loops over all the points and draws a line to every other point in points"""
    for i in range(len(points)):
        plt.plot(points[i][0], points[i][1], 'ro')             # Plots the point
        for j in range(len(points)):
            plot_line(points[i], points[j])                    # Draws line to every point in points
    plt.yticks([])

# Square graph
complete_graph(((0, 0), (0, 1), (1, 1), (1, 0)))
plt.show()


# Cool pattern graph
a = sqrt(2)/2
points4 = ((1, 0), (a, a), (0, 1), (-a, a), (-1, 0), (-a, -a), (0, -1), (a, - a))

complete_graph(points4)
plt.show()

"""
Grafene finner du i png filene horizontal_vertical.png, square.png og cool_pattern_graph.png.
"""
