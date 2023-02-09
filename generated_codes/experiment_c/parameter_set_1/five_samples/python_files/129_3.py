'''

Explanation

In the first example, the atoms are {0,1,2}, {3}, and {4}. Note that we cannot use only 2 atoms. For example, if we used {0,1} and {2,3,4} then 4 is covered twice.

In the second example, the atoms are {0,1}, {2}, {3}, and {4}.

'''

def find_atoms(x):
    for i in range(len(x)):
        x[i]=set(x[i])
    z=[]
    for i in range(len(x)):
        if x[i] not in z:
            f=1
            for j in range(len(x)):
                if i==j:
                    continue
                elif len(x[i].intersection(x[j]))>0:
                    f=0
                    break
            if f==1:
                z.append(x[i])
    return len(z)


t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    x=[]
    for j in range(m):
        z=list(map(int,input().split()))
        y=[]
        for k in range(1,len(z)):
            y.append(z[k])
        x.append(y)
    print(find_atoms(x))