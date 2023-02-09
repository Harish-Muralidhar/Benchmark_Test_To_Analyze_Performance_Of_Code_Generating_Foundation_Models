'''
'''
def foo(arr,sum):
    if sum == 0:
        return True
    if len(arr) == 0 and sum != 0:
        return False
    if arr[-1] > sum:
        return foo(arr[:-1], sum)
    else:
        return foo(arr[:-1], sum) or foo(arr[:-1], sum-arr[-1])
    
for _ in range(int(input())):
    n,x = map(int, input().split())
    arr = list(map(int, input().split()))
    sum = 0
    for i in arr:
        sum += i
    if sum % x == 0:
        temp = sum//x
        if foo(arr,sum-temp*x):
            print(temp)
        else:
            print(-1)
    else:
        print(-1)