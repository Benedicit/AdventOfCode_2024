import re

def sum_mul(mul_list):
    result = 0
    for mul in mul_list:
        removed = mul.replace('mul(', '').replace(')', '')
        numbers = list(map(int, removed.split(',')))
        result += numbers[0] * numbers[1]
    return result
mul_re = re.compile(r'mul\([1-9][0-9]*,[1-9][0-9]*\)', re.MULTILINE)
def part1():
    """
    A simple regex does the trick
    """
    with open("input/Day3.txt") as f:
        valid_mul = []
        valid_mul += re.findall(mul_re, f.read())
        result = sum_mul(valid_mul)
        print("Part 1:", result)

def part2():
    """
    Here we look for everything which is between a do() and a don't() and make our search in every substring
    The .* needs the ?, as it otherwise won't stop after the first don't()
    """
    with open("input/Day3.txt") as f:
        valid_mul = []
        line = "do()" + f.read().replace('\n', '') + "don't()"
        # Start with do() to makes things easier. The don't() is only needed for the example input
        temp = re.findall(r"do\(\).*?don't\(\)",line)
        for do in temp:
            valid_mul += re.findall(mul_re, do)
        result = sum_mul(valid_mul)
        print("Part 2:", result)

def part2_v2():
    """
    Here we remove everything between a don't() and a do() and do our search
    The .* needs the ?, as it otherwise won't stop after the first do()
    """
    with open("input/Day3.txt") as f:
        valid_mul = []
        line = f.read().replace('\n', '')
        line = re.sub(r"don't\(\).*?do\(\)", "", line)
        line = re.sub(r"don't\(\).*", "", line) # There are don't()s without a do() in the end of the input
        # There is actually a way to combine the two lines: re.sub(r"don't\(\).*?(do\(\)|$)", "", line)
        valid_mul += re.findall(mul_re, line)
        result = sum_mul(valid_mul)
        print("Part 2:", result)

part1()
part2()
part2_v2()
