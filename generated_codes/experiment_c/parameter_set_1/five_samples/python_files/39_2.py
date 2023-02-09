'''

note:

we need to check for the prime numbers in the range of the number.

'''

import math
def isPrime(num):
    if num < 2:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

# def getMaxCoins(n, k):
#     maxCoins = n
#     while k >= 2:
#         if isPrime(k):
#             return maxCoins
#         maxCoins = n % k
#         k -= 1
#     return maxCoins

def getMaxCoins(n, k):
    if k == 1:
        return n
    maxCoins = 1
    for i in range(2, k+1):
        if n % i < maxCoins:
            return maxCoins
        else:
            maxCoins = n % i
    return maxCoins

for tc in range(int(input())):
    N, K = map(int, input().split())
    print(getMaxCoins(N, K))