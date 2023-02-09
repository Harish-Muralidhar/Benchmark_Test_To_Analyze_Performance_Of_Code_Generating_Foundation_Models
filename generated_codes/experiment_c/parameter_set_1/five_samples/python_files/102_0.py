'''
 = 2, 100, or 3.

'''

k=[int(x) for x in input().split()]
n=int(input())
d={}
for i in range(n):
    string=input()
    operator,li,logical_value=string.split()
    li=int(li)
    d[li]=logical_value
    if operator=='<':
        for x in range(1,li):
            d[x] ='No'
    if operator=='>':
        for x in range(li+1,1000001):
            d[x] ='No'
    if operator=='=':
        for x in range(1,1000001):
            if x==li:
                d[x]=logical_value
            else:
                d[x]='No'
count=0
for i in d:
    if d[i]=='Yes':
        count+=1
print(count)