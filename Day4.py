import re
import numpy as np

def part1():
    """
    Instead going to the grid one by one, I utilize the np.diag() function to give me all diagonals.
    After that I concat everything in one big string, where each column, diagonal etc. is seperated by a #. Otherwise, there
    could be an accidental XMAS or SAMX. In the end I just let the regex find all matches and count them
    """
    with (open("input/Day4.txt") as f):
        grid = []
        width = 0
        for line in f:
            width = len(line)
            grid.append(list(line.replace("\n", "")))
        arr = np.array(grid)
        arr_rot = np.rot90(arr)
        diag = [np.diag(arr, k=i) for i in range(-width, width)] + \
               [np.diag(arr_rot, k=i) for i in range(-width, width)]
        
        whole_str = "#".join("".join(row) for row in arr) + \
                    "#".join("".join(row) for row in arr_rot) + \
                    "#".join("".join(d) for d in diag)
        
        count = len(re.findall(r'XMAS', whole_str)) + len(re.findall(r'SAMX', whole_str))
        print(count)

def part2():
    """
    This part was so much easier, as here it is always a 3x3 subgrid we have to look at and don't need to worry about
    things going vertical, horizontal and diagonal. So a simple search through the grid works more than fine.
    """
    with open("input/Day4.txt") as f:
        grid = []
        for line in f:
            grid.append(list(line.replace("\n", "")))
        arr = np.array(grid)
        count = 0
        for i in range(len(arr)-2):
            for j in range(len(arr[i])-2):
                check_s = arr[i][j] + arr[i+1][j+1] + arr[i+2][j+2]
                if check_s == "MAS" or check_s == "SAM":
                    check_back = arr[i+2][j] + arr[i+1][j+1] + arr[i][j+2]
                    if check_back == "MAS" or check_back == "SAM":
                        count += 1
        print(count)

part1()
part2()