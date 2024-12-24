import functools

import numpy as np

num_pad = np.array([
    ["7","8","9"],
    ["4","5","6"],
    ["1","2","3"],
    ["#","0","A"]
])
arrow_board = np.array(
    [["#","^","A"],
     ["<","v",">"]
])

def solution():
    with (open("input/Day21.txt") as file):
        result_p1 = 0
        result_p2 = 0
        for line in file:
            line = line.strip()
            depth_p1 = 3
            depth_p2 = 26
            p1 = rec_seq(line,depth_p1,depth_p1)
            p2 = rec_seq(line,depth_p2,depth_p2)
            numerical_part = int(line.replace("A",""))
            result_p1 += numerical_part * p1
            result_p2 += numerical_part * p2

        print("Part 1:", result_p1)
        print("Part 2:", result_p2)

@functools.cache
def rec_seq(s, depth, max_depth):
    """
    For every character make a depth first approach where it generates the next sequence to an A. So the start point is
    always the same.
    Using memoization it takes milliseconds
    :param s: current sequence
    :param depth: current depth
    :param max_depth: needed to switch grids
    :return: length of the current sequence at a certain depth
    """
    grid = arrow_board
    start = (0,2)
    y,x = start
    if depth == max_depth:
        grid = num_pad
        y,x = 3,2
    if depth == 0:
        return len(s)
    length = 0
    for c in s:
        new_s, (y,x) = make_sequence(c,(y,x),grid)
        length += rec_seq(new_s,depth-1,max_depth)
    return length

def make_sequence(c,start,grid):
    """
    Each grid has specific best sequences, if we need would go otherwise into the blocked space.
    In general: If we go left, we prefer x movement. If we go right, we prefer y movement.
    :param c: Character we want to press
    :param start: starting position
    :param grid: current grid
    :return: new x,y and the sequence which gets you to the button
    """
    y,x = start
    target_idx = np.where(grid == c)
    target_y, target_x = target_idx[0][0], target_idx[1][0]
    dir_grid_vert = -1 if y > target_y else 1
    dir_vert = "^" if dir_grid_vert == -1 else "v"
    dir_grid_hor = -1 if x > target_x else 1
    dir_hor = ">" if dir_grid_hor == 1 else "<"
    s = ""
    diff_y = abs(y - target_y)
    diff_x = abs(x - target_x)
    if np.array_equal(grid,arrow_board):
        if (y,x) == (1,0):
            s += dir_hor * diff_x + dir_vert * diff_y
            y,x = target_y, target_x
        elif (target_y,target_x) == (1,0):
            s += dir_vert * diff_y + dir_hor * diff_x
            y,x = target_y, target_x
    else:
        if target_x == 0 and y == 3:
            s += dir_vert * diff_y + dir_hor * diff_x
            y,x = target_y, target_x
        elif x == 0 and target_y == 3:
            s += dir_hor * diff_x + dir_vert * diff_y
            y, x = target_y, target_x
    if dir_hor == "<":
        if x != target_x:
            s += dir_hor * diff_x
        if y != target_y:
            s += dir_vert * diff_y
    else:
        if y != target_y:
            s += dir_vert * diff_y
        if x != target_x:
            s += dir_hor * diff_x
    s += "A"
    return s, (target_y,target_x)

solution()