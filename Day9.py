def get_disk():
    """
    Because of part two there is now also the highest id+1 and the length of all files returned. In part 1 they are ignored.
    '.' = -1 because all inputs are non-negative, so it is easy to filter them out.
    :return: final disk_space, dictionary length_space, id
    """
    with open("input/Day9.txt") as f:
        for line in f:
            disk = list(line.strip())
    id = 0
    free_space = False
    disk_with_space = []
    length_space = {}
    for c in disk:
        if free_space:
            disk_with_space += [-1] * int(c)
            free_space = False
        else:
            disk_with_space += [id] * int(c)
            length_space[id] = int(c)
            id += 1
            free_space = True
    return list(disk_with_space), length_space, id
def part1():
    """
    Just start from the end for the numbers to be swapped and start from the beginning for the free spaces
    """
    disk_with_space,_,_ = get_disk()
    idx_free_space = 0
    idx_occupied = len(disk_with_space) - 1
    while idx_free_space < idx_occupied:
        while disk_with_space[idx_free_space] != -1 and idx_free_space < idx_occupied:
            idx_free_space += 1
        while disk_with_space[idx_occupied] == -1 and idx_free_space < idx_occupied:
            idx_occupied -= 1
        disk_with_space[idx_free_space], disk_with_space[idx_occupied] = disk_with_space[idx_occupied], disk_with_space[idx_free_space]
    checksum = 0
    for i in range(len(disk_with_space)):
        if disk_with_space[i] == -1:
            continue
        checksum += int(disk_with_space[i]) * i
    print(checksum)
    #print(disk_with_space)

def part2():
    """
    It is an unoptimized O(n^2) solution. Where we get the start of the file and then check if there is somewhere free
    space where we can swap it to.
    """
    disk_with_space, length_space, id = get_disk()
    for i in range(1, id):
        s_id = id - i
        occupied_l = length_space[s_id]
        idx_occupied = disk_with_space.index(s_id)
        start_free = 0
        while start_free < len(disk_with_space) and start_free < idx_occupied - occupied_l:
            while disk_with_space[start_free] != -1:
                start_free += 1
            end_free = start_free + 1
            while end_free < len(disk_with_space) and disk_with_space[end_free] == -1:
                end_free += 1
            free_space = end_free - start_free
            if end_free > idx_occupied:
                break
            if free_space >= occupied_l:
                disk_with_space[start_free:start_free+occupied_l], disk_with_space[idx_occupied:idx_occupied+occupied_l] = (
                    disk_with_space[idx_occupied:idx_occupied+occupied_l], disk_with_space[start_free:start_free+occupied_l])
                break
            start_free = end_free
    checksum = 0
    for i in range(len(disk_with_space)):
        if disk_with_space[i] == -1:
            continue
        checksum += int(disk_with_space[i]) * i
    print(checksum)
    #print(disk_with_space)

part1()
part2()
