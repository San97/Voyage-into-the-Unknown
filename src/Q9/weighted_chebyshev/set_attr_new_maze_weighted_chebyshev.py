from helper.for_new_maze.generate_gn_for_new_maze import cal_gn_for_new_maze
from helper.for_new_maze.generate_state_for_new_maze import cal_state_for_new_maze
from helper.for_new_maze.heuristics.generate_weighted_chebyshev import cal_weighted_chebyshev_for_new_maze
from src.constants import INF


def set_attr_weighted_chebyshev(Maze, Dim):
    maze = Maze
    dim = Dim

    for i in range(0, dim):
        for j in range(0, dim):
            if (i == 0) and (j == 0):
                maze[i][j].state = 10
                maze[i][j].gn = cal_gn_for_new_maze(i, j, dim, maze)
                maze[i][j].hn = cal_weighted_chebyshev_for_new_maze(i, j, dim)
                maze[i][j].fn = maze[i][j].gn + maze[i][j].hn
                maze[i][j].parent = (999, 999)
            elif (i == dim - 1) and (j == dim - 1):
                maze[i][j].state = 100
                maze[i][j].gn = cal_gn_for_new_maze(i, j, dim, maze)
                maze[i][j].hn = cal_weighted_chebyshev_for_new_maze(i, j, dim)
                maze[i][j].fn = INF
                maze[i][j].parent = (-1, -1)

            else:
                maze[i][j].state = cal_state_for_new_maze()
                maze[i][j].hn = cal_weighted_chebyshev_for_new_maze(i, j, dim)
                maze[i][j].gn = cal_gn_for_new_maze(i, j, dim, maze)
                maze[i][j].fn = INF
                maze[i][j].parent = (-1, -1)
