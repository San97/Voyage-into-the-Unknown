class Cell:
    """
    defining the structure of each cell in the maze.
    """
    def __init__(self, state, parent, fn, gn, hn):
        """

        :param state: state of the cell(blocked-0 or unblocked-1)
        :param parent: indices of parent cell
        :param fn: f(n) value
        :param gn: g(n) value
        :param hn: h(n) value
        """
        self.state = state
        self.parent = parent
        self.fn = fn
        self.gn = gn
        self.hn = hn


def create_maze(dimension):
    """

    :param dimension: Dimension of maze.
    :return: created maze.
    """

    dim = dimension
    maze = []
    # making list of lists of objects of class Cell.
    for i in range(0, dim):
        sub_maze = []
        for j in range(0, dim):
            sub_maze.append(Cell(99, 1111, None, None, None))
        maze.append(sub_maze)

    return maze
