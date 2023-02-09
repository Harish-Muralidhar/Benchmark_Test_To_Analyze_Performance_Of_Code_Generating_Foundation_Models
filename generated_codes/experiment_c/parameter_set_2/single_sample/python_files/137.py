'''


'''

import random
import math

def bogoSort(n):
    arr = [i for i in range(1,n+1)]
    random.shuffle(arr)
    count = 0
    while arr != [i for i in range(1,n+1)]:
        count += 1
        i = 0
        while i < len(arr) and arr[i] == i+1:
            i += 1
        j = len(arr)-1
        while j >= 0 and arr[j] == j+1:
            j -= 1
        random.shuffle(arr[i:j+1])
    return count

def bogoSort2(n):
    arr = [i for i in range(1,n+1)]
    random.shuffle(arr)
    count = 0
    while arr != [i for i in range(1,n+1)]:
        count += 1
        i = 0
        while i < len(arr) and arr[i] == i+1:
            i += 1
        j = len(arr)-1
        while j >= 0 and arr[j] == j+1:
            j -= 1
        random.shuffle(arr[i:j+1])
    return count

def bogoSort3(n):
    arr = [i for i in range(1,n+1)]
    random.shuffle(arr)
    count = 0
    while arr != [i for i in range(1,n+1)]:
        count += 1
        i = 0
        while i < len(arr) and arr[i] == i+1:
            i += 1
        j = len(arr)-1
        while j >= 0 and arr[j] == j+1:
            j -= 1
        random.shuffle(arr[i:j+1])
    return count

def bogoSort4(n):
    arr = [i for i in range(1,n+1)]
    random.shuffle(arr)
    count = 0
    while arr != [i for i in range(1,n+1)]:
