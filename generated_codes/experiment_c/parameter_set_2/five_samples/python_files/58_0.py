'''

'''

# cook your dish here
# cook your dish here
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1,n+1):
            s = sum(a[i:j])
            if s & (1<<(m-1)) == 0:
                ans += 1
    print(ans%1000000009)