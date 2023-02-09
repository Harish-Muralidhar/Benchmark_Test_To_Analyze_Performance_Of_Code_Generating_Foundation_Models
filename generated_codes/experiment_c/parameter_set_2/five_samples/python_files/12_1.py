'''


Solution:

def min_paint(n,s):
    r=0
    g=0
    b=0
    for i in range(n):
        if s[i]=='R':
            r+=1
        elif s[i]=='G':
            g+=1
        else:
            b+=1
    return n-max(r,g,b)

t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    print(min_paint(n,s))

'''