'''


Solution:

'''
import sys

def broken_telephone(n,A):
    count=0
    for i in range(1,n-1):  #Ignoring first and last player
        if A[i]!=A[i-1] and A[i]!=A[i+1]:
            count+=1
        else:
            continue
    return count

def main():
    t=int(input())
    while t>0:
        n=int(input())
        A=list(map(int,input().split()))
        print(broken_telephone(n,A))
        t-=1

main()

'''
Optimised Solution:

def main():
    t = int(input())
    while t:
        n = int(input())
        A = list(map(int,input().split()))
        count = 0
        for i in range(1,n-1):
            if A[i] != A[i+1] and A[i] != A[i-1]:
                count += 1
        print(count)
        t-=1

main()

'''