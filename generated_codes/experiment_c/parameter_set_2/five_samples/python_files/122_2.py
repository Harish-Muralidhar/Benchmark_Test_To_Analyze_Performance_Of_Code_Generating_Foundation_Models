'''

'''

import math
import decimal

def pi_approx(k):
    decimal.getcontext().prec = k+1
    return str(decimal.Decimal(103993)/decimal.Decimal(33102))

for _ in range(int(input())):
    print(pi_approx(int(input())))