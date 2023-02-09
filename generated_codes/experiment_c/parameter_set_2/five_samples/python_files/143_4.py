"""



"""

import sys

def get_next_char(curr_char, k):
    if curr_char == '?':
        return '0'
    elif curr_char == str(k-1):
        return '0'
    else:
        return str(int(curr_char) + 1)

def get_next_str(curr_str, k):
    next_str = ''
    for i in range(len(curr_str)):
        next_str += get_next_char(curr_str[i], k)
    return next_str

def get_next_str_with_same_first_char(curr_str, k):
    next_str = ''
    for i in range(len(curr_str)):
        if i == 0:
            next_str += curr_str[0]
        else:
            next_str += get_next_char(curr_str[i], k)
    return next_str

def get_next_str_with_same_last_char(curr_str, k):
    next_str = ''
    for i in range(len(curr_str)):
        if i == len(curr_str) - 1:
            next_str += curr_str[-1]
        else:
            next_str += get_next_char(curr_str[i], k)
    return next_str

def get_next_str_with_same_first_and_last_char(curr_str, k):
    next_str = ''
    for i in range(len(curr_str)):
        if i == 0 or i == len(curr_str) - 1:
            next_str += curr_str[i]
        else:
            next_str += get_next_char(curr_str[i], k)
    return next_str

def get_next_str_with_same_first_and_last_char_and_last_second_char(curr_str, k):
   