'''

'''

import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    n = int(input())
    chocolates = []
    caramels = []
    for i in range(n):
        chocolate, caramel = map(int, input().split())
        chocolates.append(chocolate)
        caramels.append(caramel)
    desired_chocolate, desired_caramel = map(int, input().split())
    if desired_chocolate == desired_caramel == 0:
        print(0)
        return
    if desired_chocolate == 0:
        print(min(caramels))
        return
    if desired_caramel == 0:
        print(min(chocolates))
        return
    if desired_chocolate * max(caramels) < desired_caramel * min(chocolates):
        print(-1)
        return
    if desired_chocolate * min(caramels) > desired_caramel * max(chocolates):
        print(-1)
        return
    l = lcm(desired_chocolate, desired_caramel)
    min_count = math.inf
    for i in range(n):
        if chocolates[i] * desired_caramel % desired_chocolate == 0:
            count = l // caramels[i]
            min_count = min(min_count, count)
    if min_count == math.inf:
        print(-1)
    else:
        print(min_count)

if __name__ == '__main__':
    main()