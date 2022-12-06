from collections import deque

def s1(datastream):
    window = deque(maxlen=4)
    for index, char in enumerate(datastream):
        window.append(char)
        if len(set(window)) == 4:
            return index + 1
    raise Exception('no start of packet header')

def s2(datastream):
    window = deque(maxlen=14)
    for index, char in enumerate(datastream):
        window.append(char)
        if len(set(window)) == 14:
            return index + 1
    raise Exception('no start of message header')

with open("./2022/day06/day06_data.txt") as f:
    datastream = f.read()
    print(f" s1: {s1(datastream)}")
    print(f" s2: {s2(datastream)}")
