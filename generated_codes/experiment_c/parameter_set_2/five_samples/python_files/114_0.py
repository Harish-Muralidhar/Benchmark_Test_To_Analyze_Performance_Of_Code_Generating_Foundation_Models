'''

'''


import sys

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        k = int(input())
        min_cost = 0
        arr.sort()
        for i in range(n):
            if i+k+1 < n:
                min_cost += arr[i]
            else:
                min_cost += min(arr[i], arr[i+k+1])
        print(min_cost)

if __name__ == '__main__':
    main()