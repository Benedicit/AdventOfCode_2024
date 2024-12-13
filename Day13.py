import re

import numpy as np
offset = 10000000000000
def parse():
    with open("input/Day13.txt") as f:
        configs_part1 = []
        configs_part2 = []
        current_part1 = {}
        current_part2 = {}
        for line in f:
            if line == "\n":
                configs_part1.append(current_part1)
                configs_part2.append(current_part2)
                current_part1 = {}
                current_part2 = {}
                continue
            if "A" in line:
                line = re.sub("[A-Za-z+: ]", "", line)
                current_part1["A"] = np.fromstring(line, dtype=int, sep=",")
                current_part2["A"] = np.fromstring(line, dtype=int, sep=",")
            elif "B" in line:
                line = re.sub("[A-Za-z+: ]", "", line)
                current_part1["B"] = np.fromstring(line, dtype=int, sep=",")
                current_part2["B"] = np.fromstring(line, dtype=int, sep=",")
            else:
                line = re.sub("[A-Za-z=: ]", "", line)
                current_part1["Target"] = np.fromstring(line, dtype=int, sep=",")
                temp = np.fromstring(line, dtype=int, sep=",")
                current_part2["Target"] = np.array([temp[0]+offset, temp[1]+offset])
        configs_part1.append(current_part1)
        configs_part2.append(current_part2)
        return configs_part1, configs_part2

def part1():
    """
    I knew Brute force will take too long for part 2, but I wanted to do it anyway. Yes this can be optimzed, but it is
    not Brute force if it is not unoptimized :P.
    """
    configs,_ = parse()
    result = 0
    reference = []
    for c in configs:
        a = c["A"].transpose()
        b = c["B"]
        target = c["Target"]
        found = False
        for c_a in range(101):
            for c_b in range(101):
                curr = c_a * a + c_b * b
                if curr[0] == target[0] and curr[1] == target[1]:
                    result = result + 3 * c_a + c_b
                    found = True
                    reference.append((c_a, c_b))
                    break
            if found:
                break
    print(result)
    print(reference)
def part1_V2():
    """
    Simple linear equations solving. Numpy can do that automatically :)
    But because numpy will always find a solution, but not all are natural numbers, so we need an equal check
    """
    configs,_ = parse()
    result = 0
    #solutions = []
    for c in configs:
        a = c["A"]
        b = c["B"]
        target = c["Target"]
        temp = np.array([a, b]).T
        x = np.linalg.solve(temp, target.T)
        s_a = x[0].round(0)
        s_b = x[1].round(0)
        if 0 <=x[0] <= 100 and 0 <= x[1] <= 100:
            check_r = s_a * a + s_b * b
            if np.array_equal(check_r, target):
                result = result + int(s_a) * 3 + int(s_b)
                #solutions.append((s_a,s_b))
    print(result)
    #print(solutions)

def part2():
    """
    Simple linear equations solving. Numpy can do that automatically :)
    But because numpy will always find a solution, but not all are natural numbers, so we need an equal check
    """
    _,configs = parse()
    result = 0
    #solutions = []
    for c in configs:
        a = c["A"]
        b = c["B"]
        target = c["Target"]
        temp = np.array([a, b]).T
        x = np.linalg.solve(temp, target.T)
        s_a = x[0].round()
        s_b = x[1].round()
        # Number button presses are >= 0
        if 0 <=x[0] and 0 <= x[1]:
            check_r = s_a * a + s_b * b
            if np.array_equal(check_r, target):
                result = result + int(s_a) * 3 + int(s_b)
                #solutions.append((s_a,s_b))
    print(result)
    #print(solutions)

#part1()
part1_V2()
part2()


