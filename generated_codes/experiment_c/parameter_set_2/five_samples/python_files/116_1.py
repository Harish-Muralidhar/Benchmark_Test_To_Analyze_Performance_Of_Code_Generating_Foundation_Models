'''


'''

# Write your code here

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return a*b//gcd(a,b)

def lcm_list(a):
    if len(a)==1:
        return a[0]
    else:
        return lcm(a[0],lcm_list(a[1:]))

def solve(a):
    if len(a)==1:
        if a[0]==1:
            return 1
        else:
            return 0
    else:
        l=lcm_list(a)
        if l==1:
            return 1
        else:
            return 0

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        print(solve(a))