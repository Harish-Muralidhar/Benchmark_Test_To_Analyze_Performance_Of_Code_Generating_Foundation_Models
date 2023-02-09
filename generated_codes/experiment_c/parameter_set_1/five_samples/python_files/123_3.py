'''

Testcase 1: The minimal possible absolute difference is 1 and the number of pairs is 4.

'''

# Write your code here
for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    mi=min(a)
    ma=max(a)
    if abs(mi+ma-k)==0:
        print("0",n*(n-1)//2)
    else:
        c=0
        for i in range(n):
            for j in range(i+1,n):
                if abs(a[i]+a[j]-k)==abs(mi+ma-k):
                    c+=1
        print(abs(mi+ma-k),c)