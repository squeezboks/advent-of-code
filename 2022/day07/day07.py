from collections import defaultdict

def build_tree(lines):
    path = []
    root = dict()
    directory = root
    print(f'current path is: {path}')
    for line in lines:
        # process the line
        if line.startswith('$'):
            #user input
            if line.startswith('$ cd'):
                new = line.split()[2]
                # update current directory path
                path = change_directory(path, new)
                print(root)
            elif line.startswith('$ ls'):
                #user input, ls
                print(f"user listing contents of {path}")
                # create a new dict for the directory
                directory[path[-1]] = dict()
                # switch to that new dict
                directory = directory[path[-1]]
        else:
            #system output, either files or dirs
            print(f" - system output > {line}")
            if line.startswith('dir'):
                directory[line.split()[1]] = dict()
            else:
                directory[line.split()[1]] = int(line.split()[0])
    return directory

def rxrx_build_tree(current, directory, lines):
    print(f'current path is: {current}')
    print(f'current dir contents are: {directory}')
    if not lines:
        # no lines left, return
        return directory
    else:
        # process the line, update the tree and call the function again
        line = lines.pop(0)
        if line.startswith('$ cd '):
            #user input, cd
            new = line.split()[2]
            current = change_directory(current, new)
            directory[current[-1]] = dict()
            directory = directory[current[-1]]
        elif line.startswith('$ ls'):
            #user input, ls
            print(f"user listing contents of {current}")
        else:
            #system output, either files or dirs
            print(f" - system output > {line}")
            if line.startswith('dir'):
                directory[line.split()[1]] = dict()
            else:
                directory[line.split()[1]] = int(line.split()[0])
        return rxrx_build_tree(current, directory, lines)

def change_directory(current, new):
    if new == '..':
        old = current.pop()
        new = current[-1]
        print(f">> user changing directory from {old} to {new}")
    elif new == '/':
        current = ['/']
        print(f">> user changing directory to root")
    else:
        old = current
        current.append(new)
        print(f">> user changing directory from {old} to {new}")
    
    return current

def parse_system_out(current, tree, line):
    pass

def s1(data):
    files = dict()
    current = ['/']
    files[current[-1]] = dict()
    #files = rxrx_build_tree(current, files, data)
    files = build_tree(data)
    print(files)

def s2(data):
    pass

with open("./2022/day07/test_day07_data.txt") as f:
    data = f.read().splitlines()
    print(f" s1: {s1(data)}")
    print(f" s2: {s2(data)}")
