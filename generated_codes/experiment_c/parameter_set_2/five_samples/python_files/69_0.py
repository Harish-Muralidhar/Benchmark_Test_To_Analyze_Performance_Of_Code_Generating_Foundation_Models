'''


'''

import math

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def max_gcd(arr,g,x,y):
    max_val = -1
    count = 0
    for i in range(x-1,y):
        if gcd(g,arr[i]) > 1:
            if arr[i] > max_val:
                max_val = arr[i]
                count = 1
            elif arr[i] == max_val:
                count += 1
    return max_val,count

def main():
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    for i in range(m):
        g,x,y = map(int,input().split())
        max_val,count = max_gcd(arr,g,x,y)
        print(max_val,count)

if __name__ == '__main__':
    main()