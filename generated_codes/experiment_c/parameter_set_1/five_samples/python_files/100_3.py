"""


"""
import sys

def check_sum(arr, num):
    # Base case
    if num == 0:
        return True
    if len(arr) == 0:
        return False

    #print "arr = ", arr, "num = ", num
    #print "arr[-1] = ", arr[-1]
    if arr[-1] == num:
        return True
    #print "arr[:-1] = ", arr[:-1], "num = ", num
    ans1 = check_sum(arr[:-1], num)

    #print "arr[:-1] = ", arr[:-1], "num = ", num - arr[-1]
    ans2 = check_sum(arr[:-1], num - arr[-1])
    #print "ans1=", ans1, " ans2=", ans2
    return ans1 or ans2


def check_sum_iter(arr, num):
    # Base case
    if num == 0:
        return True
    if len(arr) == 0:
        return False

    a = [False] * (num + 1)

    a[0] = True
    for c in arr:
        j = num - c
        while j >= 0:
            if a[j]:
                a[j+c] = True
            j -= 1

    return a[-1]


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        sys.stdin.readline().strip()
        arr = map(int, sys.stdin.readline().strip().split())
        num = int(sys.stdin.readline().strip())
        ans = check_sum(arr, num)
        if ans:
            print "Yes"
        else:
            print "No"