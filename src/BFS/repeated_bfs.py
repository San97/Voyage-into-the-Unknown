from src.BFS.create_maze import create_maze
from src.BFS.set_attributes.set_attr_for_new_maze import set_attr_new_maze
from src.BFS.bfs import bf_search

""" Here we have implemented environment updating as and when we arrive(more colloquially append()) on a
    node on the path returned by A*star. This was not done in the old repeated forward A* file. In this file we create a
    new node with all unblocked cells.
"""


def repeated_forward_bfs(MAZE, DIM, x, y):  # x,y indices to start from initially 0,0
    dim1 = DIM  # receive from main.py when called

    og_maze = MAZE
    new_maze = create_maze(dim1)
    set_attr_new_maze(new_maze, dim1)
    new_path = list()
    # temp_path = list()
    # temp_path.append((i, j))
    # print("WE ARE IN REPEATED FORWARD A*::")
    path, blocked_cell, nodes_traversed = bf_search(new_maze, dim1, x, y)
    # print("initial path:" + str(path))
    counter = 0
    total_nodes_popped = nodes_traversed

    while path:

        if path == [-1]:
            return [-1], total_nodes_popped

        else:
            for z in path:
                # (i1, j1) = path.pop(0)
                (i1, j1) = z
                counter += 1

                if (i1, j1) == (DIM - 1, DIM - 1):                               # goal node condition(change not done)
                    new_path.append((i1, j1))
                    # print("on goal node:" + str(z))
                    # print("Before Updating the field of view:")
                    # for i in range(len(new_maze)):
                    #     for j in range(len(new_maze[i])):
                    #         print(new_maze[i][j].state, end=" ")
                    #     print('\n')

                    neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                    for (X, Y) in neighbours:
                        a = i1 + X
                        b = j1 + Y
                        if a + b > 0 and 0 <= a < dim1 and 0 <= b < dim1:
                            new_maze[a][b].state = og_maze[a][b].state
                    # print("Goal node reached")
                    # print("After Updating the field of view:")
                    # for i in range(len(new_maze)):
                    #     for j in range(len(new_maze[i])):
                    #         print(new_maze[i][j].state, end=" ")
                    #     print('\n')
                    return new_path, total_nodes_popped
                    # break

                else:
                    # print("we are in unblocked cell so simply appending::")
                    new_path.append((i1, j1))                          # append() means we are walking on the planned path
                    # print("on node:" + str((i1, j1)))

                    # print("Before Updating the field of view:")
                    # for i in range(len(new_maze)):
                    #     for j in range(len(new_maze[i])):
                    #         print(new_maze[i][j].state, end=" ")
                    #     print('\n')

                    neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Block for updating field of view
                    for (X, Y) in neighbours:
                        a = i1 + X
                        b = j1 + Y
                        if a + b > 0 and 0 <= a < dim1 and 0 <= b < dim1:
                            new_maze[a][b].state = og_maze[a][b].state

                    # print("After Updating the field of view:")
                    # for i in range(len(new_maze)):
                    #     for j in range(len(new_maze[i])):
                    #         print(new_maze[i][j].state, end=" ")
                    #     print('\n')

                    # (p, q) = path[0]
                    index = path.index((i1, j1)) + 1
                    # print("taking next node in path:")
                    (p, q) = path[index]

                    if new_maze[p][q].state == 1:
                        path.clear()
                        counter += 2
                        # new_path.append((p, q))
                        path, blocked_cell, nodes_traversed = bf_search(new_maze, dim1, i1, j1)
                        total_nodes_popped = total_nodes_popped + nodes_traversed
                        new_path.pop()

        # if new_path[-1] == (DIM - 1, DIM - 1):
        #     return new_path, counter

    return [-1], total_nodes_popped
