
def build_forest(data):
    forest = []
    for row in data:
        forest.append([int(tree) for tree in row])
    return forest

def check_row_visibility(trees):
    vis = []
    big_tree = -1
    icu = 0

    for tree in trees:
        if tree > big_tree:
            big_tree = tree
            icu = 1
        else:
            icu = 0
        vis.append(icu)
    return vis

def check_array_visibility(forest):
    return [check_row_visibility(row) for row in forest]

def transpose(array):
    return [[array[j][i] for j in range(len(array))] for i in range(len(array[0]))]

def flip_lr(array):
    return [[element for element in reversed(row)] for row in array]

def flip_ud(array):
    return [row for row in reversed(array)]

def check_direction(forest, direction):
    match direction:
        case 'left':
            return check_array_visibility(forest)
        case 'right':
            return flip_lr(check_array_visibility(flip_lr(forest)))
        case 'top':
            return transpose(check_array_visibility(transpose(forest)))
        case 'bottom':
            return transpose(flip_lr(check_array_visibility(flip_lr(transpose(forest)))))
        case _:
            raise Exception("oh no, what happened??")

def get_forest_visibility(forest):
    num_row = len(forest)
    num_col = len(forest[0])
    vl = check_direction(forest, 'left')
    vr = check_direction(forest, 'right')
    vt = check_direction(forest, 'top')
    vb = check_direction(forest, 'bottom')
    return [[(vl[i][j] or vr[i][j] or vt[i][j] or vb[i][j]) for j in range(num_row)] for i in range(num_col)]

def get_row_col(i,j,array):
    j_row = array[j]
    i_col = [row[i] for row in array]
    return j_row, i_col

def get_view(i,j,array,direction):
    row, col = get_row_col(i,j,array)
    match direction:
        case 'left':
            return [e for e in reversed(row[:i])]
        case 'right':
            return row[(i+1):]
        case 'up':
            return [e for e in reversed(col[:j])]
        case 'down':
            return col[(j+1):]

def get_viewing_distance(i,j,array,direction):
    tree = array[j][i]
    view = get_view(i,j,array,direction)
    count = 0
    if view:
        for next_tree in view:
            count +=1
            if next_tree >= tree:
                return count
        return count
    else:
        return 0

def get_scenic_score(i,j,array):
    vl = get_viewing_distance(i,j,array,'left')
    vr = get_viewing_distance(i,j,array,'right')
    vu = get_viewing_distance(i,j,array,'up')
    vd = get_viewing_distance(i,j,array,'down')
    return vl*vr*vu*vd

def get_scenic_scores(forest):
    scores = []
    for j in range(len(forest)):
        row = []
        for i in range(len(forest[0])):
            row.append(get_scenic_score(i,j,forest))
        scores.append(row)
    return scores

def s1(data):
    forest = build_forest(data)
    visibility = get_forest_visibility(forest)
    return sum([sum(row) for row in zip(*visibility)])

def s2(data):
    forest = build_forest(data)
    scores = get_scenic_scores(forest)
    return max([max(row) for row in zip(*scores)])

with open("./2022/day08/day08_data.txt") as f:
    data = f.read().splitlines()
    print(f" s1: {s1(data)}")
    print(f" s2: {s2(data)}")
