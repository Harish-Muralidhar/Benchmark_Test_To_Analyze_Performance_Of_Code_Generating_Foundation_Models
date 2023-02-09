"""

"""

def minimumAbsoluteDifference(arr, n, k):
    pairs = 0
    arr.sort()
    l = 0
    r = n - 1
    lst=[]
    while(l < r):
        if (abs(arr[l] + arr[r] - k) < abs(k - arr[l+1] - arr[r])):
            lst.append(abs(arr[l] + arr[r] - k))
            pairs+=1
            l += 1
            r -= 1
        else:
            l += 1
    return min(lst), pairs

t = int(input())
for i in range(t):
    n,k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    print(*minimumAbsoluteDifference(arr, n, k))