'''

'''

#code

def lexicographical(s,k):
    l=[]
    for i in range(len(s)):
        l.append(s[i])
    l.sort()
    return ''.join(l[:k])

t=int(input())
for i in range(t):
    s=input()
    k=int(input())
    print(lexicographical(s,k))