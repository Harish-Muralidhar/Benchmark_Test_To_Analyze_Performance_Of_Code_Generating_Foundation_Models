'''


'''

import math

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def max_occurance(a,x,y):
    s = []
    for i in range(x-1,y):
        if gcd(a,i) > 1:
            s.append(i)
    if len(s) == 0:
        return -1,-1
    else:
        max_num = max(s)
        count = s.count(max_num)
        return max_num,count

if __name__ == "__main__":
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(m):
        g,x,y = map(int,input().split())
        print(max_occurance(g,x,y))