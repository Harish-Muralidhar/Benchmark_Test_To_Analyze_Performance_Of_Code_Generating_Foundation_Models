"""


"""

import sys

def main():
    test_cases = int(sys.stdin.readline())
    for _ in range(test_cases):
        l, r, n = map(int, sys.stdin.readline().split())
        good_numbers = []
        for i in range(l, r+1):
            if is_good(i):
                good_numbers.append(i)
        if len(good_numbers) < n:
            print -1
        else:
            print good_numbers[n-1], get_path(good_numbers[n-1])

def is_good(num):
    path = get_path(num)
    return num == get_ways(path)

def get_path(num):
    path = ''
    while num > 0:
        if num % 2 == 0:
            path = '.' + path
        else:
            path = '#' + path
        num /= 2
    return path

def get_ways(path):
    ways = [0] * len(path)
    ways[0] = 1
    for i in range(1, len(path)):
        if path[i] == '.':
            ways[i] = ways[i-1] + ways[i-2]
        else:
            ways[i] = ways[i-1]
    return ways[-1]

if __name__ == '__main__':
    main()