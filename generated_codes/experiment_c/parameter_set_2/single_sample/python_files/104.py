'''

'''

import random

def generate_string(n):
    s = ""
    for i in range(n):
        s += random.choice(["A", "B"])
    return s

def find_subsequence(s):
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            if s.count(s[i:j]) == 2:
                return s[i:j]
    return -1

t = int(input())
for i in range(t):
    n = random.randint(1, 100)
    s = generate_string(n)
    print(s)
    print(find_subsequence(s))