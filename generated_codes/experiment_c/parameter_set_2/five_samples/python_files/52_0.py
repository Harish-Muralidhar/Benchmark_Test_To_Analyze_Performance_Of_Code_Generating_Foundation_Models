'''

'''

import sys

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return (a*b)//gcd(a,b)

def add_fractions(a,b,c,d):
    num = a*d + b*c
    den = b*d
    g = gcd(num,den)
    return num//g,den//g

def max_fraction(a,b):
    n = len(a)
    num = [0]*n
    den = [0]*n
    num[0] = a[0]
    den[0] = b[0]
    for i in range(1,n):
        num[i],den[i] = add_fractions(num[i-1],den[i-1],a[i],b[i])
    return num,den

def print_fraction(a,b):
    g = gcd(a,b)
    print(a//g,b//g)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = []
        b = []
        for i in range(n):
            x,y = map(int,input().split('/'))
            a.append(x)
            b.append(y)
        num,den = max_fraction(a,b)
        for i in range(n):
            print_fraction(num[i],den[i])
        print()

if __name__ == '__main__':
    main()