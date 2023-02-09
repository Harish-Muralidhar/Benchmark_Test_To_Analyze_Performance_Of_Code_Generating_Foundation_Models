"""


"""

import sys

def main():
    test_cases = int(sys.stdin.readline())
    for _ in range(test_cases):
        n, m, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        a.sort()
        if a[0] > k:
            print(-1)
            continue
        if m > n:
            print(-1)
            continue
        if m == n:
            if sum(a) % k == 0:
                print(sum(a))
            else:
                print(-1)
            continue
        if m < n:
            if sum(a[:m]) % k == 0:
                print(sum(a[:m]))
            else:
                print(-1)
            continue

if __name__ == "__main__":
    main()