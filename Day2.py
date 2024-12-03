def check_safe(numbers):
    prev = int(numbers[0])
    ascending = 0
    safe = True
    for i in range(1, len(numbers)):
        x = int(numbers[i])
        if x == prev:
            safe = False
            break
        elif x < prev:
            if ascending == 1:
                safe = False
                break
            elif ascending == 0:
                ascending = -1
        elif x > prev:
            if ascending == -1:
                safe = False
                break
            elif ascending == 0:
                ascending = 1
        if abs(x -prev) > 3:
            safe = False
            break
        prev = x
    return safe


def part1():
    with open("./input/Day2.txt") as f:
        safe_reports = 0
        unsafe_reports = []
        for line in f:
            numbers = line.split(" ")
            safe = check_safe(numbers)
            if safe:
                safe_reports += 1
            else:
                unsafe_reports.append(numbers)
        print("Part 1:", safe_reports)
        return safe_reports, unsafe_reports

def part2():
    safe_reports, unsafe_reports = part1()
    for report in unsafe_reports:
        for skip in range(0, len(report)):
            numbers = report[:skip] + report[skip+1:]
            safe = check_safe(numbers)
            if safe:
                safe_reports += 1
                break
    print("Part 2:", safe_reports)
part2()