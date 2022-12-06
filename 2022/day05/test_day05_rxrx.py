from day05 import parse_input
from day05_rxrx import *

def test_rxrx_apply_moves_9000():
    with open("./2022/day05/day05_test_data.txt") as f:
        lines = f.read().splitlines()
        stack, moves = parse_input(lines)
        result = rxrx_apply_moves_9000(stack, moves)
        assert result == [['C'],['M'],['P','D','N','Z']]
        
def test_rxrx_apply_moves_9001():
    with open("./2022/day05/day05_test_data.txt") as f:
        lines = f.read().splitlines()
        stack, moves = parse_input(lines)
        result = rxrx_apply_moves_9001(stack, moves)
        assert result == [['M'],['C'],['P','Z','N','D']]

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