"""
"""

#Solution

t = int(input())
for i in range(t):
    n = int(input())
    n = str(n)
    l = len(n)
    s = n[0]
    l = n[l-1]
    print(int(s)+int(l))