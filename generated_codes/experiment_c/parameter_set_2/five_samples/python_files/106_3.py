'''


'''

def add(a,b):
    return (a+b)%M

def mul(a,b):
    return (a*b)%M

def build(node,start,end):
    if start==end:
        tree[node]=A[start]
    else:
        mid=(start+end)//2
        build(2*node,start,mid)
        build(2*node+1,mid+1,end)
        tree[node]=add(tree[2*node],tree[2*node+1])

def update(node,start,end,l,r,val):
    if start>end or start>r or end<l:
        return
    if start==end:
        tree[node]=mul(tree[node],val)
        return
    mid=(start+end)//2
    update(2*node,start,mid,l,r,val)
    update(2*node+1,mid+1,end,l,r,val)
    tree[node]=add(tree[2*node],tree[2*node+1])

def query(node,start,end,l,r):
    if start>end or start>r or end<l:
        return 0
    if start>=l and end<=r:
        return tree[node]
    mid=(start+end)//2
    p1=query(2*node,start,mid,l,r)
    p2=query(2*node+1,mid+1,end,l,r)
    return add(p1,p2)

N,Q=map(int,input().split())
A=list(map(int,input().split()))
tree=[0]*(4*N)
build(1,0,N-1)
for i in range(Q):
    q=list(map(int,input().split()))
    if q[0]==1:
        update(1,0,N-1,q[1]-1,q[2]-1,q[3])
    elif q