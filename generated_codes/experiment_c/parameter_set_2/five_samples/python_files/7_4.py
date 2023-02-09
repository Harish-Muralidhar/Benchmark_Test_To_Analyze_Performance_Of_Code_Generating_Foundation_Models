'''

In the third example,
You will need to paint 2 balloons to make all of them appear to be the same color.

'''

T = int(input())
for i in range(T):
    s = input()
    a = s.count('a')
    b = s.count('b')
    print(min(a,b))