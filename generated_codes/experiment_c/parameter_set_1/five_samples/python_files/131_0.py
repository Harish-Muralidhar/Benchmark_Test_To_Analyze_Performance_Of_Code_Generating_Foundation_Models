'''
'''

# Write your code here
t=int(input())
while(t>0):
    n,p=map(float,input().split())
    if(p==1 or p==0 or n==0):
        print(1000000000.0,1000000000.0)
    else:
        x=pow(p,n)
        y=(1-x)/(1-p)
        print(1000000000.0/y,1000000000.0/y-1000000000.0)
    t-=1