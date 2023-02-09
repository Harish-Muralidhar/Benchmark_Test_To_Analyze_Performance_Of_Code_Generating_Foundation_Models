"""


Box: 12345 12345 12345 12345 12345
Ball: 12543 13245 13542 15423 15243

Box: 12345 12345 12345 12345 12345
Ball: 12543 13245 13542 15423 15342

Box: 12345 12345 12345 12345 12345
Ball: 12543 13245 13542 15243 15423

Box: 12345 12345 12345 12345 12345
Ball: 12543 13245 13542 15243 15342

since the number of divisors of 2 is equal to the number of divisors of 5, the number of divisors of 3 is equal to the number of divisors of 3, the number of divisors of 4 is equal to the number of divisors of 4, the number of divisors of 5 is equal to the number of divisors of 5, and the number of divisors of 1 is equal to the number of divisors of 1.


In the third case, the number of divisors of 2 is equal to the number of divisors of 4, the number of divisors of 3 is equal to the number of divisors of 9, the number of divisors of 4 is equal to the number of divisors of 16, the number of divisors of 5 is equal to the number of divisors of 25, ..., and the number of divisors of 100 is equal to the number of divisors of 100.

"""

import math

def divisors(n):
    divs = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            divs.append(i)
            if i!=n/i:
                divs.append(n/i)
    return divs

def divisors_count(n):
    return len(divisors(n))

def divisors_count_list(n):
    return [divisors_count(i) for i in range(1,n+1)]

def divisors_count_list_mod(n,mod):
    return [divisors_count(i)%mod for i