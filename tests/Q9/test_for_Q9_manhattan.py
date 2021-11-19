"""Test to compare manhattan and Weighted manhattan and plots for both Density vs AVG Trajectory Length and
Density vs Computational time when running Repeated A*."""

from src.create_maze import create_maze
from src.set_attributes.set_maze_attr_euclidean import set_attr_euclidean
from src.Q9.weighted_manhattan.repeated_astar_for_q9_weighted_manhattan import repeated_forward_astar_weighted
from src.Q9.weighted_manhattan.repeated_astar_for_q9_manhattan import repeated_forward_astar_manhattan
import numpy as np
import matplotlib.pyplot as plt
import time

dim = 101
p = 0.23
a = np.linspace(0, 0.23, 100)
Prob = a[1::]
p1list = list()
p2list = list()
iterations_per_prob = 200
x1_axis = list()
x2_axis = list()
y1_axis = list()
y2_axis = list()
z_axis = list()
y11_axis = list()
y22_axis = list()


print("For weighted manhattan(inadmissible):")
for p in Prob:
    t0 = time.perf_counter()
    avg_trajectory_per_prob = 0
    trajectory_length_per_prob = 0
    avg_denominator = 0

    for x in range(0, iterations_per_prob):
        maze = create_maze(dim)
        set_attr_euclidean(maze, dim, p)
        new_path_from_repeated_forward_astar, cells_processed = repeated_forward_astar_weighted(maze, dim, 0, 0)

        if new_path_from_repeated_forward_astar == -1:
            pass
        else:
            avg_denominator = avg_denominator + 1
            trajectory_length_per_prob = trajectory_length_per_prob + len(new_path_from_repeated_forward_astar)

    t1 = time.perf_counter() - t0
    print("time:" + str(t1))
    avg_trajectory_per_prob = trajectory_length_per_prob/avg_denominator
    p1list.append((p, avg_trajectory_per_prob ))

    print(str(p) + " " + str(avg_trajectory_per_prob))
    x1_axis.append(p)
    y1_axis.append(avg_trajectory_per_prob)
    y11_axis.append(t1)
print(p1list)


print("\n\n")
print("Now for manhattan(admissible)")

for p in Prob:
    t0 = time.perf_counter()
    avg_trajectory_per_prob = 0
    trajectory_length_per_prob = 0
    avg_denominator = 0

    for x in range(0, iterations_per_prob):
        maze = create_maze(dim)
        set_attr_euclidean(maze, dim, p)
        new_path_from_repeated_forward_astar, cells_processed = repeated_forward_astar_manhattan(maze, dim, 0, 0)

        if new_path_from_repeated_forward_astar == -1:
            pass
        else:
            avg_denominator = avg_denominator + 1
            trajectory_length_per_prob = trajectory_length_per_prob + len(new_path_from_repeated_forward_astar)

    t1 = time.perf_counter() - t0
    print("time:" + str(t1))
    avg_trajectory_per_prob = trajectory_length_per_prob/avg_denominator
    p2list.append((p, avg_trajectory_per_prob))
    print(str(p) + " " + str(avg_trajectory_per_prob))
    x2_axis.append(p)
    y2_axis.append(avg_trajectory_per_prob)
    y22_axis.append(t1)


print(p2list)

fig, ax = plt.subplots(2, 2)

ax[0][0].plot(x1_axis, y1_axis)
ax[0][0].set_ylabel("Trajectory Length")
ax[0][0].set_title("For Weighted Manhattan")


ax[0][1].plot(x1_axis, y11_axis)
ax[0][1].set_ylabel("Time")
ax[0][1].set_title("For Weighted Manhattan")


ax[1][0].plot(x1_axis, y2_axis)
ax[1][0].set_xlabel("Density")
ax[1][0].set_ylabel("Trajectory Length")
ax[1][0].set_title("For Manhattan")


ax[1][1].plot(x1_axis, y22_axis)
ax[1][1].set_xlabel("Density")
ax[1][1].set_ylabel("Time")
ax[1][1].set_title("For Manhattan")


plt.show()
