from itertools import combinations, chain

nodes = {}
with open("input/Day23.txt") as f:
    for line in f:
        c1,c2 = line.strip().split("-")
        if c1 not in nodes:
            nodes[c1] = {c2}
        else:
            nodes[c1].add(c2)
        if c2 not in nodes:
            nodes[c2] = {c1}
        else:
            nodes[c2].add(c1)

def part1():
        temp = set()
        for c in nodes:
            if not c.startswith("t"):
                continue
            current = nodes[c]
            for a,b in combinations(current, 2):
                A = nodes[a]
                B = nodes[b]
                x = [a, b, c]
                x.sort()
                x = tuple(x)
                if b in A and a in B and x not in temp:
                    temp.add(x)
        print(len(temp))
        fully_connected = []
        for n in nodes:
            nodes[n].add(n)
        for c in nodes:
            current = nodes[c]
            full = current
            full.add(c)
            subset = set()
            for x in powerset(current):
                p = set(x)
                every = True
                for z in list(x):
                    if p - nodes[z] != set():
                        every = False
                        break
                if every and len(p)> len(subset):
                    subset = p
            current.add(c)
            if len(subset) > len(fully_connected):
                fully_connected = subset
        fully_connected = list(fully_connected)
        fully_connected.sort()
        result = ",".join(fully_connected)
        print(result)

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))
part1()