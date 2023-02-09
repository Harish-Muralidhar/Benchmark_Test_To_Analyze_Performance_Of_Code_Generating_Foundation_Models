"""

Problem Setter: Dabas

Problem Tester: Dabas
"""

def play(li):
    count=0
    while len(li)!=0:
        ma=0
        for i in li:
            if i>ma:
                ma=i
        li.remove(ma)
        count+=1
    return count
t=int(input())
for i in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    li.sort()
    print(play(li))