'''

'''


#code
import sys


def num_ways(N):
    if N == 0:
        return 1
    if N == 1:
        return 1
    return (num_ways(N-1) + num_ways(N-2))

t = int(input())
for i in range(t):
    L, R, N = map(int,input().split())
#     print(L, R, N)
    c = 0
    for j in range(L, R+1):
        x = num_ways(j)
        c += 1
        if c == N:
            break
    if c == N:
        print(j, end = " ")
        if j == 0:
            print(".")
        else:
            for i in range(j):
                if i % 2 == 0:
                    print(".", end = "")
                else:
                    print("#", end = "")
    else:
        print(-1)