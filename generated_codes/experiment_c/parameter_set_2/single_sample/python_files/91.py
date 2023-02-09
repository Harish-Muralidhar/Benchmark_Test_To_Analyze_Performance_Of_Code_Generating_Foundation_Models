"""

Explanation:

Press row-button 0.

0 1 0
1 1 0
1 1 0

Press column-button 2.

0 1 1
1 1 1
1 1 1

The final configuration is achieved.

"""

import numpy as np

def check_equal(arr1, arr2):
    return np.array_equal(arr1, arr2)

def flip_row(arr, row):
    arr[row] = 1-arr[row]
    return arr

def flip_col(arr, col):
    arr[:, col] = 1-arr[:, col]
    return arr

def find_row_col(arr, row, col):
    for i in range(row):
        if arr[i, col] == 1:
            return i
    return -1

def find_col_row(arr, row, col):
    for i in range(col):
        if arr[row, i] == 1:
            return i
    return -1

def find_row_col_2(arr, row, col):
    for i in range(row):
        if arr[i, col] == 0:
            return i
    return -1

def find_col_row_2(arr, row, col):
    for i in range(col):
        if arr[row, i] == 0:
            return i
    return -1

def find_row_col_3(arr, row, col):
    for i in range(row):
        if arr[i, col] == 1:
            return i
    return -1

def find_col_row_3(arr, row, col):
    for i in range(col):
        if arr[row, i] == 1:
            return i
    return -1

def find_row_col_4(arr, row, col):
    for i in range(row):
        if arr[i, col] == 0:
            return i
    return -1

def find_col_row_4(arr, row, col):
    for i in range