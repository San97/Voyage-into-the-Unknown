from helper.for_new_maze.generate_gn_for_new_maze import cal_gn_for_new_maze
from helper.for_new_maze.generate_state_for_new_maze import cal_state_for_new_maze
from helper.for_new_maze.heuristics.generate_weighted_euclidean import cal_weighted_euclidean_for_new_maze
from src.constants import INF


def set_attr_weighted_euclidean(Maze, Dim):
    maze = Maze
    dim = Dim

    for i in range(0, dim):
        for j in range(0, dim):
            if (i == 0) and (j == 0):
                maze[i][j].state = 10  # state of start is 0
                maze[i][j].gn = cal_gn_for_new_maze(i, j, dim, maze)
                maze[i][j].hn = cal_weighted_euclidean_for_new_maze(i, j, dim)  # n-dim -> n+n
                maze[i][j].fn = maze[i][j].gn + maze[i][j].hn
                maze[i][j].parent = (999, 999)  # parent of start is (999, 999)

            elif (i == dim - 1) and (j == dim - 1):
                maze[i][j].state = 100  # state of GOAL is 100
                maze[i][j].gn = cal_gn_for_new_maze(i, j, dim, maze)
                maze[i][j].hn = cal_weighted_euclidean_for_new_maze(i, j, dim)  # n-dim -> n+n
                maze[i][j].fn = INF
                maze[i][j].parent = (-1, -1)

            else:
                maze[i][j].state = cal_state_for_new_maze()
                maze[i][j].hn = cal_weighted_euclidean_for_new_maze(i, j, dim)
                maze[i][j].gn = cal_gn_for_new_maze(i, j, dim, maze)
                maze[i][j].fn = INF
                maze[i][j].parent = (-1, -1)
