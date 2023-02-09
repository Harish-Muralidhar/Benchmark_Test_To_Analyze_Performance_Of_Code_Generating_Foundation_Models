'''

'''

# your code goes here
T=int(input())
for i in range(T):
    n=int(input())
    items=list(map(int,input().split()))
    items.sort()
    items.reverse()
    count=0
    price=0
    for i in items:
        count+=1
        if(count%2!=0):
            price+=i
    print(price)