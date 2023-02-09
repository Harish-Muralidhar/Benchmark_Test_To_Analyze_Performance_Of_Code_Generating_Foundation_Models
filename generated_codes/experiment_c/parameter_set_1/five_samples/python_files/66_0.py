'''
In second test case, you can open any page from 1 to 5 but Chef can choose any digit from 0 to 9. Probability that the Secret Digit is 1 after you opened the page with number 1 is 1/10.

Challenge:
1 ≤ T ≤ 10^5
1 ≤ N ≤ 10^18

Consider the number of digits in N. There are 1e18 numbers between 1 and 1e18. But the number of digits in one of them is limited to 18.

Find the probability of winning if both Chef's choice and your choice has uniform distribution.

You have to answer T independent test cases.

'''
from random import randint

def gcd(a,b):
    if a == 0: return b
    if b == 0: return a
    if a > b: return gcd(b, a % b)
    return gcd(a, b % a)

def prob(n):
    ans = 9
    while n > 0:
        ans = ans * 10 + 9
        n -= 1
    return ans
    
for _ in range(int(input())):
    n = int(input())
    print(prob(n), 10**n)
    #print(prob(n) // gcd(prob(n), 10**n), 10**n // gcd(prob(n), 10**n))
    
'''
from random import randint

def gcd(a,b):
    if a == 0: return b
    if b == 0: return a
    if a > b: return gcd(b, a % b)
    return gcd(a, b % a)

def prob(n):
    ans = 9
    while n > 0:
        ans = ans * 10 + 9
        n -= 1
    return ans

def prob_win(n):
    ans = 0
    for _ in range(10000):
        num = randint(1, n)
        if str(num) in str(randint(0, 9)): ans += 1
    return ans

for _ in range(int(input())):
    n = int(input())
    print(prob_win(n), 10000)
    #print(prob(n) // gcd(prob(n), 10**n), 10**n // gcd(prob(n), 10**n))
'''