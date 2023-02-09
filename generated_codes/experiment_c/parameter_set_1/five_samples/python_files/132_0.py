'''


'''
import heapq
n=int(input())
l=list()
name=list()
for _ in range(n):
    s=input().split()
    if s[0]=='-1':
        if len(l)==0:
            print(-1)
        else:
            print(l[0][1],end=' ')
            print(name[l[0][2]])
            heapq.heappop(l)
            del name[l[0][2]]
    else:
        c=int(s[0])
        name.append(s[1])
        heapq.heappush(l,(int(s[0]),int(len(l)),int(len(name)-1)))