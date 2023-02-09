'''


'''

def count(arr, n): 
    count = 0
    for i in range(1 << n): 
        subset = [] 
        for j in range(n + 1): 
            if (i & (1 << j)): 
                subset.append(arr[j]) 
        if (len(subset) >= 2): 
            count += 1
    return count 

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(count(arr,n))