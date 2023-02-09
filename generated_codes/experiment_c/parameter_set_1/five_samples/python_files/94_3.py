'''

'''

def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, number):
        if number % i == 0:
            return False
    return True

def primes(a, b):
    ret = []
    for i in range(2, a + b + 1):
        if is_prime(i):
            ret += [i]
    return ret

def sol(a, b):
    p = primes(a, b)
    n = a + b
    res = 0
    for i in range(1, len(p)):
        if p[i] > n:
            break
        res += ((a + 1) ** p[i-1]) * ((b + 1) ** (p[i] - p[i-1]))
    return res

def main():
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        print(sol(a, b) % 531169)

if __name__ == "__main__":
    main()