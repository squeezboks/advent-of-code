import multiprocessing
from queue import PriorityQueue

def parse_input(input):
    data = input.split('\n\n')
    for row in data:
        print(row)

def s1(data):
    parse_input(data)
    return 'not solved'

def s2(data):
    return 'not solved'


# protect the entry point
if __name__ == '__main__':
    with open("./2022/day13/test_day13_data.txt") as f:
        data = f.read()
        print(f" s1: {s1(data)}")
    
    with open("./2022/day13/test_day13_data.txt") as f:
        data = f.read()
        print(f" s2: {s2(data)}")


    

