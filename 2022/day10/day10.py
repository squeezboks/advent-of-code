def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def process_instr(instr, history):
    cycle = history['cycle'][-1] + 1
    x = history['x'][-1]
    if is_number(instr):
        x = x + int(instr)
    history['cycle'].append(cycle)
    history['x'].append(x)
    return history

def get_signal_strength(cycle, history):
    index = history['cycle'].index(cycle)
    return history['x'][index]*cycle

def display_msg(instr, history):
    cycle = history['cycle'][-1]
    posn = ((cycle-1) % 40)
    row = ((cycle-1) // 40)
    history['crt'][row].append(history['sprite'][posn])
    if is_number(instr):
        move = -1 * int(instr)
        history['sprite'] = history['sprite'][move:] + history['sprite'][:move]
    history['cycle'].append(history['cycle'][-1] + 1)
    return history

def render_crt(data):
    crt = ""
    for row in data:
        line = "".join(row)
        crt = crt + line + "\n"
    return crt

def s1(data):
    history = {'cycle':[1], 'x':[1]}
    signal_strength = []
    while data:
        instr = data.pop(0)
        history = process_instr(instr, history)
    
    for index, cycle in enumerate(history['cycle']):
        if cycle == 20 or not ((cycle-20) % 40):
            x = history['x'][index]
            signal_strength.append(cycle * x)
    
    return sum(signal_strength)

def s2(data):
    history = {
        'cycle':[1], 
        'sprite':'###.....................................',
        'crt':[[],[],[],[],[],[]]
        }
    
    for instr in data:
        history = display_msg(instr, history)

    return render_crt(history['crt'])

with open("./2022/day10/day10_data.txt") as f:
    data = f.read().split()
    print(f" s1: {s1(data)}")

with open("./2022/day10/day10_data.txt") as f:
    data = f.read().split()
    print(f" s2:")
    print(s2(data))
