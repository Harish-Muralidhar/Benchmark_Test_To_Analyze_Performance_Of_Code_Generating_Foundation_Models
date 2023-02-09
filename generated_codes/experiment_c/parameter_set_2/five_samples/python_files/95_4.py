'''

Explanation
Example 1:

There are 3 sub-rectangles which contains even number of currants.

Example 2:

There are 26 sub-rectangles which contains even number of currants.

'''

def count_subrectangles(cake):
    m = len(cake)
    n = len(cake[0])
    count = 0
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    if sum(cake[i][j:l+1]) % 2 == 0:
                        count += 1
    return count

def main():
    m, n = map(int, input().split())
    cake = []
    for i in range(m):
        cake.append(list(map(int, input())))
    print(count_subrectangles(cake))

if __name__ == '__main__':
    main()