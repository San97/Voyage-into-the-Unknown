"""Run this test to plot Density vs Avd Number of cells processed by Repeated A*."""


from src.create_maze import create_maze
from src.set_attributes.set_maze_attr_manhattan import set_attr
from src.Repeated_AStar import repeated_forward_astar
import numpy as np
import matplotlib.pyplot as plt
import time

dim = 101
p = 0.23
a = np.linspace(0, p, 100)
Prob = a[1::]
plist = list()
iterations_per_prob = 1000
x_axis = list()
y_axis = list()
total_time = 0
# z_axis = list()

for p in Prob:
    t0 = time.perf_counter()
    avg_cells_processed_per_prob = 0
    cells_processed_per_prob = 0
    avg_denominator = 0

    for x in range(0, iterations_per_prob):
        maze = create_maze(dim)
        set_attr(maze, dim, p)
        new_path_from_repeated_forward_astar, cells_processed = repeated_forward_astar(maze, dim, 0, 0)

        if new_path_from_repeated_forward_astar == -1:
            # print("no path can be found:")
            continue
        else:
            avg_denominator = avg_denominator + 1
            cells_processed_per_prob = cells_processed_per_prob + cells_processed

    t1 = time.perf_counter() - t0
    print("time:" + str(t1))
    avg_cells_processed_per_prob = cells_processed_per_prob/avg_denominator
    plist.append((p,avg_cells_processed_per_prob ))
    print(str(p) + " " + str(avg_cells_processed_per_prob))
    x_axis.append(p)
    y_axis.append(avg_cells_processed_per_prob)
    total_time = total_time + t1

print(plist)
print("Total time taken:" + str(total_time))

plt.plot(x_axis, y_axis)
plt.xlabel('Density')
plt.ylabel('Average Number of cells processed')
plt.title('Density vs Average Number of cells processed')
plt.show()




