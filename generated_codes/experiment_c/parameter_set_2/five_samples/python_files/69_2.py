'''


'''

import math

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def find_max(arr,g,x,y):
    S = []
    for i in range(x-1,y):
        if gcd(g,arr[i])>1:
            S.append(arr[i])
    if len(S)==0:
        print("-1 -1")
    else:
        max_num = max(S)
        print(max_num,S.count(max_num))

def main():
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    for i in range(M):
        g,x,y = map(int,input().split())
        find_max(arr,g,x,y)

main()