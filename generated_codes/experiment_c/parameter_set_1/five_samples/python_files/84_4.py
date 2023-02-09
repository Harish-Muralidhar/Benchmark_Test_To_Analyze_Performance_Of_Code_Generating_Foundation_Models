'''

'''

import math
t=int(input())
for i in range(t):
    R,C,G=map(int,input().rstrip().split())
    row=[]
    x=0
    while x<=R:
        row.append(x)
        x+=1
    coins=[]
    for i in range(len(row)):
        for j in range(len(row)):
            if j<=i:
                coins.append(math.factorial(row[i])//(math.factorial(row[j])*math.factorial(row[i]-row[j])))
    sum=0
    for i in range(0,C):
        if C-i-1<0:
            break
        else:
            sum+=coins[C-i-1]
    if G>=sum:
        print(0)
        print(G)
    else:
        result=[]
        while G!=0:
            for i in range(len(row)):
                if i<=C and G-coins[i]>=0:
                    result.append(coins[i])
                    G=G-coins[i]
                    C=C-1
                    break
        print(len(result))
        print(*result)