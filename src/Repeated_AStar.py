# importing necessary requirements

from src.create_maze import create_maze
from src.set_attributes.set_attr_for_new_maze import set_attr_new_maze
from src.AStar import astar                                     # importing A* to use during planning phase


def repeated_forward_astar(MAZE, DIM, x, y):
    """
    This is the function of Repeated A*. The agent uses this to plan the path and actually traverse on it.
    :param MAZE: original maze with all full information used by agent when it walks down the path.
    :param DIM: the dimension of maze.
    :param x: i value in (i,j) denoting start cell (0,0)
    :param y: j value in (i,j) denoting start cell (0,0)
    :return: path planned, blocked-set list, nodes processed
    """

    dim1 = DIM
    # maze with full information.
    og_maze = MAZE
    # create a new maze and update it when agent gets knowledge of the cells.
    new_maze = create_maze(dim1)
    # setting attributes of the newly created maze with all cells unblocked.
    set_attr_new_maze(new_maze, dim1)
    # new_path is the list which contains the final trajectory of agent.
    new_path = list()
    # fist call to A* to plan the initial path.
    path, blocked_cell, cells_popped = astar(new_maze, dim1, x, y)
    # total_cells_popped keeps track of all the cells popped from the fringe by A*.
    total_cells_popped = cells_popped
    # loop until path returned by A* is [-1] which means no path is available, till goal is reached, or path list
    # becomes empty denoting no node from start to goal.
    while path:
        # z contains the indices of the path at 0 position.
        for z in path:
            # checking if path returned by A* is [-1] or not
            if path == [-1]:
                return [-1], total_cells_popped
            # reaching here means path has values in it which the agent will now process and traverse accordingly.
            (i1, j1) = z
            # check if goal is reached. If condition met then append the goal node indices to the new_path and assess
            # the neighbouring cells in FOV(field of view) and update the environment. Also return the trajectory
            # nodes popped off(nodes processed)
            if (i1, j1) == (DIM - 1, DIM - 1):
                new_path.append((i1, j1))
                # neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                # for (X, Y) in neighbours:
                #     a = i1 + X
                #     b = j1 + Y
                #     if a + b > 0 and 0 <= a < dim1 and 0 <= b < dim1:
                #         new_maze[a][b].state = og_maze[a][b].state
                return new_path, total_cells_popped
            # if not goal then append it to new_path as agent walks on it. Also update the FOV during walking phase.
            else:
                new_path.append((i1, j1))

                neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # for updating field of view
                for (X, Y) in neighbours:
                    a = i1 + X
                    b = j1 + Y
                    if a + b > 0 and 0 <= a < dim1 and 0 <= b < dim1:
                        new_maze[a][b].state = og_maze[a][b].state
                # check if next cell in the path returned by A* is blocked or not. If it's blocked, then run the
                # planning phase by making a call to astar with the current cell the agent has walked on.
                index = path.index((i1, j1)) + 1
                (p, q) = path[index]

                if new_maze[p][q].state == 1:
                    path.clear()
                    path, blocked_cell, cells_popped = astar(new_maze, dim1, i1, j1)
                    total_cells_popped = total_cells_popped + cells_popped
                    # popping to avoid 2 entries of the same current cell the agent is on because we have already
                    # appended it and the path from A* will also have the same start cell which will again append in
                    # next iteration
                    new_path.pop()
    # return [-1] as trajectory because no path exits as all cells have been processed and goal is not met.
    return [-1], total_cells_popped
