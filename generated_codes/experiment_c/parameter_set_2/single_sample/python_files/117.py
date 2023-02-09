"""

Explanation
Test Case 1:

After first round, the numbering is [1, 0, 1, 2].

Test Case 2:

After first round, the numbering is [2, 1, 0, 1, 2, 3].

After second round, the numbering is [3, 2, 1, 1, 2, 3].

"""

def get_max_num(n, m, positions):
    max_num = 0
    for i in range(n):
        max_num = max(max_num, get_num(i, positions))
    return max_num

def get_num(i, positions):
    num = 0
    for pos in positions:
        if i <= pos:
            num += 1
        else:
            num -= 1
    return num

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        positions = list(map(int, input().split()))
        print(get_max_num(n, m, positions))