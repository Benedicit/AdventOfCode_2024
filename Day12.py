import time

import numpy as np

pots = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # The possible "pots" that can appear in the input

def fill_subregion(y, x, border, grid):
    """
    A simple flood fill does the job. Just count during the fill the number of tiles and
     check if the neighbor belongs to your subregion or not
    :param y: start y
    :param x: start x
    :param border: length grid
    :param grid: input
    :return: number of tiles filled, perimeter, filled grid
    """
    area = 0
    perimeter = 0
    q = []
    q.append((y, x))
    visited = set()
    grid_filled = grid.copy()
    while len(q) > 0:
        y, x = q.pop(0)
        current_pot = grid[y][x]
        visited.add((y, x))
        grid_filled[y][x] = "#"
        area += 1
        if y == 0 or grid[y-1][x] != current_pot and (y-1,x) not in visited:
            perimeter += 1
        elif grid_filled[y-1][x] == current_pot and (y-1,x) not in q:
            q.append((y-1, x))
        if y == border - 1 or grid[y+1][x] != current_pot and (y+1,x) not in visited:
            perimeter += 1
        elif grid_filled[y+1][x] == current_pot and (y+1,x) not in q:
            q.append((y+1, x))
        if x == 0 or grid[y][x-1] != current_pot and (y,x-1) not in visited:
            perimeter += 1
        elif grid_filled[y][x-1] == current_pot and (y,x-1) not in q:
            q.append((y, x-1))
        if x == border - 1 or grid[y][x+1] != current_pot and (y,x+1) not in visited:
            perimeter += 1
        elif grid_filled[y][x+1] == current_pot and (y,x+1) not in q:
            q.append((y, x+1))
    #print(area, perimeter)
    return area, perimeter, grid_filled

def part1():
    grid = []
    result = 0
    with open("input/Day12.txt") as f:
        for line in f:
            grid.append(list(line.strip()))
    start = time.time()
    grid = np.array(grid)
    border = len(grid)
    for pot in pots:
        for i in range(border):
            for j in range(border):
                if grid[i][j] == pot:
                    area, perimeter, grid = fill_subregion(i, j, border, grid)
                    result += area * perimeter
    end = time.time()
    print("Time Part 1:", end - start)
    print("Part 1:", result)

def get_sides(y,x,border, grid):
    """
        The beginning is the same, but we store the the coordinates of the outer boundary of our subregion.
        After we filled the region, we only count lines (x or y increases by one) in the set.
        :param y: start y
        :param x: start x
        :param border: length grid
        :param grid: input
        :return: number of tiles filled, number sides, filled grid
    """
    area = 0
    sides = set()
    q = []
    q.append((y, x))
    visited = set()
    grid_filled = grid.copy()
    while len(q) > 0:
        y, x = q.pop(0)
        current_pot = grid[y][x]
        visited.add((y, x))
        grid_filled[y][x] = "#"
        area += 1
        if y == 0 or grid[y - 1][x] != current_pot and (y - 1, x) not in visited:
            sides.add(("up",x,y))
        elif grid_filled[y - 1][x] == current_pot and (y - 1, x) not in q:
            q.append((y - 1, x))
        if y == border - 1 or grid[y + 1][x] != current_pot and (y + 1, x) not in visited:
            sides.add(("down",x,y))
        elif grid_filled[y + 1][x] == current_pot and (y + 1, x) not in q:
            q.append((y + 1, x))
        if x == 0 or grid[y][x - 1] != current_pot and (y, x - 1) not in visited:
            sides.add(("left",x,y))
        elif grid_filled[y][x - 1] == current_pot and (y, x - 1) not in q:
            q.append((y, x - 1))
        if x == border - 1 or grid[y][x + 1] != current_pot and (y, x + 1) not in visited:
            sides.add(("right",x,y))
        elif grid_filled[y][x + 1] == current_pot and (y, x + 1) not in q:
            q.append((y, x + 1))
    number_sides = 0
    side_list = list(sides)
    side_list.sort() # The sorting is needed so all coordinates only increase the higher to index is
    #print(side_list)
    for s in side_list:
        if s not in sides:
            continue
        direction, x, y = s
        if direction == "down" or direction == "up":
            while (direction, x+1,y) in sides:
                sides.remove((direction, x+1,y))
                x += 1
            number_sides += 1
        elif direction == "left" or direction == "right":
            while (direction, x,y+1) in sides:
                sides.remove((direction, x,y+1))
                y += 1
            number_sides += 1
    return area, number_sides, grid_filled
def part2():
    grid = []
    result = 0
    with open("input/Day12.txt") as f:
        for line in f:
            grid.append(list(line.strip()))
    start = time.time()
    grid = np.array(grid)
    border = len(grid)
    for pot in pots:
        for i in range(border):
            for j in range(border):
                if grid[i][j] == pot:
                    area, sides, grid = get_sides(i,j,border, grid)
                    #print(pot, area, sides)
                    result += area * sides
    end = time.time()
    print("Time Part 2:", end - start)
    print("Part 2:",result)
part1()
part2()