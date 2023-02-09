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
  
def max_len(arr, n): 
    max_len = 0
    for i in range(n): 
        for j in range(n): 
            if (i != j): 
                len = lcs(arr[i], arr[j], len(arr[i]), len(arr[j])) 
                if (len > max_len): 
                    max_len = len 
    return max_len 
  
t = int(input())
for i in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr = [arr1, arr2]
    print(max_len(arr, 2))