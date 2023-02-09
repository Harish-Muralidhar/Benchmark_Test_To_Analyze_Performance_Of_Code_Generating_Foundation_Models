'''

'''
def findPermutation(n,k):
    if n==k:
        print(-1)
    else:
        a=[];
        if k%2==0:
            a.append(k//2);
            i=k//2
            while i<n:
                a.append(i+1)
                a.append(i-k)
                i+=1
            a.sort()
            print(a)
        else:
            a.append((k+1)//2)
            a.append((k-1)//2)
            i=1
            while i<n-1:
                a.append(i+1)
                a.append(i-k)
                i+=1
            a.sort()
            print(a)

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    findPermutation(n,k)