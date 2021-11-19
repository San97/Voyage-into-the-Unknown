def cal_weighted_chebyshev_for_new_maze(a, b, Dim):
    dim = Dim
    x = abs(a - (dim - 1))
    y = abs(b - (dim - 1))
    return (max(x, y))*2
