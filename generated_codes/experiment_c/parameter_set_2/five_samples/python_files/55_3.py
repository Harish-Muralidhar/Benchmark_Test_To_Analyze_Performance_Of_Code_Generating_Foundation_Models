'''

Solution:

'''

import math

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a, a)

def find_gcd(arr, n):
    result = 0
    for i in range(n):
        result = gcd(arr[i], result)
    return result

def find_gcd_product(arr, n):
    result = 1
    for i in range(n):
        result = (result * find_gcd(arr, i+1)) % 1000000007
    return result

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_gcd_product(arr, n))