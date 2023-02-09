"""

"""

import sys
import math

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return (a*b)/gcd(a,b)

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        n = int(sys.stdin.readline())
        arr = []
        for j in range(n):
            arr.append(sys.stdin.readline().split('/'))
        for j in range(n):
            arr[j][0] = int(arr[j][0])
            arr[j][1] = int(arr[j][1])
        for j in range(n):
            num = arr[j][0]
            den = arr[j][1]
            for k in range(j+1,n):
                num = num + arr[k][0]
                den = lcm(den,arr[k][1])
            g = gcd(num,den)
            num = num/g
            den = den/g
            print num,'/',den
        if i != t-1:
            print

if __name__ == '__main__':
    main()