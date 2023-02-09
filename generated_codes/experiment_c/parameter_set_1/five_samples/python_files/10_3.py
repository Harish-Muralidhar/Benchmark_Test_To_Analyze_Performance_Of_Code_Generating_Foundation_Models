'''

Sample Input 1
4 2
1 2 3 4

Sample Output 1
8

Sample Input 2
10 2
5 5 5 5 5 5 5 5 5 5

Sample Output 2
625



'''


n,k=map(int,input().split())
arr=list(map(int,input().split()))
a=[]
for i in range(n):
    for j in range(i+1,min(i+k+1,n+1)):
        a.append(arr[i:j])
a=a[::-1]
ans=1
for i in a:
    m=min(i)
    ans=ans*m
print(ans%1000000007)