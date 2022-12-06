def s1(datastream):
    exit = False
    pos = 0
    while not exit:
        unique_char = len(set(datastream[pos:pos+4]))
        if unique_char != 4:
            pos += 1
            exit = False
        else:
            exit = True
    return (pos+4)

def s2(datastream):
    exit = False
    pos = 0
    while not exit:
        unique_char = len(set(datastream[pos:pos+14]))
        if unique_char != 14:
            pos += 1
            exit = False
        else:
            exit = True
    return (pos+14)

with open("./2022/day06/day06_data.txt") as f:
    datastream = f.read()
    print(f" s1: {s1(datastream)}")
    print(f" s2: {s2(datastream)}")
