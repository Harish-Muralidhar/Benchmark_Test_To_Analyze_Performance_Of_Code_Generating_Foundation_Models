'''
 = 100, nnn = 3, and nnn = 1.

'''

#code

t = int(input())
for i in range(t):
    k = int(input())
    l = []
    for j in range(k):
        l.append(input().split(" "))
    if l[0][0] == ">":
        if l[0][2] == "Yes":
            n = int(l[0][1]) + 1
        else:
            n = int(l[0][1])
    elif l[0][0] == "<":
        if l[0][2] == "Yes":
            n = int(l[0][1]) - 1
        else:
            n = int(l[0][1])
    else:
        n = int(l[0][1])
    count = 0
    for j in range(1,k):
        if l[j][0] == ">":
            if n > int(l[j][1]):
                if l[j][2] == "No":
                    count += 1
            else:
                if l[j][2] == "Yes":
                    count += 1
        elif l[j][0] == "<":
            if n < int(l[j][1]):
                if l[j][2] == "No":
                    count += 1
            else:
                if l[j][2] == "Yes":
                    count += 1
        else:
            if n == int(l[j][1]):
                if l[j][2] == "No":
                    count += 1
            else:
                if l[j][2] == "Yes":
                    count += 1
    print(count)