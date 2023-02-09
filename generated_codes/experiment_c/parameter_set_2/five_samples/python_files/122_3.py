'''

'''

import math

def pi(n):
    return math.pi

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def pi_approx(n):
    return truncate(pi(n), n)

if __name__ == "__main__":
    print(pi_approx(0))
    print(pi_approx(6))
    print(pi_approx(20))