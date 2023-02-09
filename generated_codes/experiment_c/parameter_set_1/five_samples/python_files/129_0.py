'''

'''

def func(n,m):
    S=[]
    for i in range(m):
        l=[]
        l.append(int(input()))
        for j in range(l[0]):
            l.append(int(input()))
        S.append(l)
    print()
    print(S)
    print()
    X=[]
    for i in range(n):
        X.append(i)
    print(X)

    D={i:0 for i in X}
    for i in S:
        for j in range(1,len(i)):
            D[i[j]]+=1
    print(D)
    sorted(D)
    print(D)

    A=[]
    for i in S:
        for j in range(1,len(i)):
            if D[i[j]]==1:
                A.append(i[j])
    print(A)

    for i in A:
        if i in X:
            X.remove(i)

    print(X)

    print(len(A)+len(X))


t=int(input())
for i in range(t):
    n=int(input())
    m=int(input())
    func(n,m)