'''

'''

def great(a,b):
    if(a>b):
        return a
    else:
        return b
    
def small(a,b):
    if(a<b):
        return a
    else:
        return b

def main():
    t=int(input())
    while(t>0):
        n=int(input())
        l=list(map(int,input().split()))
        e,o=l[0],l[1]
        if (e+o)!=(n*(n+1)//2):
            print(-1)
        else:
            if (e%2==0 and o%2==0) or (e%2!=0 and o%2!=0):
                if e%2==0:
                    n1=e//2
                    n2=o//2
                else:
                    n1=o//2
                    n2=e//2
                for i in range(1,n1+1):
                    print(2*i,end=" ")
                for i in range(1,n2+1):
                    print(2*i-1,end=" ")
            else:
                print(-1)
        t-=1

if __name__=="__main__":
    main()