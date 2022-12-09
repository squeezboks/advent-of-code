def process_moves(moves, rope):
    for move in moves:
        for index, knot in enumerate(rope):
            if index == 0:
                # process da move
                prev_head = rope[index][-1]
                match move:
                    case 'R':
                        head = (prev_head[0]+1, prev_head[1])
                    case 'L':
                        head = (prev_head[0]-1, prev_head[1])
                    case 'U':
                        head = (prev_head[0], prev_head[1]+1)
                    case 'D':
                        head = (prev_head[0], prev_head[1]-1)
                    case _:
                        raise Exception("well dang, that ain't a move")
                rope[index].append(head)
            else:
                # knot is tail knot
                tail = update_tail(rope[index-1][-1], rope[index][-1])
                rope[index].append(tail)
    return rope

def update_tail(head, tail):
    vect = (head[0]-tail[0], head[1]-tail[1])
    norm = (
        vect[0]/abs(vect[0]) if abs(vect[0]) != 0 else 0, 
        vect[1]/abs(vect[1]) if abs(vect[1]) != 0 else 0
        )
    if sum([ele*ele for ele in vect]) > 2:
        tail = (tail[0] + norm[0], tail[1]+norm[1])
    return tail

def build_tape(data):
    return [*"".join([line.split()[0]*int(line.split()[1]) for line in data])]

def s1(data):
    moves = build_tape(data)
    rope = [[(0,0)] for i in range(2)]
    rope = process_moves(moves, rope)
    return len(set(rope[1]))

def s2(data):
    moves = build_tape(data)
    rope = [[(0,0)] for i in range(10)]
    rope = process_moves(moves, rope)
    return len(set(rope[-1]))

with open("./2022/day09/day09_data.txt") as f:
    data = f.read().splitlines()
    print(f" s1: {s1(data)}")
with open("./2022/day09/day09_data.txt") as f:
    data = f.read().splitlines()
    print(f" s2: {s2(data)}")
