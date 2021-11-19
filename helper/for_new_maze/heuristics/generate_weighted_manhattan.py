def cal_weighted_manhattan_for_new_maze(a, b, Dim):
    dim = Dim
    return (abs(a-(dim-1))+abs(b-(dim-1))) * 2
