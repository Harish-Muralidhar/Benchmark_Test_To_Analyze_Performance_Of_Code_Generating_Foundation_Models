'''
≡nn:

100, 100.
2, 3, 4.
1, 2, 1, 1, 1, 1.





'''

from itertools import accumulate, chain

def calc(op, n, hint, hint_value):
    if hint_value:
        return n == hint if op == '=' else n > hint if op == '>' else n < hint
    return not (n == hint if op == '=' else n > hint if op == '>' else n < hint)

def total_lies(hints, hint_values):
    n = len(hints)
    pre_calc = [[[False] * (n + 1) for _ in range(10 ** 9 + 1)] for _ in range(n + 1)]
    for i in range(n):
        pre_calc[i][0][0] = True

    for i in range(1, n + 1):
        op, hint = hints[i - 1]
        t = list(accumulate([int(calc(op, j, hint, hint_values[i - 1])) for j in range(10 ** 9 + 1)]))
        for j in range(10 ** 9 + 1):
            for k in range(n + 1):
                pre_calc[i][j][k] = pre_calc[i - 1][j][k] or pre_calc[i - 1][j - 1][k - 1] or pre_calc[i - 1][j][k - 1] or pre_calc[i - 1][j - 1][k] or pre_calc[i - 1][j][k]

    return sum(pre_calc[n][j][i] for i in range(n + 1) for j in range(10 ** 9 + 1)) - 1

def main():
    t = int(input())
    ans = []
    for i in range(t):
        n = int(input())
        hints = []
        hint_values = []
        for _ in range(n):
            s = input().split()
            hints.append((s[0], int(s[1])))
            hint_values.append(s[2] == 'Yes')
        ans.append(total_lies(hints, hint_values))
    print(*ans, sep='\n')

if __name__ == "__main__":
    main()