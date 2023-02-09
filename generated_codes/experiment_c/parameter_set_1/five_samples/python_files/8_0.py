'''
Example case 2. In this example 2 as 20 is greater than 10.
Example case 3. In this example 3 as 10 is equal to 10.

'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a>b:
        print("<")
    elif a<b:
        print(">")
    else:
        print("=")