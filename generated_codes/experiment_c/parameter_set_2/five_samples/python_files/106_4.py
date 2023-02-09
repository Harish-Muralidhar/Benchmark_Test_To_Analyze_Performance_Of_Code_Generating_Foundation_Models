"""


"""

# Write your code here

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    while q:
        q-=1
        qtype,x,y,v = map(int,input().split())
        if qtype==1:
            for i in range(x-1,y):
                a[i]+=v
                a[i]%=M
        elif qtype==2:
            for i in range(x-1,y):
                a[i]*=v
                a[i]%=M
        elif qtype==3:
            for i in range(x-1,y):
                a[i]=v
        else:
            sum = 0
            for i in range(x-1,y):
                sum+=a[i]
            print(sum%M)

main()