"""


Solution:
"""
t=int(input())
for i in range(t):
    n=int(input())
    rem=0
    rev=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    print(rev)