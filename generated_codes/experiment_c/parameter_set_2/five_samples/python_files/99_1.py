'''

'''

def lcs(X, Y, m, n): 
    L = [[0 for x in range(n+1)] for x in range(m+1)] 
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
    return L[m][n] 

t=int(input())
while t>0:
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(lcs(a,b,n,n))
    t-=1