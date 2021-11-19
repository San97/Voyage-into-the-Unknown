""" Run this test to plot density vs AVG Trajectory Length using Repeated BFS."""


from src.BFS.create_maze import create_maze
from src.BFS.set_attributes.set_attr import set_attr
from src.BFS.repeated_bfs import repeated_forward_bfs
import numpy as np
import matplotlib.pyplot as plt
import time


dim = 101
p = 0.25
a = np.linspace(0, 0.25, 100)
Prob = a[1::]
plist = list()
iterations_per_prob = 200
x_axis = list()
y_axis = list()
z_axis = list()


for p in Prob:
    t0 = time.perf_counter()
    avg_trajectory_per_prob = 0
    trajectory_length_per_prob = 0
    avg_denominator = 0

    for x in range(0, iterations_per_prob):
        maze = create_maze(dim)
        set_attr(maze, dim, p)
        new_path_from_repeated_forward_bfs, cells_processed = repeated_forward_bfs(maze, dim, 0, 0)

        if new_path_from_repeated_forward_bfs == [-1]:
            pass
        else:
            avg_denominator = avg_denominator + 1
            trajectory_length_per_prob = trajectory_length_per_prob + len(new_path_from_repeated_forward_bfs)

    t1 = time.perf_counter() - t0
    print("time:" + str(t1))
    avg_trajectory_per_prob = trajectory_length_per_prob/avg_denominator
    plist.append((p,avg_trajectory_per_prob))
    print(str(p) + " " + str(avg_trajectory_per_prob))
    x_axis.append(p)
    y_axis.append(avg_trajectory_per_prob)
    z_axis.append(t1)

print(plist)

fig, ax = plt.subplots(1, 2)

ax[0].plot(x_axis, y_axis)
ax[0].set_title('Density vs Avg Trajectory Length')
ax[1].plot(x_axis, z_axis)
ax[1].set_title('Density vs Time')

plt.show()
