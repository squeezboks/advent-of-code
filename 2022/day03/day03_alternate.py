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
    assert len(res) == 1
    return get_priority(res)

def s2(inventories):
    badges = []
    for i in range(0, len(inventories), 3):
        elf1 = set(inventories[i].strip())
        elf2 = set(inventories[i+1].strip())
        elf3 = set(inventories[i+2].strip())
        res = elf1 & elf2 & elf3
        assert len(res) == 1
        badges.append(get_priority(res.pop()))
    return sum(badges)

with open("day03_data.txt") as f:
    lines = f.readlines()
    print(f" s1: {sum(map(s1, lines))}")
    print(f" s2: {s2(lines)}")
