'''
 

Example case 2. In this example 2 as 20 is greater than 10.
 

Example case 3. In this example 3 as 10 is equal to 10.

'''

#Write your code here

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    if A == B:
        print('=')
    elif A > B:
        print('≻')
    else:
        print('≺')