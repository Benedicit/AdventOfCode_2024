import re

def sum_mul(mul_list):
    result = 0
    for mul in mul_list:
        removed = mul.replace('mul(', '').replace(')', '')
        numbers = list(map(int, removed.split(',')))
        result += numbers[0] * numbers[1]
    return result
mul_re = re.compile(r'mul\([1-9][0-9]*,[1-9][0-9]*\)')
def part1():
    with open("input/Day3.txt") as f:
        valid_mul = []
        line = "".join(f.readlines()).replace('\n', '')
        valid_mul += re.findall(mul_re, line)
        result = sum_mul(valid_mul)
        print("Part 1:", result)

# Here we look for everything which is between a do() and a don't()
def part2():
    with open("input/Day3.txt") as f:
        valid_mul = []
        line = "".join(f.readlines()).replace('\n', '')
        line = "do()" + line + "don't()"
        # Start with do() to makes things easier. The don't() is needed for the example input
        temp = re.findall(r"do\(\).*?don't\(\)",line)
        for do in temp:
            valid_mul += re.findall(mul_re, do)
        result = sum_mul(valid_mul)
        print("Part 2:", result)

# Here we remove everything between a don't() and a do()
def part2_V2():
    with open("input/Day3.txt") as f:
        valid_mul = []
        line = "".join(f.readlines()).replace('\n', '')
        line = re.sub(r"don't\(\).*?do\(\)", "", line)
        line = re.sub(r"don't\(\).*", "", line) # There are don't()s without a do in the end of the input
        valid_mul += re.findall(mul_re, line)
        result = sum_mul(valid_mul)
        print("Part 2:", result)

part1()
part2()
part2_V2()
