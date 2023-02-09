"""
"""

import sys

def calculate(n):
    notes = [1,2,5,10,50,100]
    count = 0
    for i in range(5,-1,-1):
        if n>=notes[i]:
            count+=int(n/notes[i])
            n=n%notes[i]
        if n==0:
            break
    return count

t = int(input())
for i in range(t):
    n = int(input())
    print(calculate(n))