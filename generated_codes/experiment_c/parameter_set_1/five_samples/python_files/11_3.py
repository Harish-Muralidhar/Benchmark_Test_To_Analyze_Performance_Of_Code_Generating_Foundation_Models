"""
"""

t = int(input())
for i in range(t):
    p = int(input())
    cou=0
    while(p):
        if p%2==0:
            p=p//2
            cou=cou+1
        else:
            p=p-1
            cou=cou+1
    print(cou)