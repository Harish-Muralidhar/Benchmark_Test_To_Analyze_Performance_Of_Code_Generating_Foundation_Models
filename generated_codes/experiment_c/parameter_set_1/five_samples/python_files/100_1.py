'''


'''

import sys

def subsetsum(array,num):
    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum (array[1:],(num - array[0]))
            if with_v:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:],num)

def main():
    test_cases = int(sys.stdin.readline())
    for testcase in range(test_cases):
        n_m = sys.stdin.readline()
        n_m = n_m.split()
        n = int(n_m[0])
        m = int(n_m[1])
        arr = sys.stdin.readline()
        arr = arr.split()
        arr = [int(x) for x in arr]
        x = subsetsum(arr,m)
        if x:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__": 
    main()