'''


'''

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcd_list(a):
    result = a[0]
    for i in range(1, len(a)):
        result = gcd(a[i], result)
    return result

def solve(a):
    a.sort()
    g = gcd_list(a)
    if g == 1:
        return -1
    else:
        return sum([(g - i) for i in a])

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))