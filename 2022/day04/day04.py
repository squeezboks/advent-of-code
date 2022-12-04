def get_priority(item):
    item = ord(item)
    priority = item - 96 if item > 90 else item - 38
    return priority

def s1(inventory):
    inventory = inventory.strip()
    num_items = len(inventory)
    compartment1 = set(inventory[:num_items//2])
    compartment2 = set(inventory[num_items//2:])
    res, = compartment1 & compartment2
    return get_priority(res)

def s2(group):
    elf1 = set(group[0].strip())
    elf2 = set(group[1].strip())
    elf3 = set(group[2].strip())
    res, = elf1 & elf2 & elf3
    return get_priority(res)

with open("./2022/day03/day03_data.txt") as f:
    lines = f.readlines()
    print(f" s1: {sum(map(s1, lines))}")
    print(f" s2: {sum(map(s2, [lines[i:i+3] for i in range(0, len(lines), 3)]))}")
