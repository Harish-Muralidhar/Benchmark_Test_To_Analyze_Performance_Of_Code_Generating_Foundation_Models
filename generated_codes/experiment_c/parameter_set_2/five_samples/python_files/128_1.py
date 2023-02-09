'''
'''

from itertools import combinations
t = int(input())
for i in range(t):
    s = input()
    k = int(input())
    l = list(combinations(s,k))
    l.sort()
    print("".join(l[0]))