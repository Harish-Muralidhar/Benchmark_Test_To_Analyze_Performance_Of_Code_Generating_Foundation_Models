'''

'''

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().strip()))
    for _ in range(m):
        x = int(sys.stdin.readline())
        b1 = 0
        b2 = 0
        for i in range(x):
            if a[i] - a[x-1] > 0:
                b1 += a[i] - a[x-1]
            else:
                b2 += a[i] - a[x-1]
        print(b1 - b2)

if __name__ == '__main__':
    main()