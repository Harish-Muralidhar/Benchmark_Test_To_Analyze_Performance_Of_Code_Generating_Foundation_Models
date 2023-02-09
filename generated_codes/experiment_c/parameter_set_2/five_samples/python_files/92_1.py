'''


'''

import sys
import math

def main():
    T = int(input())
    for i in range(T):
        N,M,K = map(int,input().split())
        A = list(map(int,input().split()))
        A.sort()
        if N == M:
            if sum(A)%K == 0:
                print(sum(A))
            else:
                print(-1)
        else:
            if sum(A[:M])%K == 0:
                print(sum(A[:M]))
            else:
                print(-1)

if __name__ == '__main__':
    main()