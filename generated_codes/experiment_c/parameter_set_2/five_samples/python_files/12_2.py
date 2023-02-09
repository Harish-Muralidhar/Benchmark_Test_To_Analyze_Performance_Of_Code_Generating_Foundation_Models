'''


'''

t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    r=0
    g=0
    b=0
    for j in s:
        if(j=='R'):
            r+=1
        elif(j=='G'):
            g+=1
        elif(j=='B'):
            b+=1
    print(n-(max(r,g,b)))