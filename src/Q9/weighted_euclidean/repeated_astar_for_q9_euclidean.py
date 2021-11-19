from src.create_maze import create_maze
from src.Q9.weighted_euclidean.set_attr_new_maze_euclidean import set_attr_new_maze_euclidean
from src.AStar import astar


def repeated_forward_astar_euclidean(MAZE, DIM, x, y):
    """
    This is the function of Repeated A* with euclidean as heuristic.
    The agent uses this to plan the path and actually traverse on it.
    :param MAZE: original maze with all full information used by agent when it walks down the path.
    :param DIM: the dimension of maze.
    :param x: i value in (i,j) denoting start cell (0,0)
    :param y: j value in (i,j) denoting start cell (0,0)
    :return: path planned, blocked-set list, nodes processed
    """
    dim1 = DIM
    i = x
    j = y
    og_maze = MAZE
    new_maze = create_maze(dim1)
    set_attr_new_maze_euclidean(new_maze, dim1)
    new_path = list()
    path, blocked_cell, cells_popped = astar(new_maze, dim1, i, j)
    total_cells_popped = cells_popped

    while path:

        for z in path:
            if path == [-1]:
                return [-1], total_cells_popped

            (i1, j1) = z

            if (i1, j1) == (DIM - 1, DIM - 1):                               # goal node condition
                new_path.append((i1, j1))

                neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for (X, Y) in neighbours:
                    a = i1 + X
                    b = j1 + Y
                    if a + b > 0 and 0 <= a < dim1 and 0 <= b < dim1:
                        new_maze[a][b].state = og_maze[a][b].state

                return new_path, total_cells_popped

            else:
                new_path.append((i1, j1))

                neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for (X, Y) in neighbours:
                    a = i1 + X
                    b = j1 + Y
                    if a + b > 0 and 0 <= a < dim1 and 0 <= b < dim1:
                        new_maze[a][b].state = og_maze[a][b].state

                index = path.index((i1, j1)) + 1
                (p, q) = path[index]

                if new_maze[p][q].state == 1:
                    path.clear()
                    path, blocked_cell, nodes_traversed = astar(new_maze, dim1, i1, j1)
                    total_cells_popped = nodes_traversed + total_cells_popped
                    # new_path.pop()

    return [-1], total_cells_popped
