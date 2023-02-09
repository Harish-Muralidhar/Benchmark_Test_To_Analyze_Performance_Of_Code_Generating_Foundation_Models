'''

'''


for i in range(int(input())):
    a,b,c=map(int,input().split())
    temp=abs(a-b)
    if c>=temp:
        print(0)
    else:
        print(temp-c)