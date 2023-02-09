"""

Explanation

In the first example, there are 3 sub-rectangles which contains even number of currants.

In the second example, there are 26 sub-rectangles which contains even number of currants.

Solution:

"""

import numpy as np

def sub_rect(matrix):
    row = len(matrix)
    col = len(matrix[0])
    total_sub_rect = 0
    for i in range(row):
        for j in range(col):
            if i == 0 and j == 0:
                total_sub_rect += 1
            elif i == 0:
                total_sub_rect += j + 1
            elif j == 0:
                total_sub_rect += i + 1
            else:
                total_sub_rect += (i+1)*(j+1)
    return total_sub_rect

def even_sub_rect(matrix):
    row = len(matrix)
    col = len(matrix[0])
    even_sub_rect = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                even_sub_rect += sub_rect(matrix[0:i+1,0:j+1])
            else:
                even_sub_rect += sub_rect(matrix[0:i+1,0:j+1]) - 1
    return even_sub_rect

if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = np.zeros((n,m), dtype=int)
    for i in range(n):
        matrix[i] = list(map(int, input()))
    print(even_sub_rect(matrix))