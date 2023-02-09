'''

'''

for i in range(int(input())):
    q,p=map(int,input().split())
    if q>1000:
        print(q*p*0.9)
    else:
        print(q*p)