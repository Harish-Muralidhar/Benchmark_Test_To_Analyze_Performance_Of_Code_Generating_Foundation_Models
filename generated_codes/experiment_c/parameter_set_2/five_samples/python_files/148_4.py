'''


'''

import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def gcd_list(a):
    gcd_value = a[0]
    for i in range(1, len(a)):
        gcd_value = gcd(gcd_value, a[i])
    return gcd_value

def lcm_list(a):
    lcm_value = a[0]
    for i in range(1, len(a)):
        lcm_value = lcm(lcm_value, a[i])
    return lcm_value

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if gcd_list(a) == 1:
            print(lcm_list(a) - sum(a))
        else:
            print(-1)

if __name__ == '__main__':
    main()