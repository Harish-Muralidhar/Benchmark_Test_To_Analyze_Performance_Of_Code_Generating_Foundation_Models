"""


"""

import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def find_gcd(arr, n):
    result = arr[0]
    for i in range(1, n):
        result = gcd(arr[i], result)
    return result

def find_operations(arr, n, k):
    if k == 1:
        return 0
    g = find_gcd(arr, n)
    if g % k == 0:
        return 0
    return -1

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(find_operations(arr, n, k))