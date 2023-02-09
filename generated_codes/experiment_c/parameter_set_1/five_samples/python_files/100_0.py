'''


'''

# Write your code here

for i in range(int(input())):
    n,m=map(int,input().split())
    ls=list(map(int,input().split()))
    l=[]
    for j in range(1,2**n):
        k=j
        c=0
        s=0
        while(k>0):
            if(k&1==1):
                s+=ls[c]
            c+=1
            k=k>>1
        l.append(s)
    if(m in l):
        print("Yes")
    else:
        print("No")