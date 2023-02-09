"""


Explanation

Let's consider the example n = 2. If we don't fix any elements than the expected amount of shuffles will be equal to 1. Now let's fix one element. For example, let's fix 1. Now the expected amount of shuffles will be equal to the expected amount of shuffles for sorting (2). The answer is 2/1.
That's why the answer for n = 2 is 2/1.
"""
import numpy as np
import random
import math
from fractions import Fraction

def bogo_sort(seq):
    if len(seq)<=1:
        return 0
    else:
        #print(seq)
        for i in range(len(seq)):
            if seq[i]==i+1:
                seq[i]=0
        fixed_count=seq.count(0)
        if fixed_count==len(seq):
            return 0
        an=[]
        for i in range(len(seq)):
            if seq[i]!=0:
                an.append(seq[i])
        return (1+bogo_sort(an))

def shuffle(seq):
    seq=seq
    random.shuffle(seq)
    return seq

def poly(n):
    poly_sum=0
    for i in range(1,n+1):
        poly_sum+= (1/((n-i+1)**i))
    return poly_sum

def expected_value(n):
    sum=0
    for i in range(n):
        sum+=Fraction(poly(i),math.factorial(i))
    return sum

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        seq = list(range(1,n+1))
        rand_seq = shuffle(seq)
        bogosort_count = bogo_sort(rand_seq)
        print(expected_value(n))