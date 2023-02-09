"""
For second query, 2 is connected to 3 by an edge. Distance 1.
For third query, 4 is connected to 3 by an edge. Distance 1.

NOTE: Your code should be able to convert the sample input into the sample output. However, this is not enough to pass the challenge, because the code will be run on multiple test cases. Therefore, your code must solve this problem statement.

"""
# Write your code here


def lca(u, v):
    while (u > v):
        u = u // 2
    while (u < v):
        v = v // 2
    return u


def distance(u, v):
    return depth(u) + depth(v) - 2 * depth(lca(u, v))


def depth(u):
    d = 0
    while (u > 1):
        u = u // 2
        d += 1
    return d


def main():
    n = int(input())
    for _ in range(n):
        u, v = input().split()
        u, v = int(u), int(v)
        print(distance(u, v))


if __name__ == "__main__":
    main()