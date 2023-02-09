'''

'''

import math

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def prod(arr):
    prod = 1
    for i in range(len(arr)):
        prod *= arr[i]
    return prod

def find_gcd(arr, n):
    gcd_arr = []
    for i in range(1, 2**n):
        temp = []
        for j in range(n):
            if (i & (1 << j)) != 0:
                temp.append(arr[j])
        gcd_arr.append(gcd(prod(temp), 1000000007))
    return prod(gcd_arr)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(find_gcd(arr, n))

if __name__ == "__main__":
    main()