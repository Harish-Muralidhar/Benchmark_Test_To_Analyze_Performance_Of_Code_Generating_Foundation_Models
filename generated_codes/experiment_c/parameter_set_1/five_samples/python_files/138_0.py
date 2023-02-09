'''


'''

t = int(input())

while t:
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    
    for i in range(1,n-1):
        if arr[i+1]!=arr[i]:
            count += 1
    
    if arr[1]!=arr[0]:
        count += 1
    if arr[n-1]!=arr[n-2]:
        count += 1
    print(count)
    t -=1