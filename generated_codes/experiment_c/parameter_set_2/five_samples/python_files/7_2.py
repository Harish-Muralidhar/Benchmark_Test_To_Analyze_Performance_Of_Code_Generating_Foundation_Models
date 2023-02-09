"""

In the third example,
You will need to paint 2 balloons.

"""

for _ in range(int(input())):
    s = input()
    c1 = s.count('a')
    c2 = s.count('b')
    if c1 == c2:
        print(c1)
    else:
        print(min(c1,c2))