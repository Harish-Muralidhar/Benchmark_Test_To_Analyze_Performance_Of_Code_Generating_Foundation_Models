'''

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

def find_product(arr, n):
    result = 1
    for i in range(n):
        result = (result * arr[i]) % 1000000007
    return result

def find_all_gcd(arr, n):
    result = []
    for i in range(1, 2**n):
        temp = []
        for j in range(n):
            if i & (1 << j):
                temp.append(arr[j])
        result.append(find_gcd(temp, len(temp)))
    return result

def find_answer(arr, n):
    result = find_all_gcd(arr, n)
    return find_product(result, len(result))

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_answer(arr, n))