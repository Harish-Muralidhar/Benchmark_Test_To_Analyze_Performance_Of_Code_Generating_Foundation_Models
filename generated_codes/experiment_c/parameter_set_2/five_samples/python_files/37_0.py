"""


Test 3: Chef will buy 1 apple by paying 1 gold coin, and will buy 1 orange by paying 1 gold coin. He will have 2 apples and 3 oranges.

"""


t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    if n>m:
        n,m=m,n
    if n>=k:
        print(0)
    else:
        if m>=k:
            print(k-n)
        else:
            print(m-n)