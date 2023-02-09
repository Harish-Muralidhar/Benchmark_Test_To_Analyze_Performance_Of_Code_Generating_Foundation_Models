'''

Solution:
'''

# Write your code here

import math

def gcd(a, b):
    if a == 0:
        return b
    
    return gcd(b%a, a)

def greatest_gcd(arr):
    product = 1

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            product *= gcd(arr[i], arr[j])
            product %= 1000000007

    return product

T = int(input())

for _ in range(T):
    N = int(input())
    arr = [int(x) for x in input().split()]

    print(greatest_gcd(arr))