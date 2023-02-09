'''


'''

# Write your code here
import math
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    a=math.log(a,2)
    b=math.log(b,2)
    print(int(abs(a-b)))