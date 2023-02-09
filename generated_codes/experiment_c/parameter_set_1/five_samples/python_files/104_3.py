"""
"""

"""

t=int(input())
for i in range(t):
    s=input()
    l=len(s)
    if l<=2:
        print("-1")
    else:
        if s[0]==s[l-1]:
            print("-1")
        else:
            print(s[0])
"""

t=int(input())
for i in range(t):
    s=input()
    l=len(s)
    if l<=2:
        print("-1")
    else:
        if (s[0]==s[l-1]) | (s[0]==s[l-2]):
            print("-1")
        else:
            print(s[0])