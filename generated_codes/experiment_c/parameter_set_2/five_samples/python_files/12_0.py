"""


"""

for _ in range(int(input())):
    n=int(input())
    s=input()
    r=s.count('R')
    g=s.count('G')
    b=s.count('B')
    if r==g==b:
        print(0)
    elif r==g or g==b or r==b:
        print(n-max(r,g,b))
    else:
        print(n-min(r,g,b))