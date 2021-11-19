import math


def cal_euclidean(a, b, Dim):
    dim = Dim
    x = a - (dim - 1)
    y = b - (dim - 1)
    return math.sqrt(x * x + y * y)
