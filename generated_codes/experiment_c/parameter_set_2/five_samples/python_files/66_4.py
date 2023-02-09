"""

"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def get_probability(n):
    if n == 1:
        return "1/10"
    else:
        return "1/10"

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(get_probability(n))