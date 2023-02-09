
#code

for i in range(int(input())):
    n,m=[int(x) for x in input().split()]
    arr=[int(x) for x in input().split()]
    arr2=[]
    bit_arr=[0]*m
    for i in range(n):
        t=bin(arr[i])[2:]
        while(len(t)<m):
            t='0'+t
        arr2.append(t)
    for i in range(m):
        count1=0
        for j in range(n):
            if(arr2[j][m-i-1]=='1'):
                count1+=1
        if(count1>=n-count1):
            bit_arr[i]=1
    s=0
    for i in range(m):
        if(bit_arr[i]==1):
            s+=(2**i)
    print(s)