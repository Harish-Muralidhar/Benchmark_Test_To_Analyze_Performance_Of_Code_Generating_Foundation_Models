'''
Example case 2. Game will have 2 turns. In first turn Sasha will choose 2, and Chef will choose 1. In second turn Sasha will choose 3, and Chef will choose 4. Hence answer is 1.5. 
Example case 3. Game will have 2 turns. In first turn Sasha will choose 2, and Chef will choose 2. In second turn Sasha will choose 4, and Chef will choose 2. Since 2^2=4^2, Sasha won't kiss Chef. Hence answer is 0.

'''

import random
import math

def sasha_kiss(n,a,b):
    count=0
    for i in range(n):
        x=random.choice(a)
        y=random.choice(b)
        if x**y>y**x:
            count+=1
        a.remove(x)
        b.remove(y)
    return count

def expected_value(n,a,b):
    sum=0
    for i in range(10000):
        sum+=sasha_kiss(n,a,b)
    return sum/10000

t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    print(expected_value(n,a,b))