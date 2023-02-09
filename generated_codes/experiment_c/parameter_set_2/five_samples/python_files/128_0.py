'''
'''

#code
t=int(input())
for _ in range(t):
    s=input()
    k=int(input())
    l=[]
    for i in range(len(s)):
        l.append(s[i])
    l.sort()
    print(''.join(l[:k]))