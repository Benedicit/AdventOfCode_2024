from itertools import combinations

def parse():
    with open("input/Day8.txt") as f:
        antennas = {}
        y = 0
        blocked = set()
        for line in f:
            chars = list(line.strip())
            grid_length = len(chars)
            for x in range(grid_length):
                if chars[x] != ".":
                    if not antennas.get(chars[x]):
                        antennas[chars[x]] = [(x, y)]
                    else:
                        antennas[chars[x]].append((x, y))
                    blocked.add((x,y))
            y += 1
    return antennas, grid_length, blocked

def part1():
    """
    In my input there are actually horizontally or vertically aligned antennas, so they are completely ignored here.
    Just get the difference in x and y and get the next antennas in line. For part 2, just repeat it till they are out of bounce.
    In this case we don't want every antenna already in our set.
    """
    antennas, grid_length, _ = parse()
    count_pos = 0
    blocked = set()
    for antenna in antennas:
        positions = antennas[antenna]
        direction = ""
        for (x_1, y_1), (x_2, y_2) in combinations(positions, 2):
            diff_x = abs(x_1 - x_2)
            diff_y = abs(y_1 - y_2)
            if x_1 < x_2 and y_1 < y_2:
                direction = "DiagForward"
            elif x_1 > x_2 and y_1 < y_2:
                direction = "DiagBackward"
            match direction:
                case "DiagForward":
                    x_1, y_1 = x_1 - diff_x, y_1 - diff_y
                    x_2, y_2 = x_2 + diff_x, y_2 + diff_y
                case "DiagBackward":
                    x_1, y_1 = x_1 + diff_x, y_1 - diff_y
                    x_2, y_2 = x_2 - diff_x, y_2 + diff_y
            if 0 <= x_1 < grid_length and 0 <= y_1 < grid_length and (x_1, y_1) not in blocked:
                count_pos += 1
                blocked.add((x_1, y_1))
            if 0 <= x_2 < grid_length and 0 <= y_2 < grid_length and (x_2, y_2) not in blocked:
                count_pos += 1
                blocked.add((x_2, y_2))
    print(count_pos)

def part2():
    """
    Same as part 1 but this time we already have all antennas already in the set and we compute antinodes
    till we are out of bounce. In my input there was no single antenna of a frequency so no extra handling of that needed.
    """
    antennas, grid_length, blocked = parse()
    count_pos = len(blocked) # All antennas count as antinodes, so we don't start with 0 but with the number of antennas
    for antenna in antennas:
        positions = antennas[antenna]
        direction = ""
        for (x_1, y_1), (x_2, y_2) in combinations(positions, 2):
            diff_x = abs(x_1 - x_2)
            diff_y = abs(y_1 - y_2)
            if x_1 < x_2 and y_1 < y_2:
                direction = "DiagForward"
            elif x_1 > x_2 and y_1 < y_2:
                direction = "DiagBackward"
            while 0 <= x_1 < grid_length and 0 <= y_1 < grid_length:
                match direction:
                    case "DiagForward":
                        x_1, y_1 = x_1 - diff_x, y_1 - diff_y
                    case "DiagBackward":
                        x_1, y_1 = x_1 + diff_x, y_1 - diff_y
                if 0 <= x_1 < grid_length and 0 <= y_1 < grid_length and (x_1, y_1) not in blocked:
                    count_pos += 1
                    blocked.add((x_1, y_1))
            while 0 <= x_2 < grid_length and 0 <= y_2 < grid_length:
                match direction:
                    case "DiagForward":
                        x_2, y_2 = x_2 + diff_x, y_2 + diff_y
                    case "DiagBackward":
                        x_2, y_2 = x_2 - diff_x, y_2 + diff_y
                if 0 <= x_2 < grid_length and 0 <= y_2 < grid_length and (x_2, y_2) not in blocked:
                    count_pos += 1
                    blocked.add((x_2, y_2))
    print(count_pos)

part1()
part2()

