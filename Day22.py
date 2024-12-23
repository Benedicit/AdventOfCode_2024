import numpy as np


def parse():
    secrets = []
    with open("input/Day22.txt") as f:
        for line in f:
            secrets.append(int(line.strip()))
    return secrets

MODULO = 16777216


def hash_aoc(x):
    x ^= x * 64
    x %= MODULO
    x ^= x // 32
    x %= MODULO
    x ^= x << 11
    x %= MODULO
    return x

number_hashes = 2000

def solution():
    # Part 1
    secrets = parse()
    result = 0
    last_digits = np.zeros((len(secrets), number_hashes+1))
    for i in range(len(secrets)):
        x = secrets[i]
        last_digits[i][0] = x % 10
        for j in range(number_hashes):
            x = hash_aoc(x)
            last_digits[i][j+1] = x % 10
        result += x
    diffs = np.diff(last_digits)
    print(result)
    # Part 2
    possible_score = {}
    for i in range(len(diffs)):
        possible_sequences = set()
        s = diffs[i]
        for j in range(number_hashes - 4):
            check = s[j:j + 4]
            seq = tuple(check)
            if seq not in possible_sequences:
                num = last_digits[i][j+4]
                possible_sequences.add(seq)
                if seq not in possible_score:
                    possible_score[seq] = num
                else:
                    possible_score[seq] += num
    print(int(max(possible_score.values())))
solution()
