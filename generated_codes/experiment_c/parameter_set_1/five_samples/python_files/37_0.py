'''


Ans:

'''
import math
t=int(input())
for i in range(t):
    a,o,k=map(int,input().split())
    if(k>=min(a,o)):
        print(abs(a-o))
    else:
        print(k+(a+o-2*k))