'''


'''

import sys

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M, K = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        A.sort()
        if A[0] > K:
            print(-1)
            continue
        if A[0] == K:
            print(K*M)
            continue
        if A[0] < K:
            if K % A[0] == 0:
                if M * A[0] >= K:
                    print(K)
                else:
                    print(-1)
            else:
                if M * A[0] >= K - K % A[0]:
                    print(K - K % A[0])
                else:
                    print(-1)

if __name__ == '__main__':
    main()