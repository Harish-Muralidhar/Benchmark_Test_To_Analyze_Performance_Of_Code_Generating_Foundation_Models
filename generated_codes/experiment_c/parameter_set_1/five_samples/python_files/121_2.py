"""
 

"""
def distance(l,r):
    dist=0
    while(l!=r):
        if(l<r):
            l=l+1
        else:
            r=r+1
        dist=dist+1
    return dist
t=int(input())
for i in range(t):
    n=int(input())
    print(distance(0,n)+distance(n,0)+distance(0,n-1))