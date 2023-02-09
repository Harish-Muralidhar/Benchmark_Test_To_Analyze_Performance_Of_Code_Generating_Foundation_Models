"""

"""

# Write your code here

import sys

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        N, K = map(int, sys.stdin.readline().split())
        if K == 0:
            print(" ".join([str(i+1) for i in range(N)]))
        elif N == K:
            print("-1")
        else:
            print(" ".join([str(i+1) for i in range(N-K-1)] + [str(i+1) for i in range(N-1, N-K-1, -1)]))

if __name__ == '__main__':
    main()