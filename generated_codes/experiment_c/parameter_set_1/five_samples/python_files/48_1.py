'''

'''

t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    for j in range(n):
        a.append(int(input()))
    a.sort()
    c=0
    for k in range(n):
        if k!=n-1:
            if a[k]==a[k+1]:
                k=k+1
            elif a[k]!=a[k+1]:
                print(a[k])
                break
        else:
            print(a[k])
            break