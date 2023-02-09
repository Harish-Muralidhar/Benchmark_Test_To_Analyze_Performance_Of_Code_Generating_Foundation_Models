'''

'''

import math

x = int(input())
y = float(input())

if x%5==0 and x<=y:
    y = y - x - 0.5
print(round(y,2))