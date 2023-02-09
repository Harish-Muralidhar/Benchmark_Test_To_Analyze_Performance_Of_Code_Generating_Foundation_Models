/*
*/

import math

def bico_grid(R,C,G):
    i=R
    j=C
    res=[]
    while(G>0 and i>=0 and j>=0):
        if i==0 and j==0:
            break
        if (i<j) and G>0:
            res.append(G)
            break
        elif (i>=j) and G>0:
            val=math.factorial(i)//(math.factorial(i-j)*math.factorial(j))
            if val<=G:
                res.append(val)
                G-=val
                j-=1
            else:
                i-=1
    return res
        
if __name__=="__main__":
    T=int(input())
    for i in range(T):
        R,C,G=map(int,input().split())
        res=bico_grid(R,C,G)
        print(len(res))
        print(*res)

# Time Complexity=O(RC)