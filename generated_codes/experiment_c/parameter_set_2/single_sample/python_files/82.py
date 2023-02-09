"""


since the number of divisors of 1 is equal to the number of divisors of 1,
the number of divisors of 2 is equal to the number of divisors of 3,
the number of divisors of 3 is equal to the number of divisors of 2,
the number of divisors of 4 is equal to the number of divisors of 5,
and the number of divisors of 5 is equal to the number of divisors of 4.

"""

import math

def divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

def main():
    t = int(input())
    while t:
        n = int(input())
        count = 0
        for i in range(1,n+1):
            div_i = divisors(i)
            div_n = divisors(n)
            if len(div_i) == len(div_n):
                count += 1
        print(count)
        t -= 1

if __name__ == '__main__':
    main()