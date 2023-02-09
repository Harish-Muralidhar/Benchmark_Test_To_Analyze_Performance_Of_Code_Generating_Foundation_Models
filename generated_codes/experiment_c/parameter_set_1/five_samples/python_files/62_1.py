'''
2
1

'''

n,q = map(int,input().split())
A = list(map(int,input().split()))

for i in range(q):
    res = list(map(int,input().split()))
    if res[0] == 0:
        min = A[res[1]]
        for j in range(res[1],res[2]+1):
            if A[j] < min:
                min = A[j]
        print(min)
    
    if res[0] == 1:
        for j in range(res[1],res[2]+1):
            A[j] = A[j] & res[3]