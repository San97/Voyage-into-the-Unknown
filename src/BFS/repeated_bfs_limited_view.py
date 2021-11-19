from src.BFS.create_maze import create_maze
from src.BFS.set_attributes.set_attr_for_new_maze import set_attr_new_maze
from src.BFS.bfs import bf_search


def repeated_forward_bfs(MAZE, DIM, x, y):  # x,y indices to start from initially 0,0
    dim1 = DIM  # receive from main.py when called
    i = x
    j = y
    og_maze = MAZE
    new_maze = create_maze(dim1)
    set_attr_new_maze(new_maze, dim1)
    path, blocked_cell, nodes_traversed = bf_search(new_maze, dim1, i, j)
    total_cells_popped = nodes_traversed

    new_path = list()

    while path:

        if path == [-1]:
            return [-1], total_cells_popped

        else:
            for z in path:
                (i1, j1) = z

                if (i1, j1) == (DIM - 1, DIM - 1):
                    new_path.append(z)
                    # print("Goal node reached")
                    return new_path, total_cells_popped

                elif og_maze[i1][j1].state == 1:
                    # print("we found blocked cell so  calling A* again::")
                    new_maze[i1][j1].state = 1
                    (i11, j11) = new_path[-1]
                    new_path.pop()
                    # new_path.append(z)
                    # (i11, j11) = new_path[-2]
                    path, blocked_cell, nodes_traversed = bf_search(new_maze, dim1, i11, j11)
                    total_cells_popped = nodes_traversed + total_cells_popped
                    break

                else:
                    # print("we are in unblocked cell so simply appending::")
                    new_path.append(z)

        # if new_path[-1] == (DIM - 1, DIM - 1):
        #     return new_path

    return [-1], total_cells_popped

