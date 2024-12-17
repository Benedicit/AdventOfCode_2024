
registers = {}
code = []

def get_op(x):
    if 0<=x<=3:
        return x
    elif x==4:
        return registers["A"]
    elif x==5:
        return registers["B"]
    elif x==6:
        return registers["C"]
    elif x==7:
        print("That is illegal")
        return 10000

def div_a(op):
    return registers["A"] // (2 ** op)

with open("input/Day17.txt") as f:
    for line in f:
        line = line.strip().replace("Register ","").replace("Program: ","")
        if line == "":
            continue
        if "A" in line or "B" in line or "C" in line:
            r, n = line.split(": ")
            registers[r] = int(n)
        else:
            code = line.split(",")
            code = list(map(int, code))

def part1(print_r):
    inst = 0
    end_prog = len(code) -1
    instructions = ""
    result = []
    while inst < end_prog:
        # Program: 2,4,1,1,7,5,1,5,4,3,0,3,5,5,3,0
        # First iterations: 2,1,7,1,4,0,out,jmp
        op = code[inst+1]
        instr = code[inst]
        match instr:
            case 0:
                op = get_op(op)
                registers["A"] = div_a(op)
                instructions += " adv"
            case 1:
                registers["B"] ^= op
                instructions += " bxl"
            case 2:
                registers["B"] = get_op(op) & 7
                instructions += " bst"
            case 3:
                if registers["A"] != 0:
                    inst = op
                    instructions += " jnz"
                    continue
            case 4:
                registers["B"] = registers["B"] ^ registers["C"]
                instructions += " bxc"
            case 5:
                temp = get_op(op) & 7
                result.append(str(temp))
                instructions += " out"
            case 6:
                op = get_op(op)
                registers["B"] = div_a(op)
                instructions += " bdv"
            case 7:
                op = get_op(op)
                registers["C"] = div_a(op)
                instructions += " cdv"
        inst += 2
    result_str = ",".join(result)
    if print_r:
        print(result_str)
        print(instructions)
    return result_str

def part2():
    """
    Well I manually changed the number, for each digit of the octal number. Each digit responds to one number of the output.
    Start with the last number of the input, increase the current by one till it matches, then go the next digit.
    It can happen that the wanted output number is not reached, if so you need to backtrack to the digit before and increase
    it again till it reaches again the responding number, if that is now impossible backtrack further.
    TODO: Convert this algorithm to code
    """
    # Program: 2,4,1,1,7,5,1,5,4,3,0,3,5,5,3,0
    # Program: 0,3,5,4,3,0
    start = 0o4532306073267275

    #print(start)
    #end = 8 ** 17
    temp = format(start, "d")
    #print(temp)
    target = code.copy()
    target = ",".join(list(map(str,target)))
    end = start +1
    #start = 8 ** 15
    while start<end:
        registers["A"] = start
        registers["B"] = 0
        registers["C"] = 0
        curr = part1(False)
        print(curr,"    ",len(curr.replace(",","")))
        if curr == target:
            print(start)
            break
        start += 1

#part1(True)
part2()
