def cal_gn(a, b, x, A):
    maze = A
    dim = x
    if (a == 0) & (b == 0):
        return 0
    elif (a == dim-1) & (b == dim-1):
        return dim+dim-2
    else:
        if b == 0:
            return maze[a - 1][0].gn + 1
        else:
            return maze[a][b-1].gn + 1
