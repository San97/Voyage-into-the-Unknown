from src.constants import INF


def cal_gn_for_new_maze(a, b, dim, maze):
    """

    :param a: i index in tuple(i, j) of cell for which g(n) has the be set
    :param b: j index in tuple(i, j) of cell for which g(n) has the be set
    :param dim: dimension of maze
    :param maze: Maze
    :return: g(n) value
    """
    maze = maze
    dim = dim
    if (a == 0) & (b == 0):
        return 0
    else:
        # infinity is set to all other nodes except start when a new maze is created for agent other
        # then the actual maze.
        return INF
