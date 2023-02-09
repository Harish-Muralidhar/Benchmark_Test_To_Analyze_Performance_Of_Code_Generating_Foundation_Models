"""


Explanation :

The answer is (A_1 + A_2 + ... + A_N) / (B_1 + B_2 + ... + B_N)
where A_i and B_i are the numerator and denominator of the ith fraction.


"""

"""
def gcd(a,b):
    return a if b == 0 else gcd(b,a%b)

def lcm(a,b):
    return a*b//gcd(a,b)

def solve(a,b):
    sum_a = sum(a)
    sum_b = sum(b)
    g = gcd(sum_a,sum_b)
    return [sum_a//g,sum_b//g]

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = []
        b = []
        for _ in range(n):
            x,y = map(int,input().split('/'))
            a.append(x)
            b.append(y)
        r = solve(a,b)
        print('{}/{}'.format(r[0],r[1]))

if __name__ == '__main__':
    main()
"""


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


def solve(a, b):
    sum_a = sum(a)
    sum_b = sum(b)
    g = gcd(sum_a, sum_b)
    return [sum_a // g, sum_b // g]


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = []
        b = []
        for _ in range(n):
            x, y = map(int, input().split('/'))
            a.append(x)
            b.append(y)
        r = solve(a, b)
        print('{}/{}'.format(r[0], r[1]))


if __name__ == '__main__':
    main()