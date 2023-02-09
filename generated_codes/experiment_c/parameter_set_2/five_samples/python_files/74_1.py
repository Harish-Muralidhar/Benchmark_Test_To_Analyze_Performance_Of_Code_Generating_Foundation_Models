"""

Explanation

In the first test case the longest progression is (2, 4, 6). In the second test case the total number of such progressions is less than 2. In the third test case the longest progression is (5, 9, 13, 17). The 12th such progression in lexicographical order is (5, 14).

"""

import math

def main():
    t = int(input())
    for _ in range(t):
        l, r, k, n = map(int, input().split())
        if k > r - l:
            print(0, 0)
        else:
            length = math.floor((r - l) / k) + 1
            if n <= length:
                print(length, l, l + k)
            else:
                print(length, 0, 0)

if __name__ == "__main__":
    main()