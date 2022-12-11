from day10 import *

def test_process_instr():
    history = {'cycle':[1], 'x':[1]}
    instr = 'noop'
    history = process_instr(instr, history)
    assert history == {'cycle':[1,2], 'x':[1,1]}

    instr = 'addx'
    history = process_instr(instr, history)
    assert history == {'cycle':[1,2,3], 'x':[1,1,1]}

    instr = 3
    history = process_instr(instr, history)
    assert history == {'cycle':[1,2,3,4], 'x':[1,1,1,4]}

def test_get_signal_strength():
    history = {'cycle':[1,2,3,4,5,6], 'x':[1,1,1,4,4,-1]}
    assert get_signal_strength(1, history) == 1
    assert get_signal_strength(4, history) == 16
    assert get_signal_strength(6, history) == -6

def test_process_instr_long():
    history = {'cycle':[1], 'x':[1]}
    data = open("./2022/day10/test_day10_data_02.txt").read().split()
    while data:
        instr = data.pop(0)
        history = process_instr(instr, history)
    assert get_signal_strength(20, history) == 420
    assert get_signal_strength(60, history) == 1140
    assert get_signal_strength(100, history) == 1800
    assert get_signal_strength(140, history) == 2940
    assert get_signal_strength(180, history) == 2880
    assert get_signal_strength(220, history) == 3960


def test_s1():
    data = open("./2022/day10/test_day10_data_02.txt").read().split()
    assert s1(data) == 13140

def test_s2():
    data = open("./2022/day10/test_day10_data_02.txt").read().split()
    screen = "".join(["##..##..##..##..##..##..##..##..##..##..\n","###...###...###...###...###...###...###.\n","####....####....####....####....####....\n","#####.....#####.....#####.....#####.....\n","######......######......######......####\n","#######.......#######.......#######.....\n"])
    assert s2(data) == screen