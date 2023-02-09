"""

"""

def second_largest(a,b,c):
    if a > b and a > c:
        if b > c:
            return b
        else:
            return c
    elif b > a and b > c:
        if a > c:
            return a
        else:
            return c
    else:
        if a > b:
            return a
        else:
            return b

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a,b,c = map(int,input().split())
        print(second_largest(a,b,c))