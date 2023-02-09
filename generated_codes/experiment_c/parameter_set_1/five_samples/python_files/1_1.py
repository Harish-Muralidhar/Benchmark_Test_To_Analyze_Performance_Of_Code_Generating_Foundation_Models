'''

'''


def solve(n, arr):
    res = [0] * n
    curr = 1
    sign = 1 if arr[0] > 0 else -1
    for i in range(1, n):
        if sign == 1 and arr[i] < 0:
            curr += 1
            sign = -1
        elif sign == -1 and arr[i] > 0:
            curr += 1
            sign = 1
        else:
            res[i] = curr
            curr = 1
            sign = 1 if arr[i] > 0 else -1
    res[0] = curr
    return res

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split(' ')]
        res = solve(n, arr)
        print(' '.join([str(x) for x in res]))