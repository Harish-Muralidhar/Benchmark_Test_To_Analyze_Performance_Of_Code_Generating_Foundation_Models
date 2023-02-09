'''

'''



from math import factorial
from functools import reduce
from operator import mul
import math
from itertools import permutations

t=int(input())
for i in range(t):
    a=int(input().split()[0])
    b=int(input().split()[1])
    x=a+b
    y=a
    z=1
    for i in range(a,x):
        z=z*i
    for i in range(y,1,-1):
        z=z/i
    print(int(z%531169))