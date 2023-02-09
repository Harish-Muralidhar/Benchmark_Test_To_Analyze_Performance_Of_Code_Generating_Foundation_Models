'''

Case 2:

Add one ball to the first two buckets.

Case 3:

Add two balls to the first two buckets.

Case 4:

Add one ball to the first two buckets, and two balls to the last bucket.


Case 1:

Add one ball to the first and the last buckets, and two balls to the second bucket.


Case 2:

Add one ball to each of the buckets.

Case 3:

Add one ball to the first and the last buckets, and two balls to the second bucket.


Case 4:

Add one ball to the first and the last buckets, and two balls to the second bucket.

'''

import math

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def find(arr,n):
    arr.sort()
    count=0
    for i in range(n-1):
        if(arr[i+1]>arr[i]):
            if(gcd(arr[i+1],arr[i])==1):
                count+=(arr[i+1]-arr[i])
            else:
                arr[i+1]+=1
    return count

t=int(input())
while(t>0):
    n=int(input())
    arr=list(map(int,input().split()))
    print(find(arr,n))
    t-=1