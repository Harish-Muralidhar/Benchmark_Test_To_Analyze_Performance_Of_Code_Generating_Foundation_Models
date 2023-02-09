'''

Sample Input
3
3 2 5
3 3 10
5 4 7

Sample Output
2
3 2 
1
10 
3
5 1 1

Explaination
Example case 1. We first pick 3 coins from [3, 2] then we pick 2 coins from [2, 1]Example case 2. As 3rd column contains 10 coins in cell [5, 3] we pick it.Example case 3. We first pick 5 coins from [5, 4] then we pick 1 coin from [3, 3] and again we pick 1 coin from [2, 2].

'''

#CODE
import math
#import numpy as np
for _ in range(int(input())):
    #r,c,g=input()
    r,c,g=map(int,input().split())
    #coins_in_column=[]
    #for i in range(c):
    #    coins_in_column.append(sum(np.array(list(range(r)))[:i+1]))
    coins_in_column=[]
    for i in range(c+1):
        coins_in_column.append(int(sum(math.factorial(r)/(math.factorial(i)*math.factorial(r-i))[:i+1])))
    #print(coins_in_column)
    r=c
    coins_collected=0
    coins_collected_in_columns=[]
    while(coins_collected!=g):
        if(coins_in_column[r]<=(g-coins_collected)):
            coins_collected_in_columns.append(coins_in_column[r])
            coins_collected+=coins_in_column[r]
            #print(coins_collected)
            #print(coins_collected_in_columns)
            r-=1
        else:
            coins_collected_in_columns.append(g-coins_collected)
            coins_collected=g
    print(len(coins_collected_in_columns))
    print(*coins_collected_in_columns)