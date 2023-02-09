'''

Explanation
In the first example, the number of sub-rectangles containing even number of currants are:

1. The entire rectangle.
2. The entire first row.
3. The entire second column.

In the second example, the number of sub-rectangles containing even number of currants are:

1. The entire rectangle.
2. The entire first row.
3. The entire second row.
4. The entire third row.
5. The entire first column.
6. The entire second column.
7. The entire third column.
8. The entire fourth column.
9. The rectangle (1,1) to (2,2).
10. The rectangle (1,2) to (2,3).
11. The rectangle (1,3) to (2,4).
12. The rectangle (2,1) to (3,2).
13. The rectangle (2,2) to (3,3).
14. The rectangle (2,3) to (3,4).
15. The rectangle (3,1) to (3,2).
16. The rectangle (3,2) to (3,3).
17. The rectangle (3,3) to (3,4).
18. The rectangle (1,1) to (3,2).
19. The rectangle (1,2) to (3,3).
20. The rectangle (1,3) to (3,4).
21. The rectangle (1,1) to (2,3).
22. The rectangle (2,1) to (3,3).
23. The rectangle (1,2) to (3,4).
24. The rectangle (1,1) to (3,3).
25. The rectangle (1,2) to (2,4).
26. The rectangle (2,1) to (3,4).

'''

n,m = map(int,input().split())

l = []
for i in range(n):
    l.append(list(input()))

def count(l,n,m):
    c = 0
    for i in range(n):
        for j in range(m):