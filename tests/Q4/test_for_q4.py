"""Run this test to check the solvability of grid worlds for the density range (0,1)."""


from src.create_maze import create_maze
from src.AStar import astar
from src.set_attributes.set_maze_attr_manhattan import set_attr
import numpy as np
import matplotlib.pyplot as plt
import time

dim = 5
P = np.linspace(0, 0.1, 2)
Prob = P[1::]
p_list = list()
x_axis = list()
y_axis = list()
t0 = time.perf_counter()
path = list()
for p in Prob:
    solved_maze_count = 0

    for x in range(1):
        maze = create_maze(dim)
        set_attr(maze, dim, p)
        path, blocked_cell, nodes_traversed = astar(maze, dim, 0, 0)

        if path == [-1]:
            pass
        else:
            solved_maze_count = solved_maze_count + 1

    print(str(p) + " " + str(solved_maze_count))
    p_list.append((p, solved_maze_count))
    x_axis.append(p)
    y_axis.append(solved_maze_count)

print("This is path:" + str(path))
print(p_list)
t1 = time.perf_counter() - t0
print("time:" + str(t1))
plt.plot(x_axis, y_axis)
plt.xlabel('Density')
plt.ylabel('Solvability')
plt.title('Density vs Solvability')
plt.show()
