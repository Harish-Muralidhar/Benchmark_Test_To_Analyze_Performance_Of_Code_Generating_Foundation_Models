'''


'''

import math

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def findGCD(arr, n): 
    result = arr[0] 
    for i in range(1, n): 
        result = gcd(arr[i], result) 
      
    return result 

def find_min_ops(arr,n,k):
    gcd_arr = findGCD(arr,n)
    if(gcd_arr%k==0):
        return 0
    else:
        return 1

t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    print(find_min_ops(arr,n,k))