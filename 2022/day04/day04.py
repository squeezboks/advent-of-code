def check_overlaps(elf1, elf2):
    combined = [min(elf1 + elf2), max(elf1 + elf2)]    
    return length(combined) <= length(elf1) + length(elf2)

def check_contains(elf1, elf2):
    combined = [min(elf1 + elf2), max(elf1 + elf2)] 
    return (length(combined) == length(elf1)) | (length(combined) == length(elf2))   

def length(x):
    return int(abs(x[0]-x[1]))

def s1(pair):
    pair = pair.strip().split(',')
    elf1 = [int(pair[0].split('-')[0]), int(pair[0].split('-')[1])]
    elf2 = [int(pair[1].split('-')[0]), int(pair[1].split('-')[1])]
    res = check_contains(elf1, elf2)
    return res

def s2(pair):
    pair = pair.strip().split(',')
    elf1 = [int(pair[0].split('-')[0]), int(pair[0].split('-')[1])]
    elf2 = [int(pair[1].split('-')[0]), int(pair[1].split('-')[1])]
    res = check_overlaps(elf1, elf2)
    return res

with open("./2022/day04/day04_test_data.txt") as f:
    lines = f.readlines()
    print(f" test s1: {sum(map(s1, lines))}")
    print(f" test s2: {sum(map(s2, lines))}")

with open("./2022/day04/day04_data.txt") as f:
    lines = f.readlines()
    print(f" s1: {sum(map(s1, lines))}")
    print(f" s2: {sum(map(s2, lines))}")
