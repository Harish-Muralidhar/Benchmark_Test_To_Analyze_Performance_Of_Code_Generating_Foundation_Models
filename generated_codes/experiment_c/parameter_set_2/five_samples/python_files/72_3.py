'''


'''

#code

def find_ways(n):
    if n==0 or n==1:
        return 1
    if n==2:
        return 2
    return find_ways(n-1)+find_ways(n-2)

def find_good_number(l,r,n):
    count=0
    for i in range(l,r+1):
        if find_ways(i)==i:
            count+=1
            if count==n:
                return i
    return -1

def find_path(n):
    path=''
    while n>0:
        if n%2==0:
            path+='.'
        else:
            path+='#'
        n=n//2
    return path[::-1]

t=int(input())
for i in range(t):
    l,r,n=map(int,input().split())
    good_number=find_good_number(l,r,n)
    if good_number==-1:
        print(good_number)
    else:
        print(good_number,find_path(good_number))