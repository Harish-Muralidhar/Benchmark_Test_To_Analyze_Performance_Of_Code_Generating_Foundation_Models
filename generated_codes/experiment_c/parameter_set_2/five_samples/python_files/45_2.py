"""

Explanation
In the first case, the number of occurrences of 'a' is 2 and the sum of the number of occurrences of 'c' and 'b' is also 2.
In the second case, the number of occurrences of 'z' is 4 and the sum of the number of occurrences of 'q' and 'z' is also 4.
In the third case, the number of occurrences of 'a' is 1 and the sum of the number of occurrences of 'b' and 'c' is 1.
In the fourth case, the number of occurrences of 'k' is 2 and the sum of the number of occurrences of 'l' and 'w' is also 2.

"""

#code
t = int(input())
for i in range(t):
    s = input()
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    l = list(d.values())
    if len(l) == 1:
        print("YES")
    else:
        l.sort()
        if l[0] == l[-1]:
            print("YES")
        else:
            print("NO")