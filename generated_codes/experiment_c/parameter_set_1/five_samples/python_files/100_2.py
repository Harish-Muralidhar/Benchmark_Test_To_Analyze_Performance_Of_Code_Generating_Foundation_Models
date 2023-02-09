"""

"""
import numpy as np

def find_sum(arr,n,m):
    if n == 0:
        return False
    if sum(arr) == m:
        return True
    if sum(arr) < m:
        return False
    if sum(arr[1:]) >= m:
        return find_sum(arr[1:],n-1,m)
    else:
        return find_sum(arr[1:],n-1,m) or find_sum(arr[1:],n-1,m-arr[0])

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        n, m = map(int,input().split())
        arr = list(map(int,input().split()))
        if find_sum(arr,n,m):
            print("Yes")
        else:
            print("No")