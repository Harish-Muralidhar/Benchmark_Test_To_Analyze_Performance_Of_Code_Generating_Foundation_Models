'''


'''

for _ in range(int(input())):
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    if r>=g and r>=b:
        print(n-r)
    elif g>=r and g>=b:
        print(n-g)
    else:
        print(n-b)