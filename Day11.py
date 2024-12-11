import numpy as np
def part1():
    """
    This is the naive approach. It works for 25 iterations, but with number of stones >10e12 it is not feasible.
    """
    with open("input/Day11.txt") as f:
        stones = []
        for line in f:
            stones = list(map(int, line.split(" ")))
    for _ in range(25):
        i = 0
        end_stones = len(stones)
        while i < end_stones:
            current = stones[i]
            stone_str = str(current)
            if current == 0:
                stones[i] += 1
            elif len(stone_str) % 2 == 0:
                first_half = stone_str[:len(stone_str) // 2]
                second_half = stone_str[len(stone_str) // 2:]
                stones[i] = int(first_half)
                stones.insert(i+1, int(second_half))
                i += 1
                end_stones += 1
            else:
                stones[i] *= 2024
            i += 1
    print(len(stones))
    #print(stones)
def part2():
    """
    Because each stone with the same number will behave the same and the position is actually meaningless, we count simply
    always count all distinct numbers on stones and how often they appear.
    """
    with open("input/Day11.txt") as f:
        stones = []
        for line in f:
            stones = list(map(int, line.split(" ")))
    stones = np.array(stones)
    distinct_s, count = np.unique(stones, return_counts=True)
    counts = dict(zip(distinct_s, count))
    for _ in range(75):
        temp = {}
        for s in counts:
            stone_str = str(s)
            if s == 0:

                if 1 not in temp:
                    temp[1] = counts[s]
                else:
                    temp[1] += counts[s]
            elif len(stone_str) % 2 == 0:
                first_half = int(stone_str[:len(stone_str) // 2])
                second_half = int(stone_str[len(stone_str) // 2:])
                if first_half not in temp:
                    temp[first_half] = counts[s]
                else:
                    temp[first_half] += counts[s]
                if second_half not in temp:
                    temp[second_half] = counts[s]
                else:
                    temp[second_half] += counts[s]
            else:
                x = s * 2024
                if x not in temp:
                    temp[x] = counts[s]
                else:
                    temp[x] += counts[s]
        counts = temp
    result = 0
    for s in counts:
        result += counts[s]
    print(result)
part1()
part2()