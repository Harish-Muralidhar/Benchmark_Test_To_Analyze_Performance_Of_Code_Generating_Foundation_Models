'''

'''

# Write your code here

t=int(input())
for i in range(t):
    s1=input()
    s2=input()
    l1=len(s1)
    l2=len(s2)
    if l1!=l2:
        print("0 0")
    else:
        min=0
        max=0
        for j in range(l1):
            if s1[j]=='?' or s2[j]=='?':
                max+=1
            elif s1[j]!=s2[j]:
                min+=1
                max+=1
        print(min,max)