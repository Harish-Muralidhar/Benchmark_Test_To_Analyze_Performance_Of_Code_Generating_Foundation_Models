'''
'''

#code
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    k = 0
    for j in range(n-1,-1,-2):
        k += a[j]
    print(k)