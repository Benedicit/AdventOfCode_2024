import re
from PIL import Image

width = 101
height = 103
middle_hor = width // 2
middle_ver = height // 2
def part1(duration=100, print_part1=False):
    """
    We always move around the algebraic ring of width and height. So one duration can be computed in O(1) using mod.
    :param duration: how many seconds have passed
    :return: list of all robot positions
    """
    robots = []
    with open("input/Day14.txt") as f:
        for line in f:
            coordinates = re.findall(r"[-0-9]+,[-0-9]+", line)
            start, end = coordinates[0].split(",")
            mov_x, mov_y = coordinates[1].split(",")
            robots.append((int(start), int(end), int(mov_x), int(mov_y)))
    top_left = 0
    top_right = 0
    bottom_left = 0
    bottom_right = 0
    all_robots = []
    for start_x, start_y, mov_x, mov_y in robots:
        result_x = (start_x + mov_x * duration) % width
        result_y = (start_y + mov_y * duration) % height
        all_robots.append((result_x, result_y))
        if result_x < middle_hor and result_y < middle_ver:
            top_left += 1
        elif result_x > middle_hor and result_y > middle_ver:
            bottom_right += 1
        elif result_x < middle_hor and result_y > middle_ver:
            bottom_left += 1
        elif result_x > middle_hor and result_y < middle_ver:
            top_right += 1
    result = top_left * top_right * bottom_left * bottom_right
    if print_part1:
        print(result)
    return all_robots

def part2():
    """
    Scrolling through the file manager is one solution
    """
    for i in range(5000,10000):
        robots = part1(duration=i)
        img = Image.new("RGB", (width, height), (0, 0, 0))
        pixels = img.load()
        for x,y in robots:
            pixels[x, y] = (255, 255, 255)
        img.save(f"input/Day14_images/{i}.png")
part1(print_part1=True)
part2()



