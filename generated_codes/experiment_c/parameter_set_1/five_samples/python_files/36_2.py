'''

'''
T=int(input())
for t in range(T):
    n,k=map(int,input().split())
    d=input().split()
    flag=0
    for i in range(k):
        l=int(input().split()[0])
        a=input().split()
        
        for j in d:
            if j in a:
                print("YES",end=" ")
                flag=1
                break
        if flag==0:
            print("NO",end=" ")
        flag=0
    print()