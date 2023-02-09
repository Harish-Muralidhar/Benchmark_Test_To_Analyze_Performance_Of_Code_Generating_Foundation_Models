'''


since the number of divisors of 3 is equal to the number of divisors of 2, 
the number of divisors of 4 is equal to the number of divisors of 3, 
the number of divisors of 1 is equal to the number of divisors of 5 and
the number of divisors of 2 is equal to the number of divisors of 3. 

'''

'''

import sys
import time
import math

def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
    
def main():
    start_time = time.time()
    # I/O code
    f = open('input.txt', 'r')
    # f = sys.stdin
    
    T = int(f.readline())
    for _ in range(T):
        N = int(f.readline())
        length = len(factors(N))
        print length
    
    
    print time.time() - start_time
    
    
    
if __name__ == '__main__':
    main()
    
'''