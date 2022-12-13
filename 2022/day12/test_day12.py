from day12 import parse_input, Topomap

def test_parse_input():
    data = open("./2022/day12/test_day12_data.txt").read()
    assert parse_input(data) == {'grid': Grid('SabqponmabcryxxlaccszExkacctuvwjabdefghi', 8, 40), 'src':0, 'tgt':21}

def test_neighbours():
    data = open("./2022/day12/test_day12_data.txt").read()
    topomap = Topomap(data)

def test_s1():
    data = open("./2022/day12/test_day12_data.txt").read()
    pass

def test_s2():
    data = open("./2022/day12/test_day12_data.txt").read()
    pass