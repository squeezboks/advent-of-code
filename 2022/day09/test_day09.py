from day09 import *

data_s1 = open("./2022/day09/test_day09_s1_data.txt").read().splitlines()
data_s2 = open("./2022/day09/test_day09_s2_data.txt").read().splitlines()

def test_build_tape():
    assert build_tape(data_s1) == ['R', 'R', 'R', 'R', 'U', 'U', 'U', 'U', 'L', 'L', 'L', 'D', 'R', 'R', 'R', 'R', 'D', 'L', 'L', 'L', 'L', 'L', 'R', 'R']

def test_update_tail():
    tail = (0,0)
    assert update_tail((0,0),tail) == (0,0)
    assert update_tail((0,1),tail) == (0,0)
    assert update_tail((1,0),tail) == (0,0)
    assert update_tail((1,1),tail) == (0,0)
    
    assert update_tail((2,0),tail) == (1,0)
    assert update_tail((0,0),tail) == (0,0)
    assert update_tail((1,1),tail) == (0,0)
    assert update_tail((1,-1),tail) == (0,0)

    assert update_tail((-2,0),tail) == (-1,0)
    assert update_tail((0,0),tail) == (0,0)
    assert update_tail((-1,1),tail) == (0,0)
    assert update_tail((-1,-1),tail) == (0,0)

    assert update_tail((2,1),tail) == (1,1)
    assert update_tail((0,1),tail) == (0,0)
    assert update_tail((1,2),tail) == (1,1)
    assert update_tail((1,0),tail) == (0,0)

    assert update_tail((0,-1),tail) == (0,0)
    assert update_tail((-2,-1),tail) == (-1,-1)
    assert update_tail((-1,0),tail) == (0,0)
    assert update_tail((-1,-2),tail) == (-1,-1)

def test_s1():
    assert s1(data_s1) == 13

def test_s2():
    assert s2(data_s2) == 36