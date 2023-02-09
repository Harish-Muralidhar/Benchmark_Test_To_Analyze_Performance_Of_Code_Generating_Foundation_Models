"""

Question Link: https://www.codechef.com/LRNDSA01/problems/ZCO14003
"""

for i in range(int(input())):
    n, m = map(int, input().split())
    l = []
    for j in range(n):
        l.append(list(map(int, input().split())))
    if n == 1:
        if m == 1:
            print(l[0][0])
            continue
        else:
            if l[0][0] == l[0][m - 1]:
                print(sum(l[0]))
                continue
            elif l[0][0] > l[0][m - 1]:
                print(l[0][0] + sum(l[0][1:m - 1]))
                continue
            else:
                print(l[0][m - 1] + sum(l[0][1:m - 1]))
                continue
    elif m == 1:
        if l[0][0] == l[n - 1][0]:
            print(sum([i[0] for i in l]))
            continue
        elif l[0][0] > l[n - 1][0]:
            print(l[0][0] + sum([i[0] for i in l[1:n - 1]]))
            continue
        else:
            print(l[n - 1][0] + sum([i[0] for i in l[1:n - 1]]))
            continue
    else:
        if l[0][0] == l[0][m - 1] == l[n - 1][0] == l[n - 1][m - 1]:
            print(sum([i[0] for i in l]) + sum([i[m - 1] for i in l]))
            continue
        else:
            if l[0][0] == l[0][m - 1] or l[n - 1][0] == l[n - 1][m - 1]:
                print(max([sum([i[0] for i in l]), sum([i[m - 1] for i in l])]))
                continue
            else:
                if l[0][0] > l[0][m - 1] and l[n - 1][0] > l[n - 1][m - 1]:
                    print(l[0][0] + l[n - 1][0] + sum([i[0] for i in l[1:n - 1]]) + sum([i[m - 1] for i in l[1:n - 1]]))
                    continue
                elif l[0][0] < l[0][m - 1] and l[n - 1][0] < l[n - 1][m - 1]:
                    print(l[0][m - 1] + l[n - 1][m - 1] + sum([i[0] for i in l[1:n - 1]]) + sum([i[m - 1] for i in l[1:n - 1]]))
                    continue
                else:
                    if l[0][0] > l[0][m - 1]:
                        if l[n - 1][0] > l[n - 1][m - 1]:
                            print(l[0][0] + l[n - 1][0] + sum([i[0] for i in l[1:n - 1]]) + sum([i[m - 1] for i in l[1:n - 1]]))
                            continue
                        else:
                            print(l[0][0] + l[n - 1][m - 1] + sum([i[0] for i in l[1:n - 1]]) + sum([i[m - 1] for i in l[1:n - 1]]))
                            continue
                    else:
                        if l[n - 1][0] > l[n - 1][m - 1]:
                            print(l[0][m - 1] + l[n - 1][0] + sum([i[0] for i in l[1:n - 1]]) + sum([i[m - 1] for i in l[1:n - 1]]))
                            continue
                        else:
                            print(l[0][m - 1] + l[n - 1][m - 1] + sum([i[0] for i in l[1:n - 1]]) + sum([i[m - 1] for i in l[1:n - 1]]))
                            continue