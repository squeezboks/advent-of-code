def parse_input(lines):
    # find empty line to demarc state from instructions
    split_on = lines.index("")
    stack = parse_stack(lines[:split_on-1])
    instr = parse_moves(lines[split_on+1:])
    return stack, instr

def parse_stack(lines):
    # create container
    stack = []
    num_stacks = len(lines[0])//4 + 1
    for x in range(num_stacks):
        stack.append([])
    
    # build from the bottom
    for line in reversed(lines):
        for index, char in enumerate(line):
            if index % 4 == 1 and not char.isspace():
                stack[index//4].append(char)
    return stack

def parse_moves(lines):
    moves = []
    for line in lines:
        moves.append([int(i) for i in line.split() if i.isdigit()])
    return moves

def process_moves(stack, moves, crane):
    for move in moves:
        stack = apply_move(stack, move, crane)
    return stack

def apply_move(stack, move, crane):
    n = move[0]
    src_stack = move[1] - 1
    tgt_stack = move[2] - 1
    match crane:
        case 'CrateMover9000':
            for i in range(n):
                stack[tgt_stack].append(stack[src_stack].pop())
        case 'CrateMover9001':
            stack[tgt_stack].extend(stack[src_stack][-n:])
            del stack[src_stack][-n:]
    return stack

def s1(lines):
    stack, moves = parse_input(lines)
    stack = process_moves(stack, moves, 'CrateMover9000')
    res = "".join([col[-1] for col in stack])
    return res

def s2(lines):
    stack, moves = parse_input(lines)
    stack = process_moves(stack, moves, 'CrateMover9001')
    res = "".join([col[-1] for col in stack])
    return res

with open("./2022/day05/day05_data.txt") as f:
    lines = f.read().splitlines()
    print(f" s1: {s1(lines)}")
    print(f" s2: {s2(lines)}")
