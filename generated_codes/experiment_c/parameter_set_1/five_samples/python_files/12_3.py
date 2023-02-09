"""

"""

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    r = s.count('R')
    b = s.count('B')
    g = s.count('G')
    if r == b == g:
        print(0)
    elif r > b and r > g:
        if b>g:
            print(r-g)
        else:
            print(r-b)
    elif b > r and b > g:
        if r>g:
            print(b-g)
        else:
            print(b-r)
    elif g > b and g > r:
        if b>r:
            print(g-r)
        else:
            print(g-b)
    else:
        print(r+b+g-max(r,b,g))