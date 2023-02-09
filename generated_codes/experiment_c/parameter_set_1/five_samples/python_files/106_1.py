'''


'''

N,Q = map(int,input().split())
A = list(map(int,input().split()))
M = 1000000007
for query in range(Q):
    Q = list(map(int,input().split()))
    if Q[0] == 1:
        for i in range(Q[1]-1,Q[2]):
            A[i] = (A[i] + Q[3]) % M
    elif Q[0] == 2:
        for i in range(Q[1]-1,Q[2]):
            A[i] = (A[i] * Q[3]) % M
    elif Q[0] == 3:
        for i in range(Q[1]-1,Q[2]):
            A[i] = Q[3]
    elif Q[0] == 4:
        sum = 0
        for i in range(Q[1]-1,Q[2]):
            sum = (sum + A[i]) % M
        print(sum)