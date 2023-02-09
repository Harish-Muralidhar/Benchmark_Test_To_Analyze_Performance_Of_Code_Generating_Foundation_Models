'''
'''

import math

t=int(input())
for i in range(t):
    n=int(input())
    
    
    print(int(n/100)+int(n%100/50)+int(n%50/10)+int(n%10/5)+int(n%5/2)+int(n%2/1))