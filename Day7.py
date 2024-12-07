class BST:
    """
    A simple binary tree
    """
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
    """
    This function is kinda deprecated as you don't build up the tree, as you only need leafs
    but still it is nice for the understanding of my solution:
    We will traverse the tree and if you go to the left, you add the value to the parent one, if you go to the right you multiply it.
    This works as in this problem operator precedence is ignored and it is only left to right.
    :param values: The values which get accumulated on every new level of the tree
    :return: The final binary tree
    """
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
    """
    This function is the same as before, but we directly accumulate the leafs in the stack and safe runtime and storage
    Here we directly accumulate the values while we "build" up the tree
    :param values: The values which get accumulated on every new level of the tree
    :return: Leafs of the tree
    """
    stack = [values[0]]
    results = []
    counter = 0
    for v in values[1:]:
        next_stack = []
        counter += 1
        is_leaf = counter == len(values) - 1
        while len(stack) > 0:
            curr = stack.pop()
            next_stack.append(v + curr) # Instead of the values you can also add a BST(v+curr), but as we don't need the tree
            next_stack.append(v * curr) # we can safe storage and just accumulate the values
            if is_leaf:
                results.append(v + curr)
                results.append(v * curr)
        stack = next_stack
    return results

def parse_file():
    """
    :return: Dictionary with the wanted result of the equation and the numbers need to use
    """
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
    """
    Completely the same as part 1 except we have now a ternary tree with the | operator
    :param values: The values which get accumulated on every new level of the tree
    :return: The leafs of the tree
    """
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