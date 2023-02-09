'''


Input:
1
3
10 11 15

Output:
0


Explanation

The number of balls are already in a non-decreasing order and their GCD is strictly greater than 1.



Input:
1
6
2 3 4 5 48 50

Output:
1

Explanation

Add one more ball to the first bucket.

'''


from fractions import gcd
T=int(input())
for i in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    z=0
    for  i in range(len(A)-1):
        if A[i]>=A[i+1]:
            if gcd(A[i],A[i+1])==1:
                z+=1
    print(z)