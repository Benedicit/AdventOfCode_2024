
class Gate:
    def __init__(self, x, y, z, gate):
        self.in1 = x
        self.in2 = y
        self.out = z
        self.gate = gate
        self.eval = False

gates = set()
inputs = {}
second_order = {}
start_gates = []
with open("input/Day24.txt") as f:
    get_gates = False
    for line in f:
        line = line.strip()
        if line == "":
            get_gates = True
            continue
        if get_gates:
            parts = line.split(" ")
            in1 = parts[0]
            in2 = parts[2]
            out = parts[4]
            inputs[out] = 0, False
            gates.add(Gate(in1, in2, out, parts[1]))
            if (in1.startswith("x") or in1.startswith("y")) and (in2.startswith("x") or in2.startswith("y")):
                start_gates.append((in1, in2))
        else:
            signal, value = line.split(": ")
            inputs[signal] = int(value), True

def part1(current_gates):
    """
    I iterate over all gates 46 times and only update the ones which couldn't be set before.
    :param current_gates: the gates of the graph
    :return:
    """
    for _ in range(47): # it needs 46 cycles to finish
        for g in current_gates:
            x = g.in1
            y = g.in2
            next_gate = g.out
            gate_eval = g.eval
            gate = g.gate
            if gate_eval:
                continue
            v1, v1_eval = inputs[x]
            v2, v2_eval = inputs[y]
            if v1_eval and v2_eval:
                match gate:
                    case "OR":
                        inputs[next_gate] = v1 | v2, True
                    case "AND":
                        inputs[next_gate] = v1 & v2, True
                    case "XOR":
                        inputs[next_gate] = v1 ^ v2, True
                g.eval = True
    result_keys = list(filter(lambda a: "z" in a, inputs.keys()))
    result_keys.sort()
    result = ""
    for z in result_keys:
        result = str(inputs[z][0]) + result
    int_result = int(result,2)
    print(int_result)
    return int_result

part1(gates)
part2 = ["nhn", "tvb", "z12", "vdc", "khg", "z21", "gst", "z33"] # I manually checked the gate-graph
part2.sort()
print(",".join(part2))