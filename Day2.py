import numpy as np


def part1():
    with open("./input/Day2.txt") as f:
        safe_reports = 0
        unsafe_reports = []
        for line in f:
            numbers = line.split(" ")
            prev = int(numbers[0])
            ascending = 0
            safe = True
            for i in range(1, len(numbers)):
                x = int(numbers[i])
                if x == prev:
                    safe = False
                    break
                if x < prev:
                    if ascending == 1:
                        safe = False
                        break
                    elif ascending == 0:
                        ascending = -1
                    if x < prev - 3:
                        safe = False
                        break
                elif x > prev:
                    if ascending == -1:
                        safe = False
                        break
                    elif ascending == 0:
                        ascending = 1
                    if x > prev + 3:
                        safe = False
                        break
                prev = x
            if safe:
                safe_reports += 1
            else:
                unsafe_reports.append(numbers)
        print(safe_reports)
        return safe_reports, unsafe_reports
def part2():
    with open("./input/Day2.txt") as f:
        safe_reports, unsafe_reports = part1()
        for report in unsafe_reports:
            for skip in range(0, len(report)):
                prev = int(report[0])
                ascending = 0
                safe = True
                for i in range(1, len(report)):
                    if i == skip:
                        continue
                    elif (skip == 0 and i == 1) :
                        prev = int(report[i])
                        continue
                    x = int(report[i])
                    if x == prev:
                        safe = False
                        break
                    if x < prev:
                        if ascending == 1:
                            safe = False
                            break
                        elif ascending == 0:
                            ascending = -1
                        if x < prev - 3:
                            safe = False
                            break
                    elif x > prev:
                        if ascending == -1:
                            safe = False
                            break
                        elif ascending == 0:
                            ascending = 1
                        if x > prev + 3:
                            safe = False
                            break
                    prev = x
                if safe:
                    safe_reports += 1
                    break
        print(safe_reports)
part2()