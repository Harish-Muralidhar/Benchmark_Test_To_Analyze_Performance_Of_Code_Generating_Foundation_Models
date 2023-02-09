'''


since the number of divisors of 2 is equal to the number of divisors of 5,
the number of divisors of 3 is equal to the number of divisors of 4,
the number of divisors of 1 is equal to the number of divisors of 3,
the number of divisors of 5 is equal to the number of divisors of 2,
the number of divisors of 4 is equal to the number of divisors of 5.

'''

import math

def divisor(n):
    divisor_list = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            divisor_list.append(i)
            if i != n // i:
                divisor_list.append(n//i)
    return divisor_list

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        count = 0
        for j in range(1, N+1):
            if len(divisor(j)) == len(divisor(j+1)):
                count += 1
        print(count%500009)

if __name__ == '__main__':
    main()