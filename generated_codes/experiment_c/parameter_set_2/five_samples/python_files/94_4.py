'''

'''

t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    if a == b:
        print(2**(a-1))
    else:
        print(2**(min(a,b)-1))