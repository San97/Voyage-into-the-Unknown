from helper.calculate_gn import cal_gn
from helper.heuristics.cal_chebyshev import cal_chebyshev
from helper.cal_state import cal_state


def set_attr_chebyshev(Maze, Dim, P):
    maze = Maze
    dim = Dim

    for i in range(0, dim):
        for j in range(0, dim):
            if (i == 0) and (j == 0):
                maze[i][j].state = 10
                maze[i][j].gn = cal_gn(i, j, dim, maze)
                maze[i][j].hn = cal_chebyshev(i, j, dim)
                maze[i][j].fn = maze[i][j].gn + maze[i][j].hn
                maze[i][j].parent = (999, 999)

            elif (i == dim - 1) and (j == dim - 1):
                maze[i][j].state = 100
                maze[i][j].gn = cal_gn(i, j, dim, maze)
                maze[i][j].hn = cal_chebyshev(i, j, dim)
                maze[i][j].fn = maze[i][j].gn + maze[i][j].hn
                maze[i][j].parent = (-1, -1)

            else:
                maze[i][j].state = cal_state(P)
                maze[i][j].hn = cal_chebyshev(i, j, dim)
                maze[i][j].gn = cal_gn(i, j, dim, maze)
                maze[i][j].fn = maze[i][j].gn + maze[i][j].hn
                maze[i][j].parent = (-1, -1)
