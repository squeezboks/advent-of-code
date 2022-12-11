from day11 import parse_input, business, terrible_business, s1, s2
from collections import deque

def test_parse_input():
    data = open("./2022/day11/test_day11_data.txt").read()
    monkeys = parse_input(data)
    assert monkeys[0]['id'] == 0
    assert monkeys[0]['items'] == deque([79, 98])
    assert monkeys[0]['operation'] == ['*', '19']
    assert monkeys[0]['test'] == [23,2,3]
    assert len(monkeys) == 4

def test_business():
    data = open("./2022/day11/test_day11_data.txt").read()
    monkeys = parse_input(data)
    # round 1
    monkeys = business(monkeys)
    assert monkeys[0]['items'] == deque([20, 23, 27, 26])
    assert monkeys[1]['items'] == deque([2080, 25, 167, 207, 401, 1046])
    assert monkeys[2]['items'] == deque([])
    assert monkeys[3]['items'] == deque([])
    # round 2
    monkeys = business(monkeys)
    # round 3
    monkeys = business(monkeys)
    # round 4
    monkeys = business(monkeys)
    # round 5
    monkeys = business(monkeys)
    assert monkeys[0]['items'] == deque([15, 17, 16, 88, 1037])
    assert monkeys[1]['items'] == deque([20, 110, 205, 524, 72])
    assert monkeys[2]['items'] == deque([])
    assert monkeys[3]['items'] == deque([])

def test_terrible_business():
    # 1 round
    data = open("./2022/day11/test_day11_data.txt").read()
    monkeys = parse_input(data)
    for _ in range(1):
        monkeys = terrible_business(monkeys)
    assert monkeys[0]['inspections'] == 2
    assert monkeys[1]['inspections'] == 4
    assert monkeys[2]['inspections'] == 3
    assert monkeys[3]['inspections'] == 6
    # 20 rounds
    data = open("./2022/day11/test_day11_data.txt").read()
    monkeys = parse_input(data)
    for _ in range(20):
        monkeys = terrible_business(monkeys)
    assert monkeys[0]['inspections'] == 99
    assert monkeys[1]['inspections'] == 97
    assert monkeys[2]['inspections'] == 8
    assert monkeys[3]['inspections'] == 103
    # 1000 rounds
    data = open("./2022/day11/test_day11_data.txt").read()
    monkeys = parse_input(data)
    for _ in range(1000):
        monkeys = terrible_business(monkeys)
    assert monkeys[0]['inspections'] == 5204
    assert monkeys[1]['inspections'] == 4792
    assert monkeys[2]['inspections'] == 199
    assert monkeys[3]['inspections'] == 5192
    # 2000 rounds
    data = open("./2022/day11/test_day11_data.txt").read()
    monkeys = parse_input(data)
    for _ in range(2000):
        monkeys = terrible_business(monkeys)
    assert monkeys[0]['inspections'] == 10419
    assert monkeys[1]['inspections'] == 9577
    assert monkeys[2]['inspections'] == 392
    assert monkeys[3]['inspections'] == 10391
    # 5000 rounds
    data = open("./2022/day11/test_day11_data.txt").read()
    monkeys = parse_input(data)
    for _ in range(5000):
        monkeys = terrible_business(monkeys)
    assert monkeys[0]['inspections'] == 26075
    assert monkeys[1]['inspections'] == 23921
    assert monkeys[2]['inspections'] == 974
    assert monkeys[3]['inspections'] == 26000
    # 10000 rounds
    data = open("./2022/day11/test_day11_data.txt").read()
    monkeys = parse_input(data)
    for _ in range(10000):
        monkeys = terrible_business(monkeys)
    assert monkeys[0]['inspections'] == 52166
    assert monkeys[1]['inspections'] == 47830
    assert monkeys[2]['inspections'] == 1938
    assert monkeys[3]['inspections'] == 52013
    

def test_s1():
    data = open("./2022/day11/test_day11_data.txt").read()
    assert s1(data) == 10605

def test_s2():
    data = open("./2022/day11/test_day11_data.txt").read()
    assert s2(data) == 2713310158