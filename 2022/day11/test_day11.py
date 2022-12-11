from day11 import parse_input

def test_parse_input():
    data = open("./2022/day11/test_day11_data.txt").read()
    monkeys = parse_input(data)
    assert monkeys[0]['id'] == 0
    assert monkeys[0]['items'] == [79, 98]
    assert monkeys[0]['operation'] == ['*', '19']
    assert monkeys[0]['test'] == [23,2,3]

def test_s1():
    data = open("./2022/day11/test_day11_data.txt").read()
    pass

def test_s2():
    data = open("./2022/day11/test_day11_data.txt").read()
    pass