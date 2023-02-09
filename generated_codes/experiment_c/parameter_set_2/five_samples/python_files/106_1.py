"""


"""

import sys

def query1(a, x, y, v):
    for i in range(x, y+1):
        a[i] += v
        a[i] %= 1000000007
    return a

def query2(a, x, y, v):
    for i in range(x, y+1):
        a[i] *= v
        a[i] %= 1000000007
    return a

def query3(a, x, y, v):
    for i in range(x, y+1):
        a[i] = v
    return a

def query4(a, x, y):
    sum = 0
    for i in range(x, y+1):
        sum += a[i]
        sum %= 1000000007
    return sum

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a = query1(a, query[1], query[2], query[3])
        elif query[0] == 2:
            a = query2(a, query[1], query[2], query[3])
        elif query[0] == 3:
            a = query3(a, query[1], query[2], query[3])
        elif query[0] == 4:
            print(query4(a, query[1], query[2]))

if __name__ == "__main__":
    main()