"""


Explanation

In this example, your cannon is at (0, 0), the enemy battleship is a horizontal line from (-2, 2) to (1, 2). There is a rock at (0, 2). 
Your cannon can destroy the two guns at (-2, 2) and (-1, 2).

"""

#import math

t=int(input())
#t=1
while(t>0):
    Y,X1,X2 = [int(x) for x in input().split()]
    if(Y>0):
        Y1 = Y//2
    elif(Y<0):
        Y1 = Y//2 + 1
    else:
        Y1 = 0
    if(Y1>X1):
        X1 = Y1
    if(Y1>X2):
        X2 = Y1
    print(X2-X1+1)
    t=t-1