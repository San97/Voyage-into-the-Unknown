"""Test to compare Chebyshev and Weighted Heuristics and plots for both Density vs AVG Trajectory Length and
Density vs Computational time when running A*."""


from src.create_maze import create_maze
from src.AStar import astar
from src.set_attributes.set_maze_attr_chebyshev import set_attr_chebyshev
from src.set_attributes.set_maze_attr_weighted_chebyshev import set_attr_weighted_chebyshev
import numpy as np
import matplotlib.pyplot as plt
import time

dim = 101
p = 0.23
a = np.linspace(0, 0.23, 100)
Prob = a[1::]
p1list = list()
p2list = list()
iterations_per_prob = 50
x1_axis = list()
x2_axis = list()
y1_axis = list()
y2_axis = list()
z_axis = list()
y11_axis = list()
y22_axis = list()


print("For weighted chebyshev(inadmissible):")
for p in Prob:
    t0 = time.perf_counter()
    avg_cells_processed_per_prob = 0
    cells_processed_per_prob = 0
    avg_denominator = 0

    for x in range(0, iterations_per_prob):
        maze = create_maze(dim)
        set_attr_weighted_chebyshev(maze, dim, p)

        path, blocked_cell, cells_processed = astar(maze, dim, 0, 0)

        if path == [-1]:
            continue
        else:
            avg_denominator = avg_denominator + 1
            cells_processed_per_prob = cells_processed_per_prob + cells_processed

    t1 = time.perf_counter() - t0
    print("time:" + str(t1))
    avg_cells_processed_per_prob = cells_processed_per_prob/avg_denominator
    p1list.append((p,avg_cells_processed_per_prob ))

    print(str(p) + " " + str(avg_cells_processed_per_prob))
    x1_axis.append(p)
    y1_axis.append(avg_cells_processed_per_prob)
    y11_axis.append(t1)
print(p1list)


print("\n\n")
print("Now for chebyshev(admissible)")

for p in Prob:
    t0 = time.perf_counter()
    avg_cells_processed_per_prob = 0
    cells_processed_per_prob = 0
    avg_denominator = 0

    for x in range(0, iterations_per_prob):
        maze = create_maze(dim)
        set_attr_chebyshev(maze, dim, p)

        path, blocked_cell, cells_processed = astar(maze, dim, 0, 0)

        if path == [-1]:
            continue
        else:
            avg_denominator = avg_denominator + 1
            cells_processed_per_prob = cells_processed_per_prob + cells_processed

    t1 = time.perf_counter() - t0
    print("time:" + str(t1))
    avg_cells_processed_per_prob = cells_processed_per_prob/avg_denominator
    p2list.append((p, avg_cells_processed_per_prob))
    print(str(p) + " " + str(avg_cells_processed_per_prob))
    x2_axis.append(p)
    y2_axis.append(avg_cells_processed_per_prob)
    y22_axis.append(t1)


print(p2list)

fig, ax = plt.subplots(2, 2)

ax[0][0].plot(x1_axis, y1_axis)
ax[0][0].set_ylabel("No. of cells processed")
ax[0][0].set_title("For Weighted chebyshev")


ax[0][1].plot(x1_axis, y11_axis)
ax[0][1].set_ylabel("Time")
ax[0][1].set_title("For Weighted chebyshev")


ax[1][0].plot(x1_axis, y2_axis)
ax[1][0].set_xlabel("Density")
ax[1][0].set_ylabel("No. of cells processed")
ax[1][0].set_title("For Chebyshev")


ax[1][1].plot(x1_axis, y22_axis)
ax[1][1].set_xlabel("Density")
ax[1][1].set_ylabel("Time")
ax[1][1].set_title("For Chebyshev")


plt.show()
