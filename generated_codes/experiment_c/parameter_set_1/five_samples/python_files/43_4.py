"""
"""

import sys

def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        A = list(map(int, input().split(' ')))
        B = list(map(int, input().split(' ')))
        c = 0
        for i in range(N):
            # print('i:', i)
            # print('c:', c)
            if i == 0:
                if B[i] <= A[i]:
                    c += 1
            else:
                if A[i-1] + B[i] <= A[i]:
                    c += 1
            # print('c:', c)
        print(c)

if __name__ == '__main__':
    main()