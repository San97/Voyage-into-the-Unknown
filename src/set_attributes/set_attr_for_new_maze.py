from helper.for_new_maze.generate_gn_for_new_maze import cal_gn_for_new_maze
from helper.for_new_maze.generate_state_for_new_maze import cal_state_for_new_maze
from helper.for_new_maze.heuristics.generate_manhattan_for_new_maze import cal_manhattan_for_new_maze
from src.constants import INF


def set_attr_new_maze(Maze, Dim):
    """
    Function used to set attributes of the maze.
    :param Maze: Maze of which the attributes are to be set.
    :param Dim: Dimension of maze.
    :return: No return as a direct change in the objects of Cell class is reflected.
    """
    maze = Maze
    dim = Dim
    # loop though the whole maze and set the attributes. for Start cell, the state is 10. For Goal it is 100.
    # Parent of start if (999,999) as no parent exists. Parent of goal and other cells will change later on.
    for i in range(0, dim):
        for j in range(0, dim):
            if (i == 0) and (j == 0):
                maze[i][j].state = 10
                maze[i][j].gn = cal_gn_for_new_maze(i, j, dim, maze)
                maze[i][j].hn = cal_manhattan_for_new_maze(i, j, dim)
                maze[i][j].fn = maze[i][j].gn + maze[i][j].hn
                maze[i][j].parent = (999, 999)

            elif (i == dim - 1) and (j == dim - 1):
                maze[i][j].state = 100
                maze[i][j].gn = cal_gn_for_new_maze(i, j, dim, maze)
                maze[i][j].hn = cal_manhattan_for_new_maze(i, j, dim)  # n-dim -> n+n
                maze[i][j].fn = INF
                maze[i][j].parent = (-1, -1)

            else:
                maze[i][j].state = cal_state_for_new_maze()
                maze[i][j].hn = cal_manhattan_for_new_maze(i, j, dim)
                maze[i][j].gn = cal_gn_for_new_maze(i, j, dim, maze)
                maze[i][j].fn = INF
                maze[i][j].parent = (-1, -1)

