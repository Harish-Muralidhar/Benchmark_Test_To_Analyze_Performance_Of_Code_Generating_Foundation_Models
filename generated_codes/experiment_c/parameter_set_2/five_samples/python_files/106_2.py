'''


'''

# Write your code here

def query_1(x,y,v,arr):
    for i in range(x,y+1):
        arr[i] += v
        arr[i] %= M
    return arr

def query_2(x,y,v,arr):
    for i in range(x,y+1):
        arr[i] *= v
        arr[i] %= M
    return arr

def query_3(x,y,v,arr):
    for i in range(x,y+1):
        arr[i] = v
    return arr

def query_4(x,y,arr):
    sum = 0
    for i in range(x,y+1):
        sum += arr[i]
        sum %= M
    return sum


N,Q = map(int,input().split())
A = list(map(int,input().split()))

M = 1000000007

for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        A = query_1(q[1],q[2],q[3],A)
    elif q[0] == 2:
        A = query_2(q[1],q[2],q[3],A)
    elif q[0] == 3:
        A = query_3(q[1],q[2],q[3],A)
    elif q[0] == 4:
        print(query_4(q[1],q[2],A))