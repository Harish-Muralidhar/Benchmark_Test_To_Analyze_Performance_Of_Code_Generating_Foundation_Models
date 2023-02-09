"""
=1, nnn=2, and nnn=1.

"""

import sys

def get_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return f.readline().strip()

def get_ints():
    return map(int, get_input().split(' '))

def get_int():
    return int(get_input())

def get_str():
    return get_input()

def get_strs():
    return get_input().split(' ')

def get_ints_arr():
    return [map(int, get_strs()) for _ in range(get_int())]

def get_strs_arr():
    return [get_strs() for _ in range(get_int())]

def get_ints_arr_arr():
    return [get_ints_arr() for _ in range(get_int())]

def get_strs_arr_arr():
    return [get_strs_arr() for _ in range(get_int())]

def get_ints_arr_arr_arr():
    return [get_ints_arr_arr() for _ in range(get_int())]

def get_strs_arr_arr_arr():
    return [get_strs_arr_arr() for _ in range(get_int())]

def get_ints_arr_arr_arr_arr():
    return [get_ints_arr_arr_arr() for _ in range(get_int())]

def get_strs_arr_arr_arr_arr():
    return [get_strs_arr_arr_arr() for _ in range(get_int())]

def get_ints_arr_arr_arr_arr_arr():
    return [get_ints_arr_arr_arr_arr() for _ in range(get_int())]

def get_strs_arr_arr_arr_arr_arr():
    return [get_strs_arr_arr_arr_arr() for _ in range(get_int())]

