import re

def parse_input(data):
    regex = r"""(?:Monkey (?P<monkey>\S+):\n.*Starting items: (?P<items>.+)\n.*Operation: new = old (?P<operation>.+)\n.*Test: divisible by (?P<test>.+)\n.*If true: throw to monkey (?P<case_true>.+)\n.*If false: throw to monkey (?P<case_false>.+))"""
    matches = re.finditer(regex, data)
    monkeys = []
    for match in matches:
        monkey = dict()
        monkey['id'] = int(match.groups()[0])
        monkey['items'] = [int(i) for i in match.groups()[1].replace(",","").split()]
        monkey['operation'] = match.groups()[2].split()
        monkey['test'] = [int(match.groups()[3]),int(match.groups()[4]),int(match.groups()[5])]
        monkeys.append(monkey)
    return monkeys

def inspecting(worry, operation):
    match operation[0]:
        case '+':
            if operation[1] == 'old':
                return worry + worry
            else:
                return worry + int(operation[1])
        case '*':
            if operation[1] == 'old':
                return worry * worry
            else:
                return worry * int(operation[1])

def testing(worry, test):
    return (test[1] * int(not(worry%test[0]))) + (test[2] * int(bool(worry%test[0])))

def business(monkeys):
    for monkey in monkeys:
        while monkey['items']:
            item = monkey['items'].pop(0)
            item = inspecting(item, monkey['operation'])
            item = int((item/3)//1)
            target_monkey = testing(item, monkey['test'])
            monkeys[target_monkey]['items'].append(item)
    return monkeys

def s1(data):
    monkeys = parse_input(data)
    monkeys = business(monkeys)
    for monkey in monkeys:
        print(f"Monkey {monkey['id']}: {monkey['items']}")
    pass

def s2(data):
    pass

with open("./2022/day11/test_day11_data.txt") as f:
    data = f.read()
    print(f" s1: {s1(data)}")

with open("./2022/day11/test_day11_data.txt") as f:
    data = f.read()
    print(f" s2: {s2(data)}")
