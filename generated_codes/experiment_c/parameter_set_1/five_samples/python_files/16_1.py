

Solution:

# Write your code here
import math

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def gcd3(a,b,c):
    return gcd(a,gcd(b,c))

def gcd4(a,b,c,d):
    return gcd(gcd(a,b),gcd(c,d))
        
    
t=int(input())
for i in range(t):
    n,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    cnt=0
    if n==1:
        if arr[0]%k==0:
            print(0)
        else:
            print(-1)
        continue
    elif n==2:
        if arr[0]%k==0  and arr[1]%k==0:
            print(0)
        else:
            a=arr[0]
            b=arr[1]
            c=gcd(a,b)
            if c%k==0:
                print(0)
            else:
                d=gcd(c,k)
                d1=arr[0]%d
                d2=arr[1]%d
                d3=k%d
                x1=d-d1
                x2=d-d2
                x3=d-d3
                if x1+x2<=arr[0] and x1+x2<=arr[1]:
                    a=x1
                    b=x2
                    cnt+=a+b
                else:
                    a=d1
                    b=d2
                    cnt+=a+b
                print(cnt)
    elif n==3:
        if arr[0]%k==0 and arr[1]%k==0 and arr[2]%k==0:
            print(0)
        else:
            a=arr[0]
            b=arr[1]
            c=arr[2]
            cnt=0
            d=gcd3(a,b,c)
            if d%k==0:
                print(0)
            else:
                e=gcd(d,k)
                d1=arr[0]%e
                d2=arr[1]%e
                d3=arr[2]%e
                d4=k%e
                x1=e-d1
                x2=e-d2
                x3=e-d3
                x4=e-d4
                if x1+x2+x3<=max(arr[0],arr[1],arr[2]):
                    a=x1
                    b=x2
                    c=x3
                    cnt+=a+b+c
                else:
                    a=d1
                    b=d2
                    c=d3
                    cnt+=a+b+c
                print(cnt)
    elif n==4:
        if arr[0]%k==0 and arr[1]%k==0 and arr[2]%k==0 and arr[3]%k==0:
            print(0)
        else:
            a=arr[0]
            b=arr[1]
            c=arr[2]
            d=arr[3]
            cnt=0
            e=gcd4(a,b,c,d)
            if e%k==0:
                print(0)
            else:
                f=gcd(e,k)
                d1=arr[0]%f
                d2=arr[1]%f
                d3=arr[2]%f
                d4=arr[3]%f
                d5=k%f
                x1=f-d1
                x2=f-d2
                x3=f-d3
                x4=f-d4
                x5=f-d5
                if x1+x2+x3+x4<=max(arr[0],arr[1],arr[2],arr[3]):
                    a=x1
                    b=x2
                    c=x3
                    d=x4
                    cnt+=a+b+c+d
                else:
                    a=d1
                    b=d2
                    c=d3
                    d=d4
                    cnt+=a+b+c+d
                print(cnt)