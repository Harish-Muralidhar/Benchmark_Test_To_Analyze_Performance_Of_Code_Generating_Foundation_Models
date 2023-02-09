"""
 = 101, nnn = 3, nnn = 1.

Constraints

1 ≤ t ≤ 20
1 ≤ k ≤ 100000
1 ≤ li ≤ 10^9

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the function below.

def howManyLies(k, hints):
    # Return the number of lies Johnny told.
    # hints is a list of strings, each string is either "< li Yes" or "> li No"
    # where li is an integer.
    # k is the number of hints.
    # Return the minimal number of lies Johnny told.
    # If Johnny didn't lie at all, return 0.
    # If Johnny always lied, return k.

    # Write your code here.
    # print(hints)
    # print(k)
    # print(type(hints))
    # print(type(k))
    # print(hints[0])
    # print(hints[0][0])
    # print(hints[0][2])
    # print(hints[0][4])
    # print(hints[0][0:2])
    # print(hints[0][2:4])
    # print(hints[0][4:])
    # print(hints[0][0:2] + hints[0][4:])
    # print(hints[0][0:2] + hints[0][4:])
    # print(hints[0][0:2] + hints[0][4:])
    # print(hints[0][0:2] + hints[0][4:])
    # print(hints[0][0:2] + hints[0][4:])
    # print(hints[0][0:2] + hints[0][4:])
    # print(hints[0][0:2] + hints[0][4:])
    # print(hints[0][0:2] + hints[0][4:])
    # print(hints[0][0:2] + hints[