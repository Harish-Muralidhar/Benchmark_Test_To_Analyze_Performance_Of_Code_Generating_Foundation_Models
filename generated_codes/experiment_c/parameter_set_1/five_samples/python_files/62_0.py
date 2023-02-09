'''

'''

n,q=map(int,input().split())
array=list(map(int,input().split()))
for _ in range(q):
    q_type,l,r,x=map(int,input().split())
    if q_type==0:
        print(min(array[l:r+1]))
    else:
        for i in range(l,r+1):
            array[i]&=x