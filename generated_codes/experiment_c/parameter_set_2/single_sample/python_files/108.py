'''


'''

# Write your code here
import math
def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def get_prime_factors(n):
    factors = []
    for i in range(2,int(math.sqrt(n))+1):
        while n%i == 0:
            factors.append(i)
            n = n//i
    if n > 1:
        factors.append(n)
    return factors

def get_card_count(n):
    if is_prime(n):
        return n
    else:
        factors = get_prime_factors(n)
        factors = list(set(factors))
        factors.sort()
        return len(factors)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(get_card_count(n))

if __name__ == "__main__":
    main()