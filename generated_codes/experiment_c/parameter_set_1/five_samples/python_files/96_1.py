'''

Solution:

n = int(input())
choc = []; cara = []
for i in range(n):
    a,b = map(int, input().split())
    choc.append(a)
    cara.append(b)
ch, ca = map(int, input().split())

choc.sort(); cara.sort()

dch = [0] * n; dca = [0] * n
for i in range(n-1):
    dch[i] = choc[i+1] - choc[i]
    dca[i] = cara[i+1] - cara[i]

flag = 0
for i in range(n-1):
    if((i+1)%ch == 0 and (i+1)%ca == 0):
        flag = 1
        break

if(flag == 0):
    print(-1)
else:
    for i in range(n-1):
        if(dch[i]%ch == 0 and dca[i]%ca == 0):
            print(i+1)
            break

'''

import math
for i in range(int(input())):
    n = int(input())
    choco = []
    cara = []
    for j in range(n):
        n1, n2 = map(int, input().split())
        choco.append(n1)
        cara.append(n2)
    ch, ca = map(int, input().split())
    choco.sort()
    cara.sort()
    c = 0
    i = 0
    while(i < n):
        if (choco[i] >= ch and cara[i] >= ca):
            print(c)
            break
        else:
            choco[i + 1] += choco[i]
            cara[i + 1] += cara[i]
            c += 1
            i += 1
    if(i >= n):
        print(-1)