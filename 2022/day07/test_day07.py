from day07 import *
'''
/ (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
'''

def test_build_directory():
    with open("./2022/day07/test_day07_data.txt") as f:
        lines = f.read().splitlines()
        result = build_directory(lines)
    assert result == {'/': {'a': {'e': {'i': 584}, 'f': 29116, 'g': 2557, 'h.lst': 62596}, 'b.txt': 14848514, 'c.dat': 8504156, 'd': {'j': 4060174, 'd.log': 8033020, 'd.ext': 5626152, 'k': 7214296}}}

def test_change_path():
    assert change_path(['a','b','c'],'.') == ['a','b','c']
    assert change_path(['a','b','c'],'..') == ['a','b']
    assert change_path(['a','b','c'],'/') == ['/']
    assert change_path(['a','b','c'],'d') == ['a','b','c','d']

def test_get_directory_size():
    assert get_directory_size('', dict(), {'e': {'i': 584}}) == 584
    assert get_directory_size('', dict(), {'a': {'e': {'i': 584}, 'f': 29116, 'g': 2557, 'h.lst': 62596}}) == 94853
    assert get_directory_size('', dict(), {'d': {'j': 4060174, 'd.log': 8033020, 'd.ext': 5626152, 'k': 7214296}}) == 24933642
    assert get_directory_size('', dict(), {'/': {'a': {'e': {'i': 584}, 'f': 29116, 'g': 2557, 'h.lst': 62596}, 'b.txt': 14848514, 'c.dat': 8504156, 'd': {'j': 4060174, 'd.log': 8033020, 'd.ext': 5626152, 'k': 7214296}}}) == 48381165

def test_s1():
    with open("./2022/day07/test_day07_data.txt") as f:
        lines = f.read().splitlines()
        assert s1(lines) == 95437

def test_s2():
    with open("./2022/day07/test_day07_data.txt") as f:
        lines = f.read().splitlines()
        assert s2(lines) == 24933642