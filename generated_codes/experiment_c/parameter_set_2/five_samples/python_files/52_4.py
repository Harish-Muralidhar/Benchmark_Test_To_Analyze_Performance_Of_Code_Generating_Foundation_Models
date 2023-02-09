"""

"""


def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return (a*b)//gcd(a,b)

def add_fractions(a,b):
    return (a[0]+a[1],b[0]+b[1])

def max_fraction(a,b):
    if a[0]*b[1] > b[0]*a[1]:
        return (a[0],a[1])
    else:
        return (b[0],b[1])

def reduce_fraction(a,b):
    g = gcd(a,b)
    return (a//g,b//g)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = []
        b = []
        for j in range(n):
            x,y = map(int,input().split('/'))
            a.append(x)
            b.append(y)
        for j in range(n):
            ans = (a[j],b[j])
            for k in range(j+1,n):
                ans = add_fractions(ans,(a[k],b[k]))
            ans = reduce_fraction(ans[0],ans[1])
            print(str(ans[0])+'/'+str(ans[1]))
        print()

if __name__ == '__main__':
    main()