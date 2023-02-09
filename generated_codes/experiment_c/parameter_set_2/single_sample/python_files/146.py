'''


'''



def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))


def solve(arr):
    arr.sort()
    ans = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            ans += 1
    return ans


main()