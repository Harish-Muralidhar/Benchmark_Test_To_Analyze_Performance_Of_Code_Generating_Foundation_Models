"""
So you should print BWBW.

"""

t = int(input())
for i in range(t):
    x = input()
    y = input()
    li = list()
    a = 0
    b = 0
    s = ""
    for j in range(len(x)):
        if x[j] == 'B' and y[j] == 'B':
            li.append('B')
        elif x[j] == 'W' and y[j] == 'W':
            li.append('W')
        elif x[j] == 'W' and y[j] == 'B':
            a += 1
            li.append('B')
        elif x[j] == 'B' and y[j] == 'W':
            b += 1
            li.append('W')
    # print("a :", a, "b :", b)
    for j in range(len(x)):
        if a > b:
            s += "B"
            a -= 1
            li.pop(0)
        elif a < b:
            s += "W"
            b -= 1
            li.pop(-1)
        else:
            if li[0] == 'B':
                s += "B"
                a -= 1
                li.pop(0)
            else:
                s += "W"
                b -= 1
                li.pop(-1)
    print(s)