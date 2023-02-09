'''


Hint:

The method to solve this problem is to find the number of fruits to be bought. This can be done by subtracting the number of fruits present with the chef and then dividing by 2. This is because you will get the number of fruits to be bought from both the baskets.

'''



for _ in range(int(input())):
    n,m,k = map(int,input().split())
    if abs(n-m)<=k:
        print(0)
    else:
        if n>m:
            print(n-m-k)
        else:
            print(m-n-k)