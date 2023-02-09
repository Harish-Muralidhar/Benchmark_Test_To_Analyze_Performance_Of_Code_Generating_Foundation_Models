"""

Explanation

In the first example, there are 3 sub rectangles which contains even number of currants.

In the second example, there are 26 sub rectangles which contains even number of currants.

Solution:

"""

def even_count(n,m,cake):
    even_count = 0
    for i in range(n):
        for j in range(m):
            for k in range(i,n):
                for l in range(j,m):
                    if (k-i+1)*(l-j+1)%2 == 0:
                        even_count += 1
    return even_count

n,m = map(int,input().split())
cake = []
for i in range(n):
    cake.append(list(input()))
print(even_count(n,m,cake))