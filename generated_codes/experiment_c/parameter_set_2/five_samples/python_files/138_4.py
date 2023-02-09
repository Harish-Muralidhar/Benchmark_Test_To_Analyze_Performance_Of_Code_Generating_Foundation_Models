'''


'''

def broken_telephone(arr):
    count = 0
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            count += 1
    return count

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(broken_telephone(arr))