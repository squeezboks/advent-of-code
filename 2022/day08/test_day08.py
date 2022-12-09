from day08 import *
'''
30373
25512
65332
33549
35390
'''
DATA = open("./2022/day08/test_day08_data.txt").read().splitlines()

def test_build_forest():
    assert build_forest(DATA) == [
        [3,0,3,7,3],
        [2,5,5,1,2],
        [6,5,3,3,2],
        [3,3,5,4,9],
        [3,5,3,9,0]
        ]

def test_check_row_visibility():
    assert check_row_visibility([3,0,3,7,3]) == [1,0,0,1,0]
    assert check_row_visibility([2,5,5,1,2]) == [1,1,0,0,0]
    assert check_row_visibility([6,5,3,3,2]) == [1,0,0,0,0]
    assert check_row_visibility([3,3,5,4,9]) == [1,0,1,0,1]
    assert check_row_visibility([3,5,3,9,0]) == [1,1,0,1,0]

def test_check_array_visibility():
    assert check_array_visibility(build_forest(DATA)) == [
        [1,0,0,1,0],
        [1,1,0,0,0],
        [1,0,0,0,0],
        [1,0,1,0,1],
        [1,1,0,1,0]
        ]

def test_transpose():
    assert transpose(build_forest(DATA)) == [
        [3,2,6,3,3],
        [0,5,5,3,5],
        [3,5,3,5,3],
        [7,1,3,4,9],
        [3,2,2,9,0]
        ]

def test_flip_lr():
    assert flip_lr(build_forest(DATA)) == [
        [3,7,3,0,3],
        [2,1,5,5,2],
        [2,3,3,5,6],
        [9,4,5,3,3],
        [0,9,3,5,3]
        ]

def test_check_direction():
    assert check_direction(build_forest(DATA), 'left') == [
        [1,0,0,1,0],
        [1,1,0,0,0],
        [1,0,0,0,0],
        [1,0,1,0,1],
        [1,1,0,1,0]
        ]

    assert check_direction(build_forest(DATA), 'right') == [
        [0,0,0,1,1],
        [0,0,1,0,1],
        [1,1,0,1,1],
        [0,0,0,0,1],
        [0,0,0,1,1]
        ]

    assert check_direction(build_forest(DATA), 'top') == [
        [1,1,1,1,1],
        [0,1,1,0,0],
        [1,0,0,0,0],
        [0,0,0,0,1],
        [0,0,0,1,0]
        ]

    assert check_direction(build_forest(DATA), 'bottom') == [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [1,0,0,0,0],
        [0,0,1,0,1],
        [1,1,1,1,1]
        ]

def test_get_row_col():
    array = [
        [3,0,3,7,3],
        [2,5,5,1,2],
        [6,5,3,3,2],
        [3,3,5,4,9],
        [3,5,3,9,0]
        ]
    row, col = get_row_col(0,0,array)
    assert row == [3,0,3,7,3]
    assert col == [3,2,6,3,3]

    row, col = get_row_col(2,3,array)
    assert row == [3,3,5,4,9]
    assert col == [3,5,3,5,3]

def test_get_view():
    array = [
        [3,0,3,7,3],
        [2,5,5,1,2],
        [6,5,3,3,2],
        [3,3,5,4,9],
        [3,5,3,9,0]
        ]
    assert get_view(2,1,array,'left') == [5,2]
    assert get_view(2,1,array,'right') == [1,2]
    assert get_view(2,1,array,'up') == [3]
    assert get_view(2,1,array,'down') == [3,5,3]

    assert get_view(0,0,array,'left') == []
    assert get_view(0,0,array,'right') == [0,3,7,3]

def test_get_viewing_distance():
        array = [
        [3,0,3,7,3],
        [2,5,5,1,2],
        [6,5,3,3,2],
        [3,3,5,4,9],
        [3,5,3,9,0]
        ]

        i = 2
        j = 1
        assert get_viewing_distance(i,j,array,'left') == 1
        assert get_viewing_distance(i,j,array,'right') == 2
        assert get_viewing_distance(i,j,array,'up') == 1
        assert get_viewing_distance(i,j,array,'down') == 2

        i = 2
        j = 3
        assert get_viewing_distance(i,j,array,'left') == 2
        assert get_viewing_distance(i,j,array,'right') == 2
        assert get_viewing_distance(i,j,array,'up') == 2
        assert get_viewing_distance(i,j,array,'down') == 1

def test_get_scenic_score():
    array = [
        [3,0,3,7,3],
        [2,5,5,1,2],
        [6,5,3,3,2],
        [3,3,5,4,9],
        [3,5,3,9,0]
        ]
    assert get_scenic_score(2,1,array) == 4
    assert get_scenic_score(2,3,array) == 8

def test_get_scenic_scores():
    array = [
        [3,0,3,7,3],
        [2,5,5,1,2],
        [6,5,3,3,2],
        [3,3,5,4,9],
        [3,5,3,9,0]
        ]
    assert get_scenic_scores(array) == [
        [0,0,0,0,0],
        [0,1,4,1,0],
        [0,6,1,2,0],
        [0,1,8,3,0],
        [0,0,0,0,0]
    ]


def test_s1():
    with open("./2022/day08/test_day08_data.txt") as f:
        lines = f.read().splitlines()
        assert s1(lines) == 21

def test_s2():
    with open("./2022/day08/test_day08_data.txt") as f:
        lines = f.read().splitlines()
        assert s2(lines) == 8