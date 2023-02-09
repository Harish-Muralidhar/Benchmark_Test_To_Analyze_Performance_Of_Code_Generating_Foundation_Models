'''


'''

# Test case

#Input:
#2
#4 3
#111
#100
#110
#000
#2 2
#10
#01

#Output:
#4
#0

for _ in range(int(input())):
   r,c=map(int,input().split())
   a=[]
   for i in range(r):
       a.append(input())
   c=0
   for i in range(c):
       for j in range(r-1):
           for k in range(j+1,r):
               if(a[j][i]=='1' and a[k][i]=='1'):
                   c+=1
   print(c)