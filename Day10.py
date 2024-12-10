import numpy as np
def part_1_and_2():
    """
    Today was a simple graph problem where BFS or DFS are doing nice. I chose BFS and part 1 and part 2 are exactly the same.
    The only difference is that for part 1 we count the distinct number of nines reachable, while part 2 we count all
    nines/paths to a nine.
    """

    # Parse the input
    with open("input/Day10.txt") as f:
        zeros = []
        grid = []
        y = 0
        for line in f:
            line = list(map(int, line.strip()))
            for x in range(len(line)):
                if line[x] == 0:
                    zeros.append((x,y))
            grid.append(line)
            y += 1

    grid = np.array(grid)
    grid_border = y-1
    sum_nine = 0 # This is the accumulator for part 1
    sum_trails = 0 # This is the accumulator for part 2
    for zero in zeros:
        stack = [zero]
        nines = set()
        # Do the BFS
        while len(stack) > 0:
            x, y = stack.pop()
            current = grid[y][x]
            if current == 9:
                nines.add((x,y))
                sum_trails += 1
                continue
            # Check above
            if y > 0:
                above = grid[y-1][x]
                if above == current + 1:
                    stack.append((x,y-1))
            # Check below
            if y < grid_border:
                below = grid[y+1][x]
                if below == current + 1:
                    stack.append((x,y+1))
            # Check left
            if x > 0:
                left = grid[y][x-1]
                if left == current + 1:
                    stack.append((x-1,y))
            # Check right
            if x < grid_border:
                right = grid[y][x+1]
                if right == current + 1:
                    stack.append((x+1,y))
        sum_nine += len(nines)
    print("Part 1:", sum_nine)
    print("Part 2:", sum_trails)
part_1_and_2()




