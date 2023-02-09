"""

"""

import fractions

def add_fraction(a, b):
    return (a[0] + b[0], a[1] + b[1])

def reduce_fraction(a):
    gcd = fractions.gcd(a[0], a[1])
    return (a[0] / gcd, a[1] / gcd)

def max_fraction(fractions):
    n = len(fractions)
    max_fraction = fractions[0]
    for i in range(1, n):
        max_fraction = add_fraction(max_fraction, fractions[i])
        max_fraction = reduce_fraction(max_fraction)
    return max_fraction

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        fractions = []
        for j in range(n):
            a, b = map(int, input().split('/'))
            fractions.append((a, b))
        for j in range(n):
            print(max_fraction(fractions[j:]))
        print()

main()