'''


'''



for i in range(int(input())):
    a=int(input())
    print(a)


'''


GCD

'''

def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

a,b=map(int,input().split())
print(gcd(a,b))


'''


HackerRank-Lucky Number Eight

'''

for i in range(int(input())):
    n=int(input())
    a=list(input())
    sum=0
    for j in range(n):
        if a[j]=="8" and n-j>=11:
            sum=sum+1
    print(sum)


'''

HackerRank-CamelCase

'''

def camelcase(s):
    a=list(s)
    sum=1
    for i in range(len(a)):
        if a[i].isupper():
            sum=sum+1
    return sum

s=input()
print(camelcase(s))


'''

HackerRank-Sherlock and Squares

'''

import math
def squares(a,b):
    count=0
    for i in range(a,b+1):
        if math.sqrt(i).is_integer():
            count=count+1
    return count

for i in range(int(input())):
    a,b=map(int,input().split())
    print(squares(a,b))



'''

HackerRank-Halloween Sale

'''

def howManyGames(p, d, m, s):
    count=0
    while s>=p:
        count=count+1
        s=s-p
        p=max(p-d,m)
    return count



p,d,m,s=map(int,input().split())

print(howManyGames(p,d,m,s))




'''

HackerRank-Beautiful Triplets

'''

def beautifulTriplets(d, arr):
    count=0
    for i in range(len(arr)):
        a=arr[i]
        for j in range(i+1,len(arr)):
            b=arr[j]
            if a+d==b:
                for k in range(j+1,len(arr)):
                    c=arr[k]
                    if a+2*d==c:
                        count=count+1
    return count

n,d=map(int,input().split())
arr=list(map(int,input().split()))
print(beautifulTriplets(d,arr))
            



'''

HackerRank-Jumping on the Clouds

'''



def jumpingOnClouds(c):
    count=0
    i=0
    while i<len(c):
        if i+2<len(c) and c[i+2]==0:
            i=i+2
            count=count+1
        elif i+1<len(c) and c[i+1]==0:
            i=i+1
            count=count+1
        elif i+2>=len(c) and c[i+1]==0:
            i=i+1
            count=count+1
        else:
            i=i+1
    return count



n=int(input())
c=list(map(int,input().split()))
print(jumpingOnClouds(c))


'''

HackerRank-Repeated String

'''

def repeatedString(s, n):
    a=list(s)
    count=0
    m=len(a)
    for i in range(m):
        if a[i]=="a":
            count=count+1
    k=n//m
    count=count*k
    k=n%m
    for j in range(k):
        if a[j]=="a":
            count=count+1
    return count

s=input()
n=int(input())
print(repeatedString(s,n))