'''


'''

import sys

def get_input():
    return sys.stdin.readline().strip()

def get_input_int():
    return int(get_input())

def get_input_ints():
    return [int(x) for x in get_input().split()]

def get_input_int_list():
    return [int(x) for x in get_input().split()]

def get_input_string():
    return [x for x in get_input().split()]

def get_input_char_list():
    return [x for x in get_input()]

def get_input_char():
    return get_input()[0]

def get_input_char_int():
    return ord(get_input())

def get_input_char_int_list():
    return [ord(x) for x in get_input()]

def get_ints_from_file(file_name):
    f = open(file_name, 'r')
    return [int(x) for x in f.read().split()]

def get_strings_from_file(file_name):
    f = open(file_name, 'r')
    return [x for x in f.read().split()]

def get_char_list_from_file(file_name):
    f = open(file_name, 'r')
    return [x for x in f.read()]

def get_char_from_file(file_name):
    f = open(file_name, 'r')
    return f.read()[0]

def get_char_int_from_file(file_name):
    f = open(file_name, 'r')
    return ord(f.read()[0])

def get_char_int_list_from_file(file_name):
    f = open(file_name, 'r')
    return [ord(x) for x in f.read()]

def get_input_int_from_file(file_name):
    f = open