'''



'''

#CODE
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    curr = 0
    count = 0
    for i in range(n):
        if arr[i]>curr:
            count = count + (arr[i] - curr)
        curr = arr[i]
    print(count)