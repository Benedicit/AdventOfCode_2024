import numpy as np

def parse(part2=False):
    with open("input/Day15.txt") as f:
        grid = []
        movements = ""
        moves = False
        y = 0
        start = ()
        for line in f:
            line = line.strip()
            if moves:
                movements += line
                continue
            if "@" in line:
                start = line.index("@"), y
                if part2:
                    line = line.replace("#","##").replace("O","[]").replace(".","..").replace("@","@.")
                    grid.append(list(line))
                    start = line.index("@"), y
                    y += 1
                    continue
            if line == "":
                moves = True
            else:
                if part2:
                    line = line.replace("#","##").replace("O","[]").replace(".","..")
                grid.append(list(line))
                y += 1
    grid = np.array(grid)
    return grid, start, movements


def part1():
    """
    A simple state machine for the movement. Can be much more refined
    """
    grid, start, movements = parse()
    x,y = start
    for mov in movements:
        match mov:
            case "<":
                if grid[y][x-1] == "#":
                    continue
                elif grid[y][x-1] == "O":
                    temp = x-1
                    while grid[y][temp] == "O":
                        temp -= 1
                    if grid[y][temp] == "#":
                        continue
                    else:
                        grid[y][temp:x-1] = "O"
                        grid[y][x-1] = "@"
                        grid[y][x] = "."
                        x -= 1
                else:
                    grid[y][x - 1] = "@"
                    grid[y][x] = "."
                    x -= 1
            case ">":
                if grid[y][x + 1] == "#":
                    continue
                elif grid[y][x + 1] == "O":
                    temp = x + 1
                    while grid[y][temp] == "O":
                        temp += 1
                    if grid[y][temp] == "#":
                        continue
                    else:
                        grid[y][x+2:temp+1] = "O"
                        grid[y][x + 1] = "@"
                        grid[y][x] = "."
                        x += 1
                else:
                    grid[y][x + 1] = "@"
                    grid[y][x] = "."
                    x += 1
            case "^":
                if grid[y-1][x] == "#":
                    continue
                elif grid[y-1][x] == "O":
                    temp = y - 1
                    while grid[temp][x] == "O":
                        temp -= 1
                    if grid[temp][x] == "#":
                        continue
                    else:
                        grid[temp:y-1,x] = "O"
                        grid[y-1][x] = "@"
                        grid[y][x] = "."
                        y -= 1
                else:
                    grid[y - 1][x] = "@"
                    grid[y][x] = "."
                    y -= 1
            case "v":
                if grid[y + 1][x] == "#":
                    continue
                elif grid[y+1][x] == "O":
                    temp = y + 1
                    while grid[temp][x] == "O":
                        temp += 1
                    if grid[temp][x] == "#":
                        continue
                    else:
                        grid[y+2:temp+1,x] = "O"
                        grid[y + 1][x] = "@"
                        grid[y][x] = "."
                        y += 1
                else:
                    grid[y + 1][x] = "@"
                    grid[y][x] = "."
                    y += 1
    boxes = np.where(grid == "O")
    boxes = list(zip(boxes[0], boxes[1]))
    result = 0
    for i,j in boxes:
        result += 100 * i + j
    print(result)

