'''

'''

import math

def isPrime(n):
    if(n<=1):
        return False
    if(n<=3):
        return True
    if(n%2==0 or n%3==0):
        return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if(n%i==0 or n%(i+2)==0):
            return False
    return True

def countPrime(a,b):
    count=0
    for i in range(a+1):
        for j in range(b+1):
            if(i+j>1):
                if(isPrime(i+j)):
                    count+=1
    return count

t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    print(countPrime(a,b))