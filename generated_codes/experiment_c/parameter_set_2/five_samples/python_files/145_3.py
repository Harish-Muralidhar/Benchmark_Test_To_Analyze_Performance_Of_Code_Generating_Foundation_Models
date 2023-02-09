'''

Explanation
Example case 1. There are no CPCs in the map.

Example case 2. There are 3 CPCs in the map.

CPC 1:

L = 0
R = 2
T = 0
B = 1

Possible primes are 2 and 3.

CPC 2:

L = 3
R = 1
T = 0
B = 0

Possible primes are 2 and 3.

CPC 3:

L = 0
R = 1
T = 0
B = 1

Possible primes are 2 and 3.

So, the map can accommodate 3 monsters.

'''

# Write your code here

# Importing the libraries
import numpy as np
import math
import time

# Function to check if a number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while(i * i <= n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

# Function to find the number of monsters in the map
def find_monsters(map):
    monsters = 0
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] == '^':
                L = R = T = B = 0
                L = find_contiguous(map, i, j, 'L')
                R = find_contiguous(map, i, j, 'R')
                T = find_contiguous(map, i, j, 'T')
                B = find_contiguous(map, i, j, 'B')
                if min(L, R, T, B) != 0:
                    for k in range(2, min(L, R, T, B) + 1):
                        if is_prime(k):
                            monsters += 1
    return monsters

#