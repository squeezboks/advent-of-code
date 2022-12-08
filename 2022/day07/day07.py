def build_directory(lines):
    path = '[]'
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

def get_directory_size(path, memo, directory):
    size = 0
    for key, value in directory.items():
        if isinstance(value, dict):
            path = path + '/' + key
            memo[path] = get_directory_size(path, memo, value)
            size += memo[path]
        else:
            size += value
    return size

def change_path(current, new):
    match new:
        case '.' :
            return current
        case '..':
            return current[:-1]
        case '/':
            return ['/']
        case _:
            current.append(new)
            return current

def s1(data):
    root = build_directory(data)
    selected = []
    memo = dict()
    path = ''
    get_directory_size(path, memo, root)
    for value in memo.values():
        if value <= 100000:
            selected.append(value)
    return sum(selected)

def s2(data):
    root = build_directory(data)
    total_space = 70000000
    memo = dict()
    path = ''
    root_size = get_directory_size(path, memo, root)
    residual_space = total_space - root_size
    space_required = 30000000 - residual_space
    selected = root_size
    print(f"space required: {space_required}")
    for key, value in memo.items():
        if value >= space_required:
            selected = value if (value < selected) else selected
    return selected

with open("./2022/day07/day07_data.txt") as f:
    data = f.read().splitlines()
    print(f" s1: {s1(data)}")
    print(f" s2: {s2(data)}")
