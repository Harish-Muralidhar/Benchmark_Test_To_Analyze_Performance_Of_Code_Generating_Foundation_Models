'''

'''

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    print(arr[-1])