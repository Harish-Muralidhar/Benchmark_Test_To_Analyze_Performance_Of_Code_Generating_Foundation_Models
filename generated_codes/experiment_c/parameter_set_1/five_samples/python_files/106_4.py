'''



Input:
5 5
10 20 30 40 50
1 1 5 10
2 3 5 5
4 3 5
3 5 5 60
4 1 5
Output:
110
60

Explanation:
Initial A: [10, 20, 30, 40, 50] A after first query : [ 20, 30, 40, 50, 60] A after second query : [ 20, 60, 60, 60, 60] Result of third query : 20 + 60 + 60 + 60 + 60 = 210 Result of fourth query : 60



'''

#Python 3

#!/bin/python3

import os
import sys
import math

# Complete the solve function below.
def solve(n, ar, q, qry):
    #
    # Write your code here.
    #
    ans=list()
    while True:
        if q==0:
            break
        t,x,y,v=map(int,input().split())
        if t==1:
            for i in range(x-1,y):
                ar[i]+=v
                ar[i]=ar[i]%(pow(10,9)+7)
        elif t==2:
            for i in range(x-1,y):
                ar[i]*=v
                ar[i]=ar[i]%(pow(10,9)+7)
        elif t==3:
            for i in range(x-1,y):
                ar[i]=v
        elif t==4:
            sum=0
            for i in range(x-1,y):
                sum+=ar[i]
            ans.append(sum)
        q-=1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(n, arr, m, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()