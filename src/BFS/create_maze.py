class Cell:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent


def create_maze(a):
    dim = a
    maze = []

    for i in range(0, dim):
        sub_maze = []
        for j in range(0, dim):
            sub_maze.append(Cell(99, 1111))
        maze.append(sub_maze)

    return maze
