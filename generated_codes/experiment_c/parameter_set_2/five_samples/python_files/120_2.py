'''

'''

def prob(n,m):
    P = [[0 for i in range(m+1)] for j in range(n+1)]
    P[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1:
                continue
            P[i][j] = P[i-1][j]/2 + P[i][j-1]/2
    return sum([sum(i) for i in P])

t = int(input())
for i in range(t):
    n,m = [int(i) for i in input().split()]
    print(prob(n,m))