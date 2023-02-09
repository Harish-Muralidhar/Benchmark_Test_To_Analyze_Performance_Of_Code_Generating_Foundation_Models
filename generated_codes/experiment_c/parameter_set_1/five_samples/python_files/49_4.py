"""

Test 2 : Chef will pick up all the elements and remove the greatest one (5), incurring a cost equal to the smallest one (2). Then, he will remove the remaining two (4 and 2), incurring a cost equal to the smaller one (2). The total cost would be 2+2=4.

"""

for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))

    l.sort()
    count = 0
    while len(l) != 1:
        count += l.pop(0)
        l[0] -= l.pop(0)
    print(count)