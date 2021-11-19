"""Run this test to plot data for Density vs AVG(Trajectory Length/Length of Shortest Distance in Now Discovered
Gridworld using Repeated BFS."""

from src.BFS.create_maze import create_maze
from src.BFS.bfs import bf_search
from src.BFS.set_attributes.set_attr import set_attr
from src.BFS.repeated_bfs import repeated_forward_bfs
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
total_time = 0

for p in Prob:
    t0 = time.perf_counter()
    avg_ratio_per_prob = 0
    sum_ratio = 0
    trajectory_length_per_prob = 0
    shortest_path_length_per_prob = 0
    avg_denominator = 0

    for x in range(0, iterations_per_prob):
        maze = create_maze(dim)
        set_attr(maze, dim, p)

        new_path_from_repeated_forward_astar, nodes_processed = repeated_forward_bfs(maze, dim, 0, 0)

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

                neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]             # Block for updating maze
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

            shortest_path_discovered_gridworld, blocked_cell, nodes_traversed = bf_search(new_maze, dim, 0, 0)

            if shortest_path_discovered_gridworld == [-1]:
                shortest_path_discovered_gridworld_length = 0
                continue
            else:

                shortest_path_discovered_gridworld_length = len(shortest_path_discovered_gridworld)
                shortest_path_length_per_prob = shortest_path_length_per_prob + \
                                                shortest_path_discovered_gridworld_length

                trajectory_length_per_prob = trajectory_length_per_prob + len(new_path_from_repeated_forward_astar)
                ratio = len(new_path_from_repeated_forward_astar) / len(shortest_path_discovered_gridworld)
                sum_ratio = sum_ratio + ratio

                avg_denominator = avg_denominator + 1

    t1 = time.perf_counter() - t0
    print("time:" + str(t1))
    avg_ratio_per_prob = sum_ratio / avg_denominator
    plist.append((p, avg_ratio_per_prob))
    print(str(p) + " " + str(avg_ratio_per_prob))
    x_axis.append(p)
    y_axis.append(avg_ratio_per_prob)
    total_time = total_time + t1

print(plist)
print("Total time taken:" + str(total_time))

plt.plot(x_axis, y_axis)
plt.xlabel('Density', fontsize=7)
plt.ylabel('Avg of Trajectory Length/Shortest Path length in Discovered Gridworld', fontsize=7)
plt.title('Density vs Avg Trajectory length/Shortest Path Length in Discovered Gridworld', fontsize=8,
                                                                                            fontweight='bold')
plt.show()
