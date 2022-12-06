from day06 import *

test_datastream1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
test_datastream2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
test_datastream3 = "nppdvjthqldpwncqszvftbrmjlhg"
test_datastream4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
test_datastream5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"


def test_s1():
    assert s1(test_datastream1) == 7
    assert s1(test_datastream2) == 5
    assert s1(test_datastream3) == 6
    assert s1(test_datastream4) == 10
    assert s1(test_datastream5) == 11

def test_s2():
    assert s2(test_datastream1) == 19
    assert s2(test_datastream2) == 23
    assert s2(test_datastream3) == 23
    assert s2(test_datastream4) == 29
    assert s2(test_datastream5) == 26
    pass