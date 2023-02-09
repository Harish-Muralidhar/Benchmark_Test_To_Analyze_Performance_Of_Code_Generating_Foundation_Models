'''
For second query, 2 is directly connected to 3 by an edge. Hence distance 1.
For third query, 4 is directly connected to 3 by an edge. Hence distance 1.

'''
import math
def get_depth(x):
    return int(math.log(x,2))
n = int(input())
for i in range(n):
    [x,y] = map(int,input().split())
    x1 = get_depth(x)
    y1 = get_depth(y)
    h = max(x1,y1)
    while(h != 0):
        if(x == y):
            break
        elif(x > y):
            x = x//2
            h = get_depth(x)
        else:
            y = y//2
            h = get_depth(y)
    print(get_depth(x))