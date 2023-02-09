'''


'''

def numWays(path):
    count = 0
    for i in range(1, len(path)):
        if path[i] == "#" and path[i-1] == ".":
            count += 1
    return(2**count)

def solve(path):
    count = 0
    for i in range(1, len(path)):
        if path[i] == "#" and path[i-1] == ".":
            count += 1
    return(2**count)
    
    
t = int(input())
for _ in range(t):
    L, R, N = map(int, input().split())
    ans = 0
    for i in range(L, R+1):
        path = bin(i)[2:]
        path = "0"*(len(bin(R))-len(bin(i))) + path
        if(solve(path) == N):
            ans = i
            break
    if(ans == 0):
        print(-1)
    else:
        print(ans, " ".join(path))