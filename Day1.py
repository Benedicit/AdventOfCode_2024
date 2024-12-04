import numpy as np

list1 = []
list2 = []
with open("./input/Day1.txt", "r") as f:
    for line in f:
        temp = line.strip().split("   ")
        list1.append(int(temp[0]))
        list2.append(int(temp[1]))
def part1(list1, list2):
    """
    With inhouse sort functions this day is trivial
    """
    list1.sort()
    list2.sort()
    sum_distances = 0
    for x, y in zip(list1, list2):
        sum_distances += abs(x - y)
    print("The sum of distances is", sum_distances)

def part2(list1, list2):
    """
    With count functions this part is trivial. One could've instead of the numpy one used the standard library count()
    """
    similarity_score = 0
    list1 = np.array(list1)
    list2 = np.array(list2)
    unique, count = np.unique(list2, return_counts=True)
    counts = dict(zip(unique, count))
    for x in list1:
        if x in counts:
            similarity_score += counts[x] * x
    print("The similarity score is", similarity_score)
part1(list1, list2)
part2(list1, list2)
