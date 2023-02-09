"""


"""

# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    count=0
    while n>0:
        if n>=2048:
            n=n-2048
            count+=1
            continue
        if n>=1024:
            n=n-1024
            count+=1
            continue
        if n>=512:
            n=n-512
            count+=1
            continue
        if n>=256:
            n=n-256
            count+=1
            continue
        if n>=128:
            n=n-128
            count+=1
            continue
        if n>=64:
            n=n-64
            count+=1
            continue
        if n>=32:
            n=n-32
            count+=1
            continue
        if n>=16:
            n=n-16
            count+=1
            continue
        if n>=8:
            n=n-8
            count+=1
            continue
        if n>=4:
            n=n-4
            count+=1
            continue
        if n>=2:
            n=n-2
            count+=1
            continue
        if n>=1:
            n=n-1
            count+=1
    print(count)