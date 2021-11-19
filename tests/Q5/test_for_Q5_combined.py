"""Run this test for getting combined results of manhattan, chebyshev and euclidean heuristics performance along
 with graph."""


from src.create_maze import create_maze
from src.AStar import astar
from src.set_attributes.set_maze_attr_manhattan import set_attr
from src.set_attributes.set_maze_attr_euclidean import set_attr_euclidean
from src.set_attributes.set_maze_attr_chebyshev import set_attr_chebyshev
import numpy as np
import matplotlib.pyplot as plt
import time

t0 = time.perf_counter()

dim = 101
P = np.linspace(0, 0.41, 100)
Prob = P[1::]
p_list1 = list()
p_list2 = list()
p_list3 = list()
iteration = 500
x_axis1 = list()
y_axis1 = list()
x_axis2 = list()
y_axis2 = list()
x_axis3 = list()
y_axis3 = list()

for p in Prob:
    cells_traversed_per_prob = 0
    denominator = 0
    avg_cells_per_prob = 0
    for x in range(iteration):
        maze = create_maze(dim)
        set_attr(maze, dim, p)
        path, blocked_cell, cells_traversed = astar(maze, dim, 0, 0)

        if path == [-1]:
            pass
        else:
            cells_traversed_per_prob = cells_traversed + cells_traversed_per_prob
            denominator = denominator + 1
    avg_cells_per_prob = cells_traversed_per_prob/denominator
    print(str(p) + " " + str(avg_cells_per_prob))
    p_list1.append((p, avg_cells_per_prob))
    x_axis1.append(p)
    y_axis1.append(avg_cells_per_prob)

print("For manhattan" + str(p_list1))


for p in Prob:
    cells_traversed_per_prob = 0
    denominator = 0
    avg_cells_per_prob = 0
    for x in range(iteration):
        maze = create_maze(dim)
        set_attr_euclidean(maze, dim, p)
        path, blocked_cell, cells_traversed = astar(maze, dim, 0, 0)

        if path == [-1]:
            pass
        else:
            cells_traversed_per_prob = cells_traversed + cells_traversed_per_prob
            denominator = denominator + 1
    avg_cells_per_prob = cells_traversed_per_prob/denominator
    print(str(p) + " " + str(avg_cells_per_prob))
    p_list2.append((p, avg_cells_per_prob))
    x_axis2.append(p)
    y_axis2.append(avg_cells_per_prob)

print("For euclidean:" + str(p_list2))


for p in Prob:
    cells_traversed_per_prob = 0
    denominator = 0
    avg_cells_per_prob = 0
    for x in range(iteration):
        maze = create_maze(dim)
        set_attr_chebyshev(maze, dim, p)

        path, blocked_cell, cells_traversed = astar(maze, dim, 0, 0)

        if path == [-1]:
            pass
        else:
            cells_traversed_per_prob = cells_traversed + cells_traversed_per_prob
            denominator = denominator + 1
    avg_cells_per_prob = cells_traversed_per_prob/denominator
    print(str(p) + " " + str(avg_cells_per_prob))
    p_list3.append((p, avg_cells_per_prob))
    x_axis3.append(p)
    y_axis3.append(avg_cells_per_prob)
print("For Chebyshev:" + str(p_list3))

t1 = time.perf_counter() - t0
print("time:" + str(t1))

plt.plot(x_axis1, y_axis1)
plt.plot(x_axis2, y_axis2)
plt.plot(x_axis3, y_axis3)
plt.xlabel('Density')
plt.ylabel('Nodes_Traversed')
plt.title('Density vs Traversed')
plt.legend(["Manhattan", "Euclidean", "Chebyshev"])
plt.show()
