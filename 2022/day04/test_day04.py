from day04 import check_overlaps, check_contains, s1, s2

def test_check_overlaps():
    assert check_overlaps([2,4],[6,8]) == False
    assert check_overlaps([2,3],[4,5]) == False
    assert check_overlaps([5,7],[7,9]) == True
    assert check_overlaps([2,8],[3,7]) == True
    assert check_overlaps([6,6],[4,6]) == True
    assert check_overlaps([2,6],[4,8]) == True

def test_check_contains():
    assert check_contains([2,4],[6,8]) == False
    assert check_contains([2,3],[4,5]) == False
    assert check_contains([5,7],[7,9]) == False
    assert check_contains([2,8],[3,7]) == True
    assert check_contains([6,6],[4,6]) == True
    assert check_contains([2,6],[4,8]) == False

def test_s1():
    pass

def test_s2():
    pass