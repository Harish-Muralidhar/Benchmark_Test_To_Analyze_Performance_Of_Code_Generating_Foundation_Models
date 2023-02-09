'''
Hence, the answer is BWBW.


'''

import itertools

def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))

def max_hamming_distance(s1, s2, n):
    max_hamming_distance = 0
    for i in itertools.product('WB', repeat=n):
        hamming_distance_i = hamming_distance(s1, i) + hamming_distance(s2, i)
        if hamming_distance_i > max_hamming_distance:
            max_hamming_distance = hamming_distance_i
            max_hamming_distance_string = ''.join(i)
    return max_hamming_distance_string

t = int(input())
for i in range(t):
    s1 = input()
    s2 = input()
    n = len(s1)
    print(max_hamming_distance(s1, s2, n))