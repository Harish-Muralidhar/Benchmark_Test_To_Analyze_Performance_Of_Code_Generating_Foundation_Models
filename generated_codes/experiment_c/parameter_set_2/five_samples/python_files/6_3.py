'''

'''

import itertools

def min_max_diff(s1, s2):
    min_diff = float('inf')
    max_diff = float('-inf')
    for i in range(len(s1)):
        if s1[i] == '?' or s2[i] == '?':
            for j in range(26):
                if s1[i] == '?':
                    s1_copy = s1[:i] + chr(ord('a') + j) + s1[i+1:]
                else:
                    s1_copy = s1
                if s2[i] == '?':
                    s2_copy = s2[:i] + chr(ord('a') + j) + s2[i+1:]
                else:
                    s2_copy = s2
                diff = 0
                for k in range(len(s1)):
                    if s1_copy[k] != s2_copy[k]:
                        diff += 1
                min_diff = min(min_diff, diff)
                max_diff = max(max_diff, diff)
    return min_diff, max_diff

def min_max_diff_2(s1, s2):
    min_diff = float('inf')
    max_diff = float('-inf')
    for i in itertools.product(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], repeat=s1.count('?')):
        s1_copy = s1
        s2_copy = s2
        for j in range(s1.count('?')):
            s1_copy = s1_copy.replace('?', i[j], 1)
            s2_copy = s2_copy.replace('?', i[j], 1)
        diff