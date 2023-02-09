'''
'''

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def find_common_ratio(arr):
    if len(arr) == 2:
        return arr[1] / arr[0]
    else:
        return find_common_ratio(arr[1:]) / arr[0]

def find_common_difference(arr):
    if len(arr) == 2:
        return arr[1] - arr[0]
    else:
        return find_common_difference(arr[1:]) - arr[0]

def find_arithmetic_progression(arr):
    common_difference = find_common_difference(arr)
    if common_difference == 0:
        return arr
    else:
        arr_new = []
        for i in range(len(arr)):
            if i == 0:
                arr_new.append(arr[i])
            else:
                arr_new.append(arr[i] + common_difference)
        return find_arithmetic_progression(arr_new)

def find_geometric_progression(arr):
    common_ratio = find_common_ratio(arr)
    if common_ratio == 0:
        return arr
    else:
        arr_new = []
        for i in range(len(arr)):
            if i == 0:
                arr_new.append(arr[i])
            else:
                arr_new.append(arr[i] * common_ratio)
        return find_geometric_progression(arr_new)

def find_arithmetic_progression_subset(arr):
    arr_new = []
    for i in range(len(arr)):