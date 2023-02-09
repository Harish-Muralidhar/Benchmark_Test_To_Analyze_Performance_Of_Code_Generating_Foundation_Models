"""
So, the answer is BWBW.

"""

#Solution:

import itertools

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

for _ in range(int(input())):
    s1 = input()
    s2 = input()
    n = len(s1)
    max_hamming_distance = 0
    lexicographically_smallest_string = ''
    for s in itertools.product('WB', repeat=n):
        s = ''.join(s)
        hamming_distance_sum = hamming_distance(s, s1) + hamming_distance(s, s2)
        if hamming_distance_sum > max_hamming_distance:
            max_hamming_distance = hamming_distance_sum
            lexicographically_smallest_string = s
        elif hamming_distance_sum == max_hamming_distance:
            lexicographically_smallest_string = min(lexicographically_smallest_string, s)
    print(lexicographically_smallest_string)