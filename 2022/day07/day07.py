from collections import defaultdict

def pretty(d, indent=0):
    for key, value in d.items():
        if isinstance(value, dict):
            print(' ' * indent + f" - {key} (dir)")
            pretty(value, indent+1)
        else:
            print(' ' * indent + f" - {key} (file, size = {value})")


def build_tree(lines):
    path = []
    root = {'/': dict()}
    directory = root
    for line in lines:
        # process the line
        if line.startswith('$'):
            #user input
            if line.startswith('$ cd'):
                new = line.split()[2]
                # update current directory path
                path = change_path(path, new)
                # update working directory
                directory = root
                for i in path:
                    directory = directory[i]
        else:
            #system output, either files or dirs
            if line.startswith('dir'):
                directory[line.split()[1]] = dict()
            else:
                directory[line.split()[1]] = int(line.split()[0])
    return root

def change_path(current, new):
    if new == '..':
        current.pop()
    elif new == '/':
        current = ['/']
    else:
        current.append(new)
    return current

def parse_system_out(current, tree, line):
    pass

def s1(data):
    files = build_tree(data)
    pretty(files)

def s2(data):
    pass

with open("./2022/day07/test_day07_data.txt") as f:
    data = f.read().splitlines()
    print(f" s1: {s1(data)}")
    print(f" s2: {s2(data)}")
