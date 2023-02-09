'''

Explanation
In the first example, there are only 3 sub rectangles which contains even number of currants:

1 1
1 1

1 1
0 1

1 1
1 0

In the second example, there are 26 sub rectangles which contains even number of currants:

1 0 1 0
0 1 0 1
1 1 1 0

0 0 1 1
1 1 0 0
0 1 1 1

1 0 1 0
0 1 0 1
0 0 1 1

1 0 0 0
0 1 1 1
1 1 0 0

1 1 0 0
0 1 1 1
0 0 0 0

1 1 0 0
0 1 1 1
0 0 1 0

1 1 0 0
0 1 1 1
0 0 1 1

1 1 0 0
0 1 1 1
0 0 0 1

0 0 1 1
1 1 0 0
0 1 1 1

0 1 0 0
1 1 1 1
0 0 1 0

0 1 0 0
1 1 1 1
0 1 0 0

0 0 1 1
1 1 0 0
1 0 1 1

0 0 1 1
1 1 0 0
1 1 1 0

0 0 1 1
1 1 0 0
1 1 1 1

0 0 1 1
1 1 0 0
0 0 1 1

0 0 0 0
1 1 1 1
1 1 1 0

0 1 0 0
1 1 1 1
0 0 0 1

0 1 0 0
1 1 1 1
0 1 1 0

0 1 0 0
1 1 1 1
1 0 0 0

0 1 0 0
1 1 1 1
0 0 1 0

0 1 0 0
1 1 1 1
0 0 1 1

0 1 0 0
1 1 1 1
0 0 0 1

0 1 0 0
1 1 1 1
0 1 1 1

0 1 1 1
1 1 1 1
0 0 0 0

0 1 1 1
1 1 1 1
0 1 0 0
'''

N,M=map(int, input().split())
a= list(map(int, list(input())))

count = 0

for i in range(N):
    for j in range(M):
        if i-j%2==0:
            count+=1


def countSubRectEven(a,n,m):
    count = 0
    for i in range(n):
        for j in range(m):
            count += a[i][j]
    return count * (count - 1) // 2

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = []
        for i in range(n):
            a.append(list(map(int, input())))
        print(countSubRectEven(a, n, m))

if __name__ == "__main__":
    main()