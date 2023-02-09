'''

'''

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        k = int(input())
        print(calc(a, n, k))

def calc(a, n, k):
    a.sort()
    cost = 0
    for i in range(n):
        if i <= k:
            cost += a[i]
        else:
            cost += a[i]*2
    return cost

if __name__ == '__main__':
    main()