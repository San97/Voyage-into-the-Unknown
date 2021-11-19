from helper.calculate_gn import cal_gn
from helper.for_new_maze.heuristics.generate_weighted_manhattan import cal_weighted_manhattan_for_new_maze
from helper.cal_state import cal_state


def set_attr_weighted_manhattan(Maze, Dim, P):
    maze = Maze
    dim = Dim

    for i in range(0, dim):
        for j in range(0, dim):
            if (i == 0) and (j == 0):
                maze[i][j].state = 10
                maze[i][j].gn = cal_gn(i, j, dim, maze)
                maze[i][j].hn = cal_weighted_manhattan_for_new_maze(i, j, dim)
                maze[i][j].fn = maze[i][j].gn + maze[i][j].hn
                maze[i][j].parent = (999, 999)

            elif (i == dim - 1) and (j == dim - 1):
                maze[i][j].state = 100
                maze[i][j].gn = cal_gn(i, j, dim, maze)
                maze[i][j].hn = cal_weighted_manhattan_for_new_maze(i, j, dim)
                maze[i][j].fn = maze[i][j].gn + maze[i][j].hn
                maze[i][j].parent = (-1, -1)

            else:
                maze[i][j].state = cal_state(P)
                maze[i][j].hn = cal_weighted_manhattan_for_new_maze(i, j, dim)
                maze[i][j].gn = cal_gn(i, j, dim, maze)
                maze[i][j].fn = maze[i][j].gn + maze[i][j].hn
                maze[i][j].parent = (-1, -1)
