'''

Solution:

'''




N = int(input())
arr = list(map(int, input().split()))
Q = int(input())

def brute_force(arr,k):
    result = 0
    visited = [0]*len(arr)
    
    while(0 in visited):
        idx = -1
        max_gold = -1
        for i in range(len(arr)):
            if(visited[i]==0 and arr[i]>max_gold):
                idx = i
                max_gold = arr[i]
                
        visited[idx] = 1
        result += arr[idx]
        
        for i in range(1,k+1):
            if(idx+i<len(arr) and visited[idx+i]==0):
                visited[idx+i] = 1
                
            if(idx-i>=0 and visited[idx-i]==0):
                visited[idx-i] = 1
                
    return result

for i in range(Q):
    k = int(input())
    print(brute_force(arr,k))