from src.create_maze import create_maze
from src.set_attributes.set_attr_for_new_maze import set_attr_new_maze
from src.AStar import astar

""" Here we have implemented environment updating as and when we arrive(more colloquially append()) on a
    node on the path returned by A*star. This was not done in the old repeated forward A* file. In this file we create
    a new node with all unblocked cells.
"""


def repeated_forward_astar_q8(MAZE, DIM, x, y):                    # x,y indices to start from initially 0,0
    dim1 = DIM                                                  # receive from main.py when called
    og_maze = MAZE
    new_maze = create_maze(dim1)
    set_attr_new_maze(new_maze, dim1)
    new_path = list()
    path, blocked_cell, nodes_traversed = astar(new_maze, dim1, x, y)
    # print("path by Astar:" + str(path))
    total_nodes_popped = 0
    backtrack_count = 0
    counter = 1

    while path:

        for z in path:
            if path == [-1]:
                return [-1], total_nodes_popped, backtrack_count
            (i1, j1) = z
            if (i1, j1) == (DIM - 1, DIM - 1):                               # goal node condition
                new_path.append((i1, j1))
                neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for (X, Y) in neighbours:
                    a = i1 + X
                    b = j1 + Y
                    if a + b > 0 and 0 <= a < dim1 and 0 <= b < dim1:
                        new_maze[a][b].state = og_maze[a][b].state
                return new_path, total_nodes_popped, backtrack_count
            else:
                new_path.append((i1, j1))                          # append() means we are walking on the planned path
                # print("Appended node"+ str((i1, j1)))
                # print("Before Updating:")
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
                # print("After Updating:")
                # for i in range(len(new_maze)):
                #     for j in range(len(new_maze[i])):
                #         print(new_maze[i][j].state, end=" ")
                #     print('\n')
                # print("\n\n")
                index = path.index((i1, j1)) + 1
                (p, q) = path[index]

                if new_maze[p][q].state == 1:
                    if index-1 == 0:
                        path.clear()
                        # backtrack_count = backtrack_count + 3
                        # print("called for recent unblocked node" + str((i1, j1)))
                        path, blocked_cell, nodes_traversed = astar(new_maze, dim1, i1, j1)
                        total_nodes_popped = total_nodes_popped + nodes_traversed
                        # print("path by Astar:" + str(path))
                        new_path.pop()

                    if (index-4) > 0:
                        (i11, j11) = path[index-4]
                        path.clear()
                        # backtrack_count = backtrack_count + 3
                        # print("called for (3 steps back)" + str((i11, j11)))
                        path, blocked_cell, nodes_traversed = astar(new_maze, dim1, i11, j11)
                        total_nodes_popped = total_nodes_popped + nodes_traversed
                        # print("path by Astar:" + str(path))

                        # new_path.pop()
                        # new_path.pop()
                        # new_path.pop()

                    elif (index-3) > 0:
                        (i11, j11) = path[index - 3]
                        path.clear()
                        # backtrack_count = backtrack_count + 2
                        # print("called for 2 steps back" + str((i11, j11)))
                        path, blocked_cell, nodes_traversed = astar(new_maze, dim1, i11, j11)
                        total_nodes_popped = total_nodes_popped + nodes_traversed
                        # print("path by Astar:" + str(path))

                    elif (index - 2) > 0:
                        (i11, j11) = path[index - 2]
                        path.clear()
                        # backtrack_count = backtrack_count + 2
                        # print("called for 1 step back" + str((i11, j11)))
                        path, blocked_cell, nodes_traversed = astar(new_maze, dim1, i11, j11)
                        total_nodes_popped = total_nodes_popped + nodes_traversed
                        # print("path by Astar:" + str(path))
                        # new_path.pop()
                        # new_path.pop()

                    else:
                        # print("called for last module" + str((i1, j1)))
                        path.clear()
                        path, blocked_cell, nodes_traversed = astar(new_maze, dim1, i1, j1)
                        # print("path by Astar:" + str(path))
                        total_nodes_popped = total_nodes_popped + nodes_traversed
                        counter = counter + 1
                        # new_path.pop()

    return [-1], total_nodes_popped, counter
