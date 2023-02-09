'''

'''

import math
t=int(input())
while(t):
   n=list(map(int,input().split()))
   if(sum(n)==180):
      print("YES")
   else:
      print("NO")
   t=t-1