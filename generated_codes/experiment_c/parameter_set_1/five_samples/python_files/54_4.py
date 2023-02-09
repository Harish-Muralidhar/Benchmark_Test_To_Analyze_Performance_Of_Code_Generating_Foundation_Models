'''

'''
import itertools

t = int(input())

for i in range(t):
    n = int(input())
    e, o = map(int, input().split())
    if e + o != (n*(n+1))/2:
        print(-1)
    elif e > n/2 and n%2 == 0:
        print(-1)
    else:
        if e == (n*(n+1))/2:
            for j in range(n):
                print(2, end=" ")
        elif o == (n*(n+1))/2:
            for j in range(n):
                print(1, end=" ")
        else:
            e2 = 0
            o2 = 0
            evens = []
            odds = []
            flag = 0
            for j in range(2,n+1):
                if j%2 == 0:
                    evens.append(j)
                else:
                    odds.append(j)
            if e%2 == 0:
                e2 = int(e/2)
                if len(evens) >= e2:
                    lst = list(itertools.combinations(evens, e2))
                    for k in range(len(lst)):
                        for m in lst[k]:
                            print(m, end=" ")
                        if n-e2 == len(odds):
                            for m in odds:
                                print(m, end=" ")
                        elif n-e2 > len(odds):
                            for m in range(len(odds)):
                                print(odds[m], end=" ")
                            for m in range(n-e2-len(odds)):
                                print(1, end=" ")
                        elif n-e2 < len(odds):
                            for m in range(n-e2):
                                print(odds[m], end=" ")
                        print()
                        flag = 1
                        break
                else:
                    print(-1)
            elif o%2 == 0:
                o2 = int(o/2)
                if len(odds) >= o2:
                    lst = list(itertools.combinations(odds, o2))
                    for k in range(len(lst)):
                        for m in lst[k]:
                            print(m, end=" ")
                        if n-o2 == len(evens):
                            for m in evens:
                                print(m, end=" ")
                        elif n-o2 > len(evens):
                            for m in range(len(evens)):
                                print(evens[m], end=" ")
                            for m in range(n-o2-len(evens)):
                                print(2, end=" ")
                        elif n-o2 < len(evens):
                            for m in range(n-o2):
                                print(evens[m], end=" ")
                        print()
                        flag = 1
                        break
                else:
                    print(-1)
            if flag == 0 and len(evens) == 0 and len(odds) == 0:
                for j in range(n):
                    print(j, end=" ")
                print()