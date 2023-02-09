"""

"""

import math

def fibo(n):
    return ((1+math.sqrt(5))**n-(1-math.sqrt(5))**n)/(2**n*math.sqrt(5))

def is_fibo(n):
    return n == int(fibo(math.log((1+math.sqrt(5))*n, 1+math.sqrt(5))))


t = int(input())

for i in range(t):
    k = int(input())
    arr = list(map(int, input().strip().split()))
    flag = True
    for i in range(k-1):
        if arr[i+1] != 0:
            if is_fibo(arr[i]+1):
                flag = True
            else:
                flag = False
                break
    if flag:
        print("Yes")
    else:
        print("No")