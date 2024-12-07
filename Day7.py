class BST:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    def get_val(self):
        return self.val
    def set_left(self, left):
        self.left = left
    def set_right(self, right):
        self.right = right
    def set_val(self, val):
        self.val = val

def build_binary_tree(values):
    tree = BST(values[0])
    stack = [tree]
    for v in values[1:]:
        next_stack = []
        while len(stack) > 0:
            curr = stack.pop()
            curr.left = BST(v)
            curr.right = BST(v)
            next_stack.append(curr.left)
            next_stack.append(curr.right)
        stack = next_stack
    return tree

def build_binary_tree_with_calc(values):
    stack = [values[0]]
    results = []
    counter = 0
    for v in values[1:]:
        next_stack = []
        counter += 1
        is_leaf = counter == len(values) - 1
        while len(stack) > 0:
            curr = stack.pop()
            next_stack.append(v + curr)
            next_stack.append(v * curr)
            if is_leaf:
                results.append(v + curr)
                results.append(v * curr)
        stack = next_stack
    return results

def parse_file():
    with open("input/Day7.txt") as f:
        equations = {}
        for line in f:
            wanted, eq = line.split(": ")
            equations[int(wanted)] = list(map(int, eq.split(" ")))
    return equations
def part1():
    equations = parse_file()
    acc = 0
    for eq in equations:
        results = build_binary_tree_with_calc(equations[eq])
        #print(eq, results)
        if eq in results:
            acc += eq
    print(acc)


def build_ternary_tree_with_calc(values):
    stack = [values[0]]
    results = []
    counter = 0
    for v in values[1:]:
        next_stack = []
        counter += 1
        is_leaf = counter == len(values) - 1
        while len(stack) > 0:
            curr = stack.pop()
            next_stack.append(v + curr)
            next_stack.append(int(str(curr) + str(v)))
            next_stack.append(v * curr)
            if is_leaf:
                results.append(v + curr)
                results.append(int(str(curr) + str(v)))
                results.append(v * curr)
        stack = next_stack
    return results

def part2():
    equations = parse_file()
    acc = 0
    for eq in equations:
        results = build_ternary_tree_with_calc(equations[eq])
        #print(eq, results)
        if eq in results:
            acc += eq
    print(acc)


part1()
part2()