'''

Explanation :

In the first test case, there are 12 ways to place the knights. (1,1) and (2,2), (1,1) and (2,1), (1,2) and (2,2), (1,2) and (2,1) are not valid because the knights will attack each other.

In the second test case, there are 26 ways to place the knights.


'''
 
t = int(input())
curr = []
for _ in range(t):
    a,b = map(int,input().split())
    curr.append((a,b))
    if (a==1) or (b==1):
        print(a*b)
        continue
    if (a==2) or (b==2):
        if (a==2):
            if b%4==0:
                print(b)
            elif b%4==1:
                print(b+1)
            else:
                print(b+2)
        else:
            if a%4==0:
                print(a)
            elif a%4==1:
                print(a+1)
            else:
                print(a+2)
        continue
    else:
        print((a*b)+((a-2)*(b-2)))