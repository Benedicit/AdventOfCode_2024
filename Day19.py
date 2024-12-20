import functools
import re

patterns = [] # It needs to be available in combs(), but not as an argument, otherwise automated caching doesn't work

@functools.cache
def combs(s):
    """
    :param s: current string
    :return: number of possible combinations
    """
    result = 0
    if s == "":
        return 1
    else:
        for p in patterns:
            if s.startswith(p):
                result += combs(s[len(p):])
        return result

with open("input/Day19.txt") as f:
    towels = ""
    targets = []
    skip = False
    valid_towels = []
    for line in f:
        line = line.strip()
        if skip:
            targets.append(line)
        elif line == "":
            skip = True
            continue
        else:
            towels += line
    temp = towels.split(", ")
    regex = ""
    for t in temp:
        regex += f"({t})?"
    regex = f"^({regex})*$"
    sum_combs = 0
    for t in targets:
        search = re.findall(regex, t)
        if search:
            valid_towels.append(t)
    print(f"Part 1: {len(valid_towels)}")
    patterns = temp
    for t in valid_towels:
        sum_combs += combs(t)
    print(f"Part 2: {sum_combs}")









