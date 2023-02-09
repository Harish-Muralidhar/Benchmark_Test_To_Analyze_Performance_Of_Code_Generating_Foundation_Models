'''

'''

import numpy as np

def max_alternating_subarray(arr):
    n = len(arr)
    if n == 1:
        return 1
    if n == 2:
        return 2
    max_len = 1
    for i in range(n):
        curr_len = 1
        for j in range(i+1, n):
            if arr[j]*arr[j-1] < 0:
                curr_len += 1
            else:
                break
        max_len = max(max_len, curr_len)
    return max_len

def max_alternating_subarray_fast(arr):
    n = len(arr)
    if n == 1:
        return 1
    if n == 2:
        return 2
    max_len = 1
    for i in range(n):
        curr_len = 1
        for j in range(i+1, n):
            if arr[j]*arr[j-1] < 0:
                curr_len += 1
            else:
                break
        max_len = max(max_len, curr_len)
    return max_len

def max_alternating_subarray_fast(arr):
    n = len(arr)
    if n == 1:
        return 1
    if n == 2:
        return 2
    max_len = 1
    for i in range(n):
        curr_len = 1
        for j in range(i+1, n):
            if arr[j]*arr[j-1] < 0:
                curr_len += 1
            else:
                break
        max_len = max(max_len, curr_len)
    return max_len

def max_alternating_subarray_fast(arr):
    n = len(arr)
    if n == 1:
        return 1
    if n == 2:
        return 2
    max_len = 1
    for i in range(n):
        curr_len = 1
        for j in range(i+1,