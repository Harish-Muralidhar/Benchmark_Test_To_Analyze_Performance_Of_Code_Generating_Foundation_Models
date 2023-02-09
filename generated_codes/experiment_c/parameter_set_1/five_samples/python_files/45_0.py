"""
"""

T=int(input())
for i in range(T):
    string=input()
    if(len(string)==len(set(string))):
        print("NO")
    else:
        count=0
        for j in set(string):
            if(string.count(j)>=2):
                count+=1
        if(count>1):
            print("NO")
        else:
            print("YES")