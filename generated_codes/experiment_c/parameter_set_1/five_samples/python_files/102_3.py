"""
 = 1, 2, 3.

Note: The example input is not a valid test case.



"""

t=int(input())
for _ in range(t):
    k=int(input())
    count=0
    for _ in range(k):
        x=input().split()
        if x[0]=='<':
            if x[1]=='1':
                if x[2]=='Yes':
                    count+=1
            elif x[1]=='2':
                if x[2]=='No':
                    count+=1
        if x[0]=='>':
            if x[1]=='1':
                if x[2]=='Yes':
                    count+=1
            elif x[1]=='2':
                if x[2]=='Yes':
                    count+=1
        if x[0]=='=':
            if x[2]=='No':
                count+=1
    print(count)