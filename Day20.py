from heapq import heappush, heappop
from itertools import combinations

import numpy as np


dirs = [(1,0),(-1,0),(0,1),(0,-1)]

def cheat(grid, walls):
    border = grid.shape[0]
    for y,x in walls:
        if y == border-1 or x == border-1:
            continue
        cord = y,x

def build_path(nodes, goal,start):
    path = []
    stack = [goal]
    while len(stack) > 0:
        node = stack.pop()
        path.append(node)
        if node == start:
            path.reverse()
            return path
        stack.append(nodes[node])
    path.reverse()
    return path

def pairs_p1(path, grid, border):
    for a,b in combinations(path,2):
        diff = abs(a[0]-b[0])+abs(a[1]-b[1])
        if diff <= 2:
            _,diff_path = dijkstra(border,grid,a,b)
            if diff_path > diff and diff_path-diff >= 100:
                yield diff_path-diff
        continue
def pairs_p2(path, grid, border):
    for a,b in combinations(path,2):
        diff = abs(a[0]-b[0])+abs(a[1]-b[1])
        if 2 < diff <= 20:
            _,diff_path = dijkstra(border,grid,a,b)
            if diff_path > diff and diff_path-diff >= 100:
                yield diff_path-diff
        continue
def solution():
    """
    As there is only one path through the grid, a cheat is simply a pair of points in the grid. Only the ones where
    the Manhattan distance is less or equal than the max number of picoseconds are considered. Then it is checked, if we
    can gain anything. It is still simply brute forcing, so part 2 takes >10 minutes, but it works.
    """
    grid = []
    y = 0
    start = ()
    goal = ()
    with open("input/Day20.txt") as f:
        for line in f:
            line = line.strip()
            grid.append(list(line))
            if "S" in line:
                start = y, line.index("S")
            if "E" in line:
                goal = y, line.index("E")
            y += 1
    grid = np.array(grid)
    border = grid.shape[0]
    nodes,_ = dijkstra(border, grid, start, goal)
    shortest_path = build_path(nodes, goal, start)
    num_cheats_p1 = 0
    for _ in pairs_p1(shortest_path, grid, border):
        num_cheats_p1 += 1
    print("Part 1:", num_cheats_p1)

    num_cheats_p2 = 0
    for _ in pairs_p2(shortest_path, grid, border):
        num_cheats_p2 += 1
    print("Part 2:", num_cheats_p2+num_cheats_p1)
    """
    unique, count = np.unique(cheats, return_counts=True)
    counts = dict(zip(unique, count))
    print(counts)
    """


def get_neighbors(cord, visited, grid, border):
    neighbors = []
    for d in dirs:
        n = cord[0] + d[0], cord[1] + d[1]
        if n in visited:
            continue
        if 0<=n[0]<border and 0<=n[1]<border and grid[n] != "#":
            neighbors.append(n)
    return neighbors

def dijkstra(border, grid, start, goal):
    costs = np.full((border, border), 1000000000)
    visited = set()
    pq = []
    nodes = {start: ()}
    heappush(pq, (0, start))
    while len(pq) > 0:
        cost, (cords) = heappop(pq)
        if cords == goal:
            #print(costs[goal])
            break
        visited.add(cords)
        costs[cords] = cost
        for n in get_neighbors(cords, visited, grid, border):
            new_cost = cost + 1
            if new_cost < costs[n]:
                costs[n] = new_cost
                heappush(pq, (new_cost, n))
                nodes[n] = cords
    return nodes, costs[goal]

solution()