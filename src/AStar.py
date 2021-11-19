from sortedcollections import SortedSet         # used Sorted Set because of log(n) time complexity for all operations.
from src.constants import INF                   # importing infinity variable


def astar(MAZE, Dim, x, y):
    """
    This is the function of Astar used to find shortest path from start to goal node. It is also used in Repeated
    Forward A* during path planning phase.
    :param MAZE: maze given to astar for path planning.
    :param Dim: the dimension of maze.
    :param x: i value in (i,j) denoting where to start the path planning
    :param y: j value in (i,j) denoting where to start the path planning
    :return: path planned, blocked-set list, nodes processed
    """

    maze = MAZE
    dim = Dim
    open_list = SortedSet()
    open_set = set()                                    # to keep track of of all the unprocessed cells in open_list
    closed_set = set()                                  # to keep track of all the cells processed
    blocked_set = set()                                 # to keep track of all the blocked_nodes
    # adding first unprocessed start cell in the list of open cells.
    open_list.add(((maze[x][y].fn, maze[x][y].hn), (x, y), maze[x][y].parent))
    # storing all indices of cells those in open_list also in open_set to easily check in O(1) time complexity.
    open_set.add((x, y))
    counter = 0                                         # to keep track of all processed nodes.
    # loop until there is nothing in open_list or the goal state is reached
    while open_list:
        # popping elements from front end from the open_list to process it
        curr = open_list.pop(0)
        counter = counter + 1
        # to set i index of current cell of maze
        i1 = curr[1][0]
        # to set j index of current cell of maze
        j1 = curr[1][1]
        # block for goal state as state of GOAL is 100. We create a new list called path which will contain final
        # path of cells from start cell to goal cell. We start from goal node and append the indices of parent by
        # using the parent attribute of each cell until we reach the start cell indices (x,y). We then return the
        # inverted list.
        if maze[i1][j1].state == 100:
            path = list()
            while (i1, j1) != (x, y):
                path.append((i1, j1))
                (i1, j1) = maze[i1][j1].parent
            path.append((i1, j1))
            return path[::-1], blocked_set, counter

        # Block for each successor. child_array consists all the possible movements of 1 distance in each direction.
        # Traverse through value in child_array and check if it's a valid cell in maze and if it is then process it.
        child_array = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for (X, Y) in child_array:
            a = i1 + X
            b = j1 + Y
            if a + b > 0 and 0 <= a < dim and 0 <= b < dim:
                # keeping a track of the probable g(n) of the successor using child_curr_cost.
                child_curr_cost = maze[i1][j1].gn + 1
                # blocked state condition. g(n), f(n) set to infinity and parent attribute is set to current node
                # being processed
                if maze[a][b].state == 1:
                    maze[a][b].gn = INF
                    maze[a][b].fn = INF
                    maze[a][b].parent = (i1, j1)
                    closed_set.add((a, b))
                    blocked_set.add((a, b))
                # If not block, then check if its already in open_set and if it is then check if old g(n) is less than
                # or equal to it. If this is the case then nothing is done as its already optimal. If it's not then
                # proper changes are made to g(n) and parent is set to current node under process. We will have to
                # first discard the old entry in open_list and then add the updated one.
                elif (a, b) in open_set:
                    if maze[a][b].gn <= child_curr_cost:
                        pass
                    else:
                        open_list.discard(((maze[a][b].fn, maze[a][b].hn), (a, b), maze[a][b].parent))
                        maze[a][b].gn = child_curr_cost
                        maze[a][b].fn = child_curr_cost + maze[a][b].hn
                        maze[a][b].parent = (i1, j1)
                        open_list.add(((maze[a][b].fn, maze[a][b].hn), (a, b), (i1, j1)))
                # check if its in the closed_set. If it is and old g(n) is already optimal then no changes. If this is
                # not the case then remove the indices from closed set, make proper assignments and add to the open_list
                elif (a, b) in closed_set:
                    if maze[a][b].gn <= child_curr_cost:
                        pass
                    else:
                        closed_set.remove((a, b))
                        maze[a][b].gn = child_curr_cost
                        maze[a][b].fn = child_curr_cost + maze[a][b].hn
                        maze[a][b].parent = (i1, j1)
                        open_list.add(((maze[a][b].fn, maze[a][b].hn), (a, b), (i1, j1)))
                        open_set.add((a, b))
                # if successor is discovered first time, then proper assignments are made and is added to open_list
                else:
                    maze[a][b].gn = child_curr_cost
                    maze[a][b].fn = child_curr_cost + maze[a][b].hn
                    maze[a][b].parent = (i1, j1)
                    open_list.add(((maze[a][b].fn, maze[a][b].hn), (a, b), (i1, j1)))
                    open_set.add((a, b))
        # After being processed, the current cell is now added to the closed_set
        closed_set.add((i1, j1))
    # Return condition when no cells are left to explore meaning that no path to goal exists.
    return [-1], blocked_set, counter
