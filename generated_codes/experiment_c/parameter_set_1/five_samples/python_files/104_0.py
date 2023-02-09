'''

'''

import random

def checkSubsequence(s,t):
    it = iter(t)
    return all(c in it for c in s)


for _ in range(int(input())):
    s = input()
    t = s
    while True:
        t = random.choice(list(t))
        if checkSubsequence(s,t) and checkSubsequence(t,s):
            break
    else:
        t = -1
    print(t)