from heapq import heappush, heappop
import numpy as np

border = 71
CORRUPTED = -10000
GOAL = border-1,border-1
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
grid = np.zeros((border, border), dtype=int)
MAX_CORRUPTION = 1024

def get_neighbors(cord, visited):
    neighbors = []
    for d in dirs:
        n = cord[0] + d[0], cord[1] + d[1]
        if n in visited:
            continue
        if 0<=n[0]<border and 0<=n[1]<border and grid[n] != CORRUPTED:
            neighbors.append(n)
    return neighbors

def dijkstra(print_goal):
    costs = np.full((border, border), 1000000000)
    visited = set()
    pq = []
    nodes = {(0, 0): ()}
    heappush(pq, (0, (0, 0)))
    while len(pq) > 0:
        cost, (cords) = heappop(pq)
        if cords == GOAL:
            if print_goal:
                print("Min steps to goal:", costs[GOAL])
            break
        visited.add(cords)
        costs[cords] = cost
        for n in get_neighbors(cords, visited):
            new_cost = cost + 1
            if new_cost < costs[n]:
                costs[n] = new_cost
                heappush(pq, (new_cost, n))
                nodes[n] = cords
    return nodes

def solution():
    corruption = []
    with open("input/Day18.txt") as f:
        for line in f:
            line = line.strip().split(",")
            x,y = int(line[0]), int(line[1])
            corruption.append((y,x))
    for i in range(MAX_CORRUPTION):
        c = corruption[i]
        grid[c] = CORRUPTED
    dijkstra(print_goal=True) # Part 1
    for i in range(MAX_CORRUPTION,len(corruption)):
        c = corruption[i]
        grid[c] = CORRUPTED
        nodes = dijkstra(print_goal=False)
        # Check if there is a path from the goal to the start
        try:
            path = set()
            stack = [(border-1,border-1)]
            while len(stack) > 0:
                cords = stack.pop()
                path.add(cords)
                if cords == (0,0):
                    break
                stack.append(nodes[cords])
        except Exception:
            y,x = c
            print(f"{x},{y}") # Part 2
            break

solution()



