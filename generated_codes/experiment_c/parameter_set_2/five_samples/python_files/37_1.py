"""


"""

for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if a>b:
        a=a-b
        if a>c:
            print(a-c)
        else:
            print(0)
    else:
        b=b-a
        if b>c:
            print(b-c)
        else:
            print(0)