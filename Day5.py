from itertools import permutations


def part1():
    with open("input/Day5.txt") as f:
        second_part = False
        rules = {}
        updates = []
        for line in f:
            if second_part:
                line = line.strip()
                updates.append(line.split(","))
            elif line == "\n":
                second_part = True
            else:
                line = line.strip()
                rule = line.split("|")
                if rule[0] not in rules:
                    rules[rule[0]] = {rule[1]}
                else:
                    rules[rule[0]].add(rule[1])
        correct_update = []
        incorrect_update = []
        for update in updates:
            len_update = len(update)
            correct = True
            for i in range(len_update):
                current = update[len_update-1-i]
                rule = rules.get(current)
                if rule:
                    for x in update[:len_update-1-i]:
                        if x in rule:
                            correct = False
                            break
                if not correct:
                    break
            if correct:
                correct_update.append(update)
            else:
                incorrect_update.append(update)
        result = 0
        for update in correct_update:
            result += int(update[len(update)//2])
        print(result)
        return rules, incorrect_update

def part2():
    rules, incorrect_update = part1()
    for update in incorrect_update:
        len_update = len(update)
        for _ in range(len_update):
            for i in range(len_update):
                current = update[len_update -1-i]
                rule = rules.get(current)
                if rule:
                    for x in update[:len_update-1-i]:
                        next_n = update.index(x)
                        if x in rule:
                            update[len_update-1-i], update[next_n] = update[next_n], update[len_update-1-i]
                            break
    result = 0
    for update in incorrect_update:
        result += int(update[len(update) // 2])
    print(result)
part2()