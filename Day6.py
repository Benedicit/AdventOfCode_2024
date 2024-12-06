import time

import numpy as np

def turn90(direction, x, y):
    match direction:
        case "UP":
            y += 1
            return x, y, "RIGHT"
        case "DOWN":
            y -= 1
            return x, y, "LEFT"
        case "LEFT":
            x += 1
            return x, y, "UP"
        case "RIGHT":
            x -= 1
            return x, y, "DOWN"
def parse_grid():
    with open("input/Day6.txt") as f:
        grid = []
        start_x = 0
        start_y = 0
        found = False
        for line in f:
            if "^" in line:
                found = True
                start_x = line.index("^")
            if not found:
                start_y += 1
            grid.append(list(line.strip()))
    return start_x, start_y, np.array(grid)

def part1():
    """
    It may get more compact but for my needs a simple state machine does the job fast enough while still being simple
    """
    direction = "UP"
    start_x, start_y, grid = parse_grid()
    x_length = grid.shape[0]
    y_length = grid.shape[1]
    path = set()
    while x_length > start_x >= 0 and y_length > start_y >= 0:
        if grid[start_y, start_x] == "#":
            start_x, start_y, direction = turn90(direction, start_x, start_y)
        grid[start_y, start_x] = "X"
        path.add((start_y, start_x))
        match direction:
            case "UP":
                start_y -= 1
            case "DOWN":
                start_y += 1
            case "LEFT":
                start_x -= 1
            case "RIGHT":
                start_x += 1
    unique, count = np.unique(grid, return_counts=True)
    counts = dict(zip(unique, count))
    result = counts["X"]
    print(result)
    return path

def check_loop(x_length, y_length, start_x, start_y, grid):
    loop = False
    direction = "UP"
    begin = time.time()
    while x_length > start_x >= 0 and y_length > start_y >= 0:
        if grid[start_y, start_x] == "#":
            start_x, start_y, direction = turn90(direction, start_x, start_y)
        match direction:
            case "UP":
                start_y -= 1
            case "DOWN":
                start_y += 1
            case "LEFT":
                start_x -= 1
            case "RIGHT":
                start_x += 1
        end = time.time()
        # It's way simpler, way more sketchy, to simply check execution time
        if end - begin >= 0.01: # This magic number depends on the speed of your CPU and may need to be changed for your needs
            loop = True
            break
    return loop

def part2():
    """
    A 130x130 is very easy to brute force and takes on a M1 Pro ~23,5 seconds
    """
    path = part1()
    start = time.time()
    start_x, start_y, grid = parse_grid()
    x_length = grid.shape[0]
    y_length = grid.shape[1]
    count_options = 0
    for (i, j) in path:
        grid_copy = np.copy(grid)
        x = start_x
        y = start_y
        grid_copy[i, j] = "#"
        loop = check_loop(x_length, y_length, x, y, grid_copy)
        if loop:
            count_options += 1
    end = time.time()
    print(end - start)
    print(count_options)

part2()



