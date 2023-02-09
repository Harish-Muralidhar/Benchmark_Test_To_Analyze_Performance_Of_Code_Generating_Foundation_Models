"""

"""

# cook your dish here

import math

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return (a*b) // gcd(a, b)

def is_power_of_ten(n):
    return n > 0 and (n == 1 or (n % 10 == 0 and is_power_of_ten(n // 10)))

def power_of_ten(n):
    if n == 0:
        return 1
    return 10 * power_of_ten(n - 1)

def find_power_of_ten(n):
    if n == 1:
        return 0
    return 1 + find_power_of_ten(n // 10)

def find_p_q(n):
    if n == 1:
        return (1, 10)
    if n % 10 == 0:
        return (1, 10)
    if is_power_of_ten(n):
        return (1, 10)
    if n % 10 == 1:
        return (1, 10)
    p = 1
    q = 10
    n_power = find_power_of_ten(n)
    n_power_ten = power_of_ten(n_power)
    if n % n_power_ten == 1:
        p = 1
        q = n_power_ten
    else:
        p = 1
        q = n_power_ten * 10
    return (p, q)

def main():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        p, q = find_p_q(n)
        g = gcd(p, q)
        p = p // g
        q = q // g
        print(p, q)

if __name__ == '__main__':
    main()