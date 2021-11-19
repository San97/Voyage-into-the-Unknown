def cal_chebyshev(a, b, Dim):
    dim = Dim
    x = abs(a - (dim - 1))
    y = abs(b - (dim - 1))
    return max(x, y)
