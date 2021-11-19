"""Run this to test to plot data for
Density vs AVG( Length of Shortest Distance in Now Discovered Gridworld/Shortest Path in Full Gridworld """

from src.create_maze import create_maze
from src.AStar import astar
from src.set_attributes.set_maze_attr_manhattan import set_attr
from src.Repeated_AStar import repeated_forward_astar
import numpy as np
import matplotlib.pyplot as plt

dim = 101
p = 0.23
a = np.linspace(0, p, 100)
Prob = a[1::]
plist = list()
iterations_per_prob = 500
x_axis = list()
y_axis = list()

for p in Prob:
    avg_ratio_per_prob = 0
    sum_ratio = 0
    shortest_path_full_gridworld_perprob = 0
    shortest_path_length_perprob = 0
    avg_denominator = 0

    for x in range(0, iterations_per_prob):
        maze = create_maze(dim)
        set_attr(maze, dim, p)
        shortest_path_full_gridworld, blocked_cell, nodes_traversed = astar(maze, dim, 0, 0)
        if shortest_path_full_gridworld == [-1]:
            continue
        new_path_from_repeated_forward_astar, cells_processed = repeated_forward_astar(maze, dim, 0, 0)

        if new_path_from_repeated_forward_astar == [-1]:
            continue
        else:
            new_maze = create_maze(dim)
            set_attr(new_maze, dim, p)
            done_list = list()

            for y in new_path_from_repeated_forward_astar:
                (i, j) = y
                new_maze[i][j].state = maze[i][j].state
                done_list.append((i, j))

                neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for (X, Y) in neighbours:
                    a = i + X
                    b = j + Y
                    if a + b > 0 and 0 <= a < dim and 0 <= b < dim:
                        new_maze[a][b].state = maze[a][b].state
                        done_list.append((a, b))

            for i in range(len(new_maze)):
                for j in range(len(new_maze[i])):
                    if (i, j) in done_list:
                        pass
                    else:
                        new_maze[i][j].state = 1
            shortest_path_discovered_gridworld, blocked_cell, nodes_traversed = astar(new_maze, dim, 0, 0)

            if shortest_path_discovered_gridworld == [-1]:
                shortest_path_discovered_gridworld_length = 0
                continue
            else:
                shortest_path_length_perprob = shortest_path_length_perprob + \
                                               len(shortest_path_discovered_gridworld)

                shortest_path_full_gridworld_perprob = shortest_path_full_gridworld_perprob + \
                                                       len(shortest_path_full_gridworld)

                ratio = len(shortest_path_discovered_gridworld) / len(shortest_path_full_gridworld)
                sum_ratio = sum_ratio + ratio

                avg_denominator = avg_denominator + 1

    avg_ratio_per_prob = sum_ratio / avg_denominator
    plist.append((p, avg_ratio_per_prob))
    print(str(p) + " " + str(avg_ratio_per_prob))
    x_axis.append(p)
    y_axis.append(avg_ratio_per_prob)

print(plist)

plt.plot(x_axis, y_axis)
plt.xlabel('Density', fontsize=8)
plt.ylabel('Avg of Ratio', fontsize=8)
plt.title('Density vs AVG Shortest Path in Discovered Gridworld/Shortest Path in Full Gridworld', fontsize=7.5,
                                                                                                fontweight = 'bold')
plt.show()