def part2():
    """
    Almost the same as part 1, but for horizontal movements slices of the array will be moved. For the tricky part, the
    vertical movements, there is a recursive function which moves the boxes, in a second grid and if the
    movement is possible the new grid will be used, otherwise the old one stays.
    """
    grid, start, movements = parse(part2=True)
    x,y = start
    count = 0
    for mov in movements:
        match mov:
            case "<":
                if grid[y][x-1] == "#":
                    continue
                elif grid[y][x-1] == "[" or grid[y][x-1] == "]":
                    temp = x-1
                    while grid[y][temp] == "[" or grid[y][temp] == "]":
                        temp -= 1
                    if grid[y][temp] == "#":
                        continue
                    else:
                        grid[y][temp:x-1] = grid[y][temp+1:x]
                        grid[y][x-1] = "@"
                        grid[y][x] = "."
                        x -= 1
                else:
                    grid[y][x - 1] = "@"
                    grid[y][x] = "."
                    x -= 1
            case ">":
                if grid[y][x + 1] == "#":
                    continue
                elif grid[y][x + 1] == "[" or grid[y][x+1] == "]":
                    temp = x + 1
                    while grid[y][temp]== "[" or grid[y][temp]== "]":
                        temp += 1
                    if grid[y][temp] == "#":
                        continue
                    else:
                        grid[y][x+2:temp+1] = grid[y][x+1:temp]
                        grid[y][x + 1] = "@"
                        grid[y][x] = "."
                        x += 1
                else:
                    grid[y][x + 1] = "@"
                    grid[y][x] = "."
                    x += 1
            case "^":
                current = grid[y-1][x]
                if current == "#":
                    continue
                elif current == "[" or current == "]":
                    if current == "[":
                        left = x
                        right = x + 1
                    else:
                        left = x - 1
                        right = x
                    mod_grid = grid.copy()
                    check_move = move(left,right,y-1,-1,mod_grid)
                    if not check_move:
                        continue
                    else:
                        grid = mod_grid
                        grid[y-1][x] = "@"
                        grid[y][x] = "."
                        y -= 1
                else:
                    grid[y - 1][x] = "@"
                    grid[y][x] = "."
                    y -= 1
            case "v":
                current = grid[y+1][x]
                if current == "#":
                    continue
                elif current == "[" or current == "]":
                    if current == "[":
                        left = x
                        right = x + 1
                    else:
                        left = x - 1
                        right = x
                    mod_grid = grid.copy()
                    check_move = move(left, right, y + 1, 1, mod_grid)
                    if not check_move:
                        continue
                    else:
                        grid = mod_grid
                        grid[y + 1][x] = "@"
                        grid[y][x] = "."
                        y += 1
                else:
                    grid[y + 1][x] = "@"
                    grid[y][x] = "."
                    y += 1
        count += 1
    boxes = np.where(grid == "[") # It's always the distance to the left and top edge, so only the left part needs to be looked at
    boxes = list(zip(boxes[0], boxes[1]))
    result = 0
    for i,j in boxes:
        result += 100 * i + j
    print(result)

def move(left, right, y, direction, mod_grid):
    """
    The boxes are is similar to a binary tree, and I use a DFS where the parent moves only if the child can move.
    To make things easier, it is assumed that movement is possible and the leafs move always, but in the second grid. If it turned out not
    to be impossible the second grid will be discarded.
    :param left: index of [
    :param right: index of ]
    :param y: current y position
    :param direction: -1 === down, 1 === up
    :param mod_grid: the grid where movements will be stored
    :return: True if movement is possible, False otherwise
    """
    next_l = mod_grid[y + direction][left]
    next_r = mod_grid[y + direction][right]
    if next_l == "#" or next_r == '#':
        return False
    elif next_l == "." and next_r == ".":
        mod_grid[y + direction][left] = "["
        mod_grid[y + direction][right] = "]"
        mod_grid[y][left] = "."
        mod_grid[y][right] = "."
        return True
    else:
        movable_r = movable_l = True
        if next_l == "[":
            movable_l = move(left, right, y + direction, direction, mod_grid)
        if next_r == "[":
            movable_r = move(right, right+1, y + direction, direction, mod_grid)
        if next_l == "]":
            movable_l = move(left-1, left, y + direction, direction,mod_grid)
        movement_possible = movable_l and movable_r
        if movement_possible:
            mod_grid[y+direction][left] = "["
            mod_grid[y+direction][right] = "]"
            mod_grid[y][left] = "."
            mod_grid[y][right] = "."
        return movement_possible

part1()
part2()




