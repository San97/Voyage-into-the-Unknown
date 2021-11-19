from src.create_maze import create_maze
from src.set_attributes.set_attr_for_new_maze import set_attr_new_maze
from src.AStar import astar                                               # importing A* to use during planning phase


def repeated_forward_astar(MAZE, DIM, x, y):
    """
    This is the function of Repeated A*. The agent uses this to plan the path and actually traverse on it. But here the
    agent's FOV is crippled by 75 percent and can only see 1 cell ahead of him.
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
    # fist call to A* to plan the initial path.
    path, blocked_cell, nodes_traversed = astar(new_maze, dim1, x, y)
    # total_cells_popped keeps track of all the cells popped from the fringe by A*.
    total_cells_popped = nodes_traversed
    # new_path is the list which contains the final trajectory of agent.
    new_path = list()
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
            # check if goal is reached. If condition met then append the goal node indices to the new_path.
            # Also return the trajectory nodes popped off(nodes processed)
            if (i1, j1) == (DIM-1, DIM-1):
                new_path.append(z)
                # print("Goal node reached")
                return new_path, total_cells_popped
            # check if the current cell is blocked or not. If block, then update the environment, pop this current cell
            # from new_path and call the A* for path planning from previous unblocked cell. Popping is required to
            # avoid same unnecessary copy of the cell in the trajectory because this is not backtrack.
            elif og_maze[i1][j1].state == 1:
                new_maze[i1][j1].state = 1
                (i11, j11) = new_path[-1]                               # <---changed here
                new_path.pop()
                path, blocked_cell, nodes_traversed = astar(new_maze, dim1, i11, j11)
                total_cells_popped = nodes_traversed + total_cells_popped
                break
            # this is for an unblocked cell. Just simply append to the trajectory list.
            else:
                new_path.append(z)
    # return [-1] as trajectory because no path exits as all cells have been processed and goal is not met.
    return [-1], total_cells_popped

