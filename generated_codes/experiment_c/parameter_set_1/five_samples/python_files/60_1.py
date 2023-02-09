'''

Example case 3.

Matrix which is determined by vector y is 

0 1
0 0
 
Then A → X = ¬ O and X → A is

1 0
0 0
 
'''

def solve(A):
    N = len(A)
    Y = [-1]*N
    for i in range(N):
        for j in range(N):
            if Y[i] == -1 and A[i][j] == 0:
                Y[i] = 0
                Y[j] = 1
            elif Y[i] == -1 and A[i][j] == 1 and Y[j] == 0:
                Y[i] = 1
                Y[j] = 0
            elif Y[i] == -1 and A[i][j] == 1 and Y[j] == -1:
                Y[i] = 0
                Y[j] = 1
            elif Y[i] == -1 and A[i][j] == 1 and Y[j] == 1:
                Y[i] = 1
                Y[j] = 0
    for i in range(N):
        for j in range(N):
            if Y[i] == -1:
                Y[i] = 1
            if Y[j] == -1:
                Y[j] = 1
            if A[i][j] == 1 and Y[i] == Y[j]:
                return -1
    return Y
            
def main():
    t = int(input())
    while t > 0:
        n = int(input())
        A = []
        for i in range(n):
            A.append(list(map(int,input().split())))
        Y = solve(A)
        if Y == -1:
            print("-1")
        else:
            print(" ".join(str(x) for x in Y))
        t -= 1

main()