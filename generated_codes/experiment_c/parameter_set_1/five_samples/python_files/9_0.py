"""

Solution:
"""
import sys
import os
import math
import random
from collections import Counter,defaultdict
from itertools import product,permutations,combinations,accumulate
from operator import itemgetter
try:
    sys.setrecursionlimit(100000)
except:
    pass

try:
    sys.stdin = open('input.txt')
    sys.stdout = open('output.txt', 'w')
except:
    pass

def read():
    return sys.stdin.readline().strip()

def write(value):
    sys.stdout.write(str(value))

def writeln(value):
    write(value)
    write('\n')

def debug(*args):
    sys.stderr.write('DEBUG: ')
    sys.stderr.write(' '.join(map(str,args))+'\n')

s = read()
moves = 0
while True:
    try:
        ind=s.index('CHEF')
        moves += 1
        s=s[:ind]+s[ind+4:]
    except:
        break
    
write(moves)