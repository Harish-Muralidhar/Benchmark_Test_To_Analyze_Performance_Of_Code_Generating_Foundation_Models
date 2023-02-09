'''


'''

def gcd(a,b):
    return a if b==0 else gcd(b,a%b)

def gcdall(a):
    b = a[0]
    for i in range(1,len(a)):
        b = gcd(b,a[i])
    return b

def fun(a):
    if(gcdall(a)>1):
        return 0
    else:
        m = max(a)
        ans = -1
        for i in range(1,m+1):
            if(gcdall(a+[i])>1):
                ans = i
                break
        if(ans==-1):
            return -1
        else:
            return 1+fun(a+[i])    


for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    print(fun(l))