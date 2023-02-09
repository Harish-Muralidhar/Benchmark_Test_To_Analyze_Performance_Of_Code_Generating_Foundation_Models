'''

'''

import sys

def get_input():
    return sys.stdin.readline()

def get_input_list():
    return sys.stdin.readline().split()

def get_input_int():
    return int(sys.stdin.readline())

def get_input_int_list():
    return list(map(int, sys.stdin.readline().split()))

def get_input_float():
    return float(sys.stdin.readline())

def get_input_float_list():
    return list(map(float, sys.stdin.readline().split()))

def get_input_str():
    return str(sys.stdin.readline())

def get_input_str_list():
    return str(sys.stdin.readline()).split()

def get_input_str_list_list():
    return [list(map(str, sys.stdin.readline().split()))]

def get_input_grid(n):
    grid = []
    for i in range(n):
        grid.append(list(map(int, sys.stdin.readline().split())))
    return grid

def get_input_grid_char(n):
    grid = []
    for i in range(n):
        grid.append(list(sys.stdin.readline().split()))
    return grid

def print_grid(grid):
    for i in range(len(grid)):
        print(' '.join(map(str, grid[i])))

def print_grid_char(grid):
    for i in range(len(grid)):
        print(''.join(grid[i]))

def main():
    t = get_input_int()
    for i in range(t):
        n = get_input_int()
        a = get_input_int_list()
        b = get_input_int_list()
        c = 0
        for j in range(n):
            if a[j] >= b[j]:
                c +=