'''

Explanation
Test case 1. No cell is a CPC.
Test case 2.
The first cell of the second row is a CPC with p=5. It can accommodate 5 monsters.
The first cell of the fourth row is a CPC with p=3. It can accommodate 3 monsters.
The first cell of the sixth row is a CPC with p=5. It can accommodate 5 monsters.
Hence, the answer is 3.

'''
# Write your code here
T=int(input())
for i in range(T):
    r,c=map(int,input().split())
    ll=[]
    for j in range(r):
        s=input()
        ll.append(s)
    count=0
    for k in range(1,r-1):
        for l in range(1,c-1):
            if ll[k][l]=='^':
                l1,r1,t1,b1=0,0,0,0
                for t in range(l,c):
                    if ll[k][t]=='^':
                        l1+=1
                    else:
                        break
                for t in range(l,0,-1):
                    if ll[k][t]=='^':
                        r1+=1
                    else:
                        break
                for t in range(k,r):
                    if ll[t][l]=='^':
                        t1+=1
                    else:
                        break
                for t in range(k,0,-1):
                    if ll[t][l]=='^':
                        b1+=1
                    else:
                        break
                m=min(l1,r1,t1,b1)
                c=0
                for p in range(2,m+1):
                    flag=0
                    for d in range(2,p):
                        if p%d==0:
                            flag=1
                            break
                    if flag==0:
                        c+=1
                count+=c
    print(count)
    

'''
# Write your code here
T=int(input())
for i in range(T):
    r,c=map(int,input().split())
    ll=[]
    for j in range(r):
        s=input()
        ll.append(s)
    count=0
    for k in range(1,r-1):
        for l in range(1,c-1):
            if ll[k][l]=='^':
                l1,r1,t1,b1=0,0,0,0
                for t in range(l,c):
                    if ll[k][t]=='^':
                        l1+=1
                    else:
                        break
                for t in range(l,0,-1):
                    if ll[k][t]=='^':
                        r1+=1
                    else:
                        break
                for t in range(k,r):
                    if ll[t][l]=='^':
                        t1+=1
                    else:
                        break
                for t in range(k,0,-1):
                    if ll[t][l]=='^':
                        b1+=1
                    else:
                        break
                m=min(l1,r1,t1,b1)
                for p in range(2,m+1):
                    flag=0
                    for d in range(2,p):
                        if p%d==0:
                            flag=1
                            break
                    if flag==0:
                        count+=1
    print(count)
'''