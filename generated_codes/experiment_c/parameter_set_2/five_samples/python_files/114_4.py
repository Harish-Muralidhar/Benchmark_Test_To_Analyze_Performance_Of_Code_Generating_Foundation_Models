'''

'''

def min_cost(arr,n,k):
    arr.sort()
    cost = 0
    for i in range(n):
        if i < k:
            cost += arr[i]
        else:
            cost += arr[i]*2
    return cost

n = int(input())
arr = list(map(int,input().split()))
q = int(input())
for i in range(q):
    k = int(input())
    print(min_cost(arr,n,k))