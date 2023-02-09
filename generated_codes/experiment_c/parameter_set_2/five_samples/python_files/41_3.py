'''


'''

#Code

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'withdraw' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER amount
#  2. FLOAT balance
#

def withdraw(amount, balance):
    # Write your code here
    if amount%5==0 and amount<=balance:
        balance=balance-amount-0.5
    return balance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    amount = int(input().strip())

    balance = float(input().strip())

    result = withdraw(amount, balance)

    fptr.write(str(result))
    fptr.close()