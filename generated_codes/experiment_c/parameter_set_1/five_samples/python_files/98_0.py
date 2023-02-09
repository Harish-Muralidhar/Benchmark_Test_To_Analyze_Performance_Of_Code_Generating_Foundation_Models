'''
 

In this case Asuna places the volcano at (1, 1).
 

Kirito's turn, he places volcano at (5, 1), kills the monster. Asuna can't place the volcano at any other position. Hence, Kirito wins.
You can see that in all the 3 cases Asuna has to be the first to move.
'''

#Solution
for i in range(int(input())):
    r,c = map(int,input().split())
    m = []
    for j in range(r):
        m.append(list(input()))

    if r==1:
        if "#" in m[0]:
            print("Kirito")
        else:
            print("Asuna")
    elif c==1:
        f = 1
        for j in range(r):
            if m[j][0] != "#":
                f = 0
                break
        if f:
            print("Kirito")
        else:
            print("Asuna")
    else:
        for j in range(r):
            for k in range(c):
                if m[j][k]=="^":
                    m[j][k] = 0
                else:
                    m[j][k] = 1
        for j in range(1,r-1):
            for k in range(1,c-1):
                if m[j][k] == 0:
                    l,r,t,b = 0,0,0,0
                    for a in range(k-1,-1,-1):
                        if m[j][a] == 0:
                            l += 1
                        else:
                            break
                    for a in range(k+1,c):
                        if m[j][a] == 0:
                            r += 1
                        else:
                            break
                    for a in range(j-1,-1,-1):
                        if m[a][k] == 0:
                            t += 1
                        else:
                            break
                    for a in range(j+1,r):
                        if m[a][k] == 0:
                            b += 1
                        else:
                            break
                    a = min(l,r,t,b)
                    p = 2
                    while(p<=a):
                        if a%p == 0:
                            m[j][k] = 2
                            break
                        p += 1
        cnt = 0
        for j in range(r):
            for k in range(c):
                if m[j][k] == 2:
                    cnt += 1
        if cnt%2 == 1:
            print("Asuna")
        else:
            print("Kirito")