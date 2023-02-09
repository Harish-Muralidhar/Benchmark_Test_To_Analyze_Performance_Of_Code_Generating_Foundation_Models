"""

"""

N = int(input())
A = list(map(int, input().split()))

for i in range(0, N):
    for j in range(i+1, N):
        print(A[i] & A[j], end=" ")