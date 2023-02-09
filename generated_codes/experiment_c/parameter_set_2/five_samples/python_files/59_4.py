'''


'''



# Write your code here
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def solve(N,arr):
    ans = 1
    for i in range(N):
        ans = ans * (nCr(arr[i],arr[i]) + nCr(arr[i],arr[i]-1))
    return ans%1000000009

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    print(solve(N,arr))