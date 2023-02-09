'''

'''

# Write your code here
t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    count = 0
    for i in range(n):
        if a[i]-b[i] >= 0:
            count += 1
    print(count)
    t -= 1