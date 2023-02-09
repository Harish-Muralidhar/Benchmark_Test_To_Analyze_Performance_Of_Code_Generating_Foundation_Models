'''
 = 1, 2, 3.



Solution :

t=int(input())
while t:
    t=t-1
    k=int(input())
    l=[]
    while k:
        k=k-1
        s=list(map(str,input().split()))
        l.append(s)
    print(l)
    if l[0][0]==l[1][0]:
        if l[0][2]=='Yes' and l[1][2]=='No':
            print(0)
        else:
            print(1)
    else:
        print(0)

'''