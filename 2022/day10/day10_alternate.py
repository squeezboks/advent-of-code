def s1(data):
    data = [1] + [int(i) for i in data.replace('noop','0').replace('addx', '0').split()]
    print(sum([(i+1)*(sum(data[:(i+1)])) for i, _ in enumerate(data) if ((i+1) == 20 or not ((i-19) % 40))]))

def s2(data):
    data = [int(i) for i in data.replace('noop','0').replace('addx', '0').split()]
    sprite = "###....................................."
    for i, x in enumerate(data):
        print(sprite[(i%40)], end="") if (i+1)%40 != 0 else print(sprite[(i%40)])
        sprite = sprite[(-1*x):] + sprite[:(-1*x)]

with open("./2022/day10/day10_data.txt") as f:
    data = f.read()
    s1(data)

with open("./2022/day10/day10_data.txt") as f:
    data = f.read()
    s2(data)
