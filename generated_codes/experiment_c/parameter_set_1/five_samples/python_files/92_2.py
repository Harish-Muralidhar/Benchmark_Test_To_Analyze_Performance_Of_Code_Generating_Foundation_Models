'''

'''


T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    if sum(A) % K != 0 or sum(A[:M]) % K != 0 or sum(A[:M]) < sum(A) // K:
        print(-1)
    else:
        print(sum(A[:M]))