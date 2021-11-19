from queue import Queue
""" This is BFS """


def bf_search(MAZE, Dim, x, y):
    maze = MAZE
    dim = Dim
    open_queue = Queue()
    closed_set = set()
    blocked_set = set()
    open_queue.put(((x, y), maze[x][y].parent))
    counter = 0

    while not open_queue.empty():

        curr = open_queue.get()
        counter = counter + 1

        i1 = curr[0][0]  # to set i index of current maze cell
        j1 = curr[0][1]  # to set j index of current maze cell

        # print("current node:" + str((i1, j1)))

        if maze[i1][j1].state == 100:  # as state of GOAL is 100
            path = list()  # path to return(From goal to start)

            while (i1, j1) != (x, y):
                path.append((i1, j1))
                # print("path:"+str((i1, j1)))
                (i1, j1) = maze[i1][j1].parent
            path.append((i1, j1))
            # path.append((x, y))
            return path[::-1], blocked_set, counter

        else:
            child_array = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for (X, Y) in child_array:
                a = i1 + X
                b = j1 + Y
                # print((a, b))

                if a + b > 0 and 0 <= a < dim and 0 <= b < dim:

                    if maze[a][b].state == 1:  # blocked state condition
                        maze[a][b].parent = (i1, j1)
                        # print("parent created" + str(maze[a][b].parent))
                        closed_set.add((a, b))
                        blocked_set.add((a, b))

                    elif (a, b) in closed_set:
                        pass

                    else:
                        # print("Discovered 1st time and added to open_queue")
                        maze[a][b].parent = (i1, j1)
                        open_queue.put(((a, b), (i1, j1)))
                        closed_set.add((a, b))

    return [-1], blocked_set, counter
