"""

Test case generation
You can use this tool to generate test cases

"""




def solve(n, m):
    return (n+1)*(m+1)

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))