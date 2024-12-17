import numpy as np
from heapq import heappop, heappush

def parse():
    grid = []
    with open("input/Day16.txt") as f:
        for line in f:
            grid.append(list(line.strip()))
    grid = np.array(grid)
    return grid

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Left, Up, Right

def get_neighbors(cord,curr_d, grid):
    x,y = cord
    inverse_d = -x,-y
    neighbors = []
    for d in directions:
        turned = True if d != curr_d else False
        if d != inverse_d:
            if d == curr_d:
                new_x, new_y = cord[0] + d[0], cord[1] + d[1]
                if grid[new_y][new_x] != "#":
                    neighbors.append((new_x,new_y, d, turned))
            else:
                neighbors.append((x, y, d, turned))
    return neighbors

start_cost = 100000000

def part1():
    """
    Dijkstra does the job
    """
    grid = parse()
    border = grid.shape[0]
    border_x = grid.shape[1]
    pq = []
    x, y = 1, border - 2
    goal = "E"
    d = (1, 0)
    nodes = {(x, y, d): []}
    heappush(pq, (0, (x, y, d)))
    cost_nodes = {(x,y,d) : start_cost}
    while len(pq) > 0:
        cost, (x, y, d) = heappop(pq)
        current = (x, y, d)
        if grid[y][x] == goal:
            print(cost,d)
        for n in get_neighbors((x,y), d, grid):
            x_c, y_c, d, turned = n
            neighbor = (x_c, y_c, d)
            new_score = cost + 1000 if turned else cost + 1
            if (x_c, y_c, d) not in cost_nodes:
                cost_nodes[neighbor] = start_cost
            if new_score == cost_nodes[neighbor]:
                nodes[(x_c, y_c, d)].add(current)
            elif new_score < cost_nodes[neighbor]:
                nodes[(x_c, y_c, d)] = {current}
                cost_nodes[neighbor] = new_score
                heappush(pq, (new_score, (x_c, y_c, d)))
    tiles = set()
    stack = [(border_x-2,1,directions[0])]
    while len(stack) > 0:
        x,y,d = stack.pop()
        if (x,y,d) in tiles:
            continue
        grid[y][x] = "O"
        for n in nodes[(x,y,d)]:
            if n not in tiles:
                stack.append(n)
        tiles.add((x,y,d))
    check = np.where(np.array(grid) == "O")
    check = list(zip(check[0], check[1]))
    print(len(check))

part1()











