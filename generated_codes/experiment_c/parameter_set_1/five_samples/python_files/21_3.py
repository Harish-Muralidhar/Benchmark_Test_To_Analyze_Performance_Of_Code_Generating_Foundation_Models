'''

'''

T=int(input())

for i in range(0,T):
    x=input().split()
    a=int(x[0])
    b=int(x[1])
    print(a%b)

'''
Method 2: (Using arithmetic operators)

T=int(input())

for i in range(0,T):
    x=input().split()
    a=int(x[0])
    b=int(x[1])
    print(a-((a//b)*b))
'''