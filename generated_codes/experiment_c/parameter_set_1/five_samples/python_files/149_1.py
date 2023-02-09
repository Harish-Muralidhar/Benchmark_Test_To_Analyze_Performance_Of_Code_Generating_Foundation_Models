"""
"""


def solution(arr):
    memory = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > memory:
            memory += (arr[i] - memory)
    return memory


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()][0:n]
        print(solution(arr))