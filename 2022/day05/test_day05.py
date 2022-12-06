from day05 import *

def test_parse_stack():
    with open("./2022/day05/day05_test_data.txt") as f:
        lines = f.read().splitlines()
        split_on = lines.index("")
        result = parse_stack(lines[:split_on-1])
    assert result == [['Z','N'],['M','C','D'],['P']]

def test_parse_moves():
    with open("./2022/day05/day05_test_data.txt") as f:
        lines = f.read().splitlines()
        split_on = lines.index("")
        result = parse_moves(lines[split_on+1:])    
        assert result == [[1,2,1],[3,1,3],[2,2,1],[1,1,2]]

def test_process_moves():
    with open("./2022/day05/day05_test_data.txt") as f:
        lines = f.read().splitlines()
        split_on = lines.index("")
        
        stack = parse_stack(lines[:split_on-1])
        moves = parse_moves(lines[split_on+1:])
        result = process_moves(stack, moves, 'CrateMover9000')
        assert result == [['C'],['M'],['P','D','N','Z']]
        
        stack = parse_stack(lines[:split_on-1])
        moves = parse_moves(lines[split_on+1:])
        result = process_moves(stack, moves, 'CrateMover9001')
        assert result == [['M'],['C'],['P','Z','N','D']]

def test_apply_move():
    with open("./2022/day05/day05_test_data.txt") as f:
        lines = f.read().splitlines()
        
        split_on = lines.index("")
        
        stack = parse_stack(lines[:split_on-1])
        moves = parse_moves(lines[split_on+1:])
        result = apply_move(stack, moves[0], 'CrateMover9000')
        assert result == [['Z','N','D'],['M','C'],['P']]

        stack = parse_stack(lines[:split_on-1])
        moves = parse_moves(lines[split_on+1:])
        stack = apply_move(stack, moves[0], 'CrateMover9001')
        result = apply_move(stack, moves[1], 'CrateMover9001')
        assert result == [[],['M','C'],['P','Z','N','D']]

def test_s1():
    with open("./2022/day05/day05_test_data.txt") as f:
        lines = f.read().splitlines()
        result = s1(lines)
        assert result == 'CMZ'

def test_s2():
    with open("./2022/day05/day05_test_data.txt") as f:
        lines = f.read().splitlines()
        result = s2(lines)
        assert result == 'MCD'