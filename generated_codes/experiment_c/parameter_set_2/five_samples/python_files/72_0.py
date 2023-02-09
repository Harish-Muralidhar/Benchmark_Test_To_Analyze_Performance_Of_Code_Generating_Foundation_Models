"""


"""

#code

for _ in range(int(input())):
    l,r,n = map(int,input().split())
    c = 0
    for i in range(l,r+1):
        if i%2 == 0:
            c += 1
            if c == n:
                print(i,end=" ")
                break
    if c != n:
        print(-1,end=" ")
    print()