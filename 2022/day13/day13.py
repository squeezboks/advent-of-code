import multiprocessing

def parse_input(input):
    data = input.split('\n\n')
    packets = []
    for pair in data:
        left = pair.split()[0]
        right = pair.split()[1]
        packets.append((eval(left), eval(right)))
    return packets

def compare_lists(left, right):
    #check if left and right are not empty
    if left and right:
        # there are items in both lists, compare the items
        for index in range(min(len(left),len(right))):
            if isinstance(left[index], list):
                if isinstance(right[index], list):
                    result = compare_lists(left[index], right[index])
                else:
                    result = compare_lists(left[index], list(right[index]))
                
                # check result is valid
                if result != 0:
                        return result
            else:
                if isinstance(right[index], list):
                    result = compare_lists(list(left[index]), right[index])
                else:
                    lval = int(left[index])
                    rval = int(right[index])
                    if lval == rval:
                        result = 0
                    else:
                        result = 1 if lval < rval else -1
                
                # check result is valid
                if result != 0:
                        return result
        return 0
    else:
        # this covers the empty lists case
        return 0

def s1(data):
    packets = parse_input(data)
    result = []
    for index, pair in enumerate(packets, start=1):
        print(f"== Pair {index} ==")
        result.append(compare_lists(*pair))

    print(result)
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


    

