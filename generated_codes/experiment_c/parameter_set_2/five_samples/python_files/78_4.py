'''

'''

import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True

def count_primes(x1,x2,y):
    count = 0
    for x in range(x1,x2+1):
        if is_prime(x*x + y*y):
            count += 1
    return count

t = int(input())
for i in range(t):
    y,x1,x2 = map(int,input().split())
    print(count_primes(x1,x2,y))