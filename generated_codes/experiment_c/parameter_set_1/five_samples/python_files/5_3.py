"""


"""

import sys

T=int(input())
for _ in range(T):
    N=int(input())
    a=input()
    F=int(input())
    b=input()
    a=a.split()
    b=b.split()
    flag=0
    for i in range(N-F+1):
        if(a[i]==b[0]):
            flag=1
            for j in range(i+1,i+F):
                if(b[j-i]!=a[j]):
                    flag=0
            if flag:
                print("Yes")
                break
    if not flag:
        print("No")