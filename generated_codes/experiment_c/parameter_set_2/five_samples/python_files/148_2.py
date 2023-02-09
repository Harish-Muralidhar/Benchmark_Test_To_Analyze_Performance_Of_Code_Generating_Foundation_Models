"""


"""

import math

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def gcd_array(arr):
    n = len(arr)
    result = arr[0]
    for i in range(1, n):
        result = gcd(arr[i], result)
    return result

def min_balls(arr):
    n = len(arr)
    arr.sort()
    gcd_arr = gcd_array(arr)
    if gcd_arr == 1:
        return -1
    else:
        return arr[n-1] - gcd_arr + 1

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(i) for i in input().split()][0:n]
        print(min_balls(arr))