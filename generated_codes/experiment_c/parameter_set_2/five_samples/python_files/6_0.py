'''

'''

import itertools

def get_diff(s1, s2):
    diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff += 1
    return diff

def get_min_max_diff(s1, s2):
    min_diff = len(s1)
    max_diff = 0
    for i in itertools.product(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], repeat=s1.count('?')):
        s1_tmp = s1
        s2_tmp = s2
        for j in range(len(i)):
            s1_tmp = s1_tmp.replace('?', i[j], 1)
            s2_tmp = s2_tmp.replace('?', i[j], 1)
        diff = get_diff(s1_tmp, s2_tmp)
        if diff < min_diff:
            min_diff = diff
        if diff > max_diff:
            max_diff = diff
    return min_diff, max_diff

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s1 = input()
        s2 = input()
        print(' '.join(map(str, get_min_max_diff(s1, s2))))