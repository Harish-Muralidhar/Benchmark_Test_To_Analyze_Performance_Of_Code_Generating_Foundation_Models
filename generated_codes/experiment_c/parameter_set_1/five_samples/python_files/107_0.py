'''

'''

n,m = map(int,input().strip().split())
a = list(input())
a = list(map(int,a))
for i in range(m):
    x = int(input())
    B1 = 0
    B2 = 0
    for j in range(x):
        if a[j]-a[x-1]>0:
            B1 += a[j]-a[x-1]
        elif a[j]-a[x-1]<0:
            B2 += a[j]-a[x-1]
    print(B1+B2)
'''
import sys

def input(): return sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())
    a = list(map(int, input()))
    for i in range(m):
        x = int(input())
        B1 = 0
        B2 = 0
        for j in range(x):
            if a[j] - a[x - 1] > 0:
                B1 += a[j] - a[x - 1]
            elif a[j] - a[x - 1] < 0:
                B2 += a[j] - a[x - 1]
        print(B1 + B2)

if __name__ == '__main__':
    main()

'''