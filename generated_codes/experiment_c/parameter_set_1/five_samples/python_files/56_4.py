'''

'''

#code

def solve(N, K):
    arr = []
    for i in range(1, N+1):
        if (i-K) > 0:
            arr.append(i-K)
        else:
            arr.append(N + (i-K))
    return arr

T = int(input())
for t in range(T):
    N, K = list(map(int, input().split()))
    arr = solve(N, K)
    for e in arr:
        print(e, end = " ")
    print()