'''
'''

t = int(input())

for i in range(0,t):
    n = [int(x) for x in input().split()]
    x = int(n[0])
    y = int(n[1])
    a = [int(x) for x in input().split()]
    sum = 0
    for i in range(0,x):
        sum = sum + a[i]
    if sum < y:
        print(-1)
    else:
        print(sum//y)