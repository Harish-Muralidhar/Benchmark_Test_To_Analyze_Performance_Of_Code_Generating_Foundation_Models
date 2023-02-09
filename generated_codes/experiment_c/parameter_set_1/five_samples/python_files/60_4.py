'''


'''



# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=[]
    for i in range(n):
        x=[int(x) for x in input().split()]
        a.append(x)
    if n==1:
        if a[0][0]==0:
            print(0)
        else:
            print(-1)
    else:
        flag=0
        lst=[]
        s=0
        for i in range(n):
            if a[i][i]==1:
                lst.append(i)
                s+=1
        if s%2==0:
            for i in range(n):
                for j in range(n):
                    if a[i][j]==0 and i<j:
                        flag=1
                        break
            if flag==1:
                print(-1)
            else:
                print(0,end=" ")
                for i in range(1,n):
                    print(0,end=" ")
                print()
        else:
            for i in range(n):
                for j in range(n):
                    if a[i][j]==1 and i<j:
                        flag=1
                        break
            if flag==1:
                print(-1)
            else:
                print(0,end=" ")
                for i in lst:
                    print(1,end=" ")
                for i in range(1,n-s):
                    print(0,end=" ")
                print()