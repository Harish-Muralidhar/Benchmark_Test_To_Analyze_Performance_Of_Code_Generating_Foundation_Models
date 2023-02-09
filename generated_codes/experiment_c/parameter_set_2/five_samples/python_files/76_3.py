"""

"""

# cook your dish here
t=int(input())
for _ in range(t):
    x=int(input())
    b=int(input())
    dishes=[]
    for i in range(b):
        dishes.append(list(map(int,input().split())))
    c=int(input())
    clans=[]
    for i in range(c):
        clans.append(list(map(int,input().split())))
    dishes.sort()
    clans.sort()
    #print(dishes)
    #print(clans)
    i=0
    j=0
    count=0
    while(i<b and j<c):
        if(dishes[i][0]<clans[j][0]):
            count+=dishes[i][1]
            i+=1
        elif(dishes[i][0]>clans[j][0]):
            count+=clans[j][1]
            j+=1
        else:
            count+=max(dishes[i][1],clans[j][1])
            i+=1
            j+=1
    while(i<b):
        count+=dishes[i][1]
        i+=1
    while(j<c):
        count+=clans[j][1]
        j+=1
    print(count)