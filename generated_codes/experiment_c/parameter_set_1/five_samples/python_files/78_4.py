"""
"""

import math

def is_supernatural(i,j):
    if i == 0 and j == 0:
        return True
    i_is_square = math.sqrt(i).is_integer()
    j_is_square = math.sqrt(j).is_integer()
    if i_is_square and j_is_square:
        return True
    if i_is_square and j%2 == 0:
        return True
    if j_is_square and i%2 == 0:
        return True
    if i%3 == 0 and j%3 == 0:
        return True
    return False

def get_num_guns(y,x1,x2):
    num_guns = 0
    for x in range(x1,x2+1):
        if not is_supernatural(x,y):
            num_guns += 1
    return num_guns

num_cases = int(input())
for i in range(num_cases):
    y,x1,x2 = [int(x) for x in input().split()]
    print(get_num_guns(y,x1,x2))