'''
Example case 2. In this example 2 as 20 is greater than 10.
Example case 3. In this example 3 as both are equal.

'''
T = int(input())
for i in range(T):
    a,b = [int(x) for x in input().split()]
    if a==b:
        print("=")
    elif a<b:
        print("<")
    else:
        print(">")