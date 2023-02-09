"""

"""

#code

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

def maxSubsequence(arr, n): 
    max = 0
    for i in range(n): 
        for j in range(n): 
            if (i != j): 
                temp = lcs(arr[i], arr[j], len(arr[i]), len(arr[j])) 
                if (max < temp): 
                    max = temp 
    return max 

t = int(input())
while(t):
    n = int(input())
    arr = []
    for i in range(2):
        arr.append(list(map(int,input().split())))
    print(maxSubsequence(arr, n))
    t = t - 1