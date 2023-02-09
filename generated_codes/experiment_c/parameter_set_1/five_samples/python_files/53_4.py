'''

'''

t=int(input())
while(t):
    n=int(input())
    a=input().split()
    s=''
    for i in range(n):
        s+=a[i]
    c=0
    for i in s:
        if(s.count(i)%2!=0):
            c+=1
    print(c)
    t-=1