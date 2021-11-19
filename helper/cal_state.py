import random


def cal_state(P):
    """
    Used for setting state of cells in maze.
    :param P: Probability P with which a cell is blocked.
    :return: state of cell(blocked, unblocked)
    """
    r = random.uniform(0, 1)                    # generate a random floating decimal between 0 and 1
    if r <= P:
        return 1                                # 1 for blocked state
    else:
        return 0                                # 0 for unblocked state
