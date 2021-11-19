from helper.cal_state import cal_state


def set_attr(Maze, Dim, P):
    maze = Maze
    dim = Dim

    for i in range(0, dim):
        for j in range(0, dim):
            if (i == 0) and (j == 0):
                maze[i][j].state = 10  # state of start is 0
                maze[i][j].parent = (999, 999)  # parent of start is (999, 999)

            elif (i == dim - 1) and (j == dim - 1):
                maze[i][j].state = 100  # state of GOAL is 100
                maze[i][j].parent = (-1, -1)

            else:
                maze[i][j].state = cal_state(P)
                maze[i][j].parent = (-1, -1)

