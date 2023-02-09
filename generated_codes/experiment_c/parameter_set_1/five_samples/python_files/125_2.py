'''

In the second example case, Chef will choose 2 or 3 in first turn. In the second turn Sasha can choose 4 or 1. There are 3 times Sasha will kiss fellow:
Sasha chooses: 4 & 2, 4 & 3, 1 & 2.
Hence answer is 3/4 = 0.75 = 1.500000.

In the last example case, Chef will choose 2 or 2 in first turn. In the second turn Sasha can choose 2 or 2. There are 2 times Sasha will kiss fellow:

Sasha chooses: 2 & 2.
Hence answer is 2/4 = 0.5 = 1.000000.
 

"""

import math
import numpy as np
import random

def binomial_dist(n,k,p):
    '''
    This function calculates the binomial probabilities of n trials(bernoulli) with k successes with probability p
    '''
    binomial_prob = 0
    q = 1-p
    binomial_prob = math.factorial(n) / (math.factorial(n-k)*(math.factorial(k))) * (p**k) * (q**(n-k))
    return binomial_prob

def prob_kiss(chef_gifts,sasha_gifts):
    '''
    This function takes two arrays of numbers and returns the probability of Sasha kissing chef
    '''
    kiss_prob = 0
    for i in range(len(chef_gifts)):
        for j in range(len(sasha_gifts)):
            kiss_prob += binomial_dist(1,1,(chef_gifts[i]**sasha_gifts[j])/(sasha_gifts[j]**chef_gifts[i]))
    kiss_prob = kiss_prob / (len(chef_gifts) * len(sasha_gifts))
    return kiss_prob

test_cases = int(input())
for i in range(test_cases):
    n = int(input())
    chef_gifts = list(map(int,input().split()))
    sasha_gifts = list(map(int,input().split()))

    print(prob_kiss(chef_gifts,sasha_gifts))