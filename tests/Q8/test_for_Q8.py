""" Run this test to plot Density vs Average Trajectory Length and Density vs Average Computational Time when we do
    more backtracking using the stored information and recycling it."""


from src.create_maze import create_maze
from src.AStar import astar
from src.set_attributes.set_maze_attr_manhattan import set_attr
from src.Q8_repeated_astar import repeated_forward_astar_q8
from src.Repeated_AStar import repeated_forward_astar
import numpy as np
import matplotlib.pyplot as plt
import time


dim = 101
p = 0.23
a = np.linspace(0, p, 100)
Prob = a[1::]
plist = list()
iterations_per_prob = 200
x_axis = list()
y_axis = list()
x1_axis = list()
y1_axis = list()
total_time = 0
z_axis = list()
z1_axis = list()

for p in Prob:
    t0 = time.perf_counter()
    avg_trajectory_per_prob = 0
    trajectory_length_per_prob = 0
    avg_denominator = 0

    for x in range(0, iterations_per_prob):
        maze = create_maze(dim)
        set_attr(maze, dim, p)

        path, blocked_cell, nodes_traversed = astar(maze, dim, 0, 0)
        if path == [-1]:
            pass
        else:
            pass
        new_path_from_repeated_forward_astar, cells_processed, backtrack_cells= repeated_forward_astar_q8(maze, dim, 0, 0)

        if new_path_from_repeated_forward_astar == [-1]:
            pass
        else:
            avg_denominator = avg_denominator + 1
            trajectory_length_per_prob = trajectory_length_per_prob + len(new_path_from_repeated_forward_astar)

    t1 = time.perf_counter() - t0
    print("time:" + str(t1))
    avg_trajectory_per_prob = trajectory_length_per_prob/avg_denominator
    plist.append((p, avg_trajectory_per_prob))
    print(str(p) + " " + str(avg_trajectory_per_prob))
    x_axis.append(p)
    y_axis.append(avg_trajectory_per_prob)
    z_axis.append(t1)
    total_time = total_time + t1


for p in Prob:
    t0 = time.perf_counter()
    avg_trajectory_per_prob = 0
    trajectory_length_per_prob = 0
    avg_denominator = 0

    for x in range(0, iterations_per_prob):
        maze = create_maze(dim)
        set_attr(maze, dim, p)
        path, blocked_cell, nodes_traversed = astar(maze, dim, 0, 0)
        if path == [-1]:
            pass
        else:
            pass
        new_path_from_repeated_forward_astar, cells_processed = repeated_forward_astar(maze, dim, 0, 0)

        if new_path_from_repeated_forward_astar == [-1]:
            # print("no path can be found:")
            pass
        else:
            avg_denominator = avg_denominator + 1
            trajectory_length_per_prob = trajectory_length_per_prob + len(new_path_from_repeated_forward_astar)

    t1 = time.perf_counter() - t0
    print("time:" + str(t1))
    avg_trajectory_per_prob = trajectory_length_per_prob/avg_denominator
    plist.append((p, avg_trajectory_per_prob))
    print(str(p) + " " + str(avg_trajectory_per_prob))
    x1_axis.append(p)
    y1_axis.append(avg_trajectory_per_prob)
    z1_axis.append(t1)
    # z_axis.append(t1)
    total_time = total_time + t1

fig, ax = plt.subplots(2, 2)
ax[0][0].plot(x_axis, y_axis)
ax[0][0].set_ylabel("Trajectory Length")
ax[0][0].set_title("For Q8")

ax[0][1].plot(x_axis, z_axis)
ax[0][1].set_ylabel("Time")
ax[0][1].set_title("For Q8")

ax[1][0].plot(x1_axis, y1_axis)
ax[1][0].set_ylabel("Trajectory Length")
ax[1][0].set_xlabel("Density")
ax[1][0].set_title("For Q6")

ax[1][1].plot(x1_axis, z1_axis)
ax[1][1].set_ylabel("Time")
ax[1][1].set_xlabel("Density")
ax[1][1].set_title("For Q6")
plt.show()