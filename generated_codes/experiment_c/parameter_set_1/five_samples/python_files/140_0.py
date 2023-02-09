'''


'''

def find_way(n):
    if n == 1 or n ==2:
        return n
    if arr[n] != 0:
        return arr[n]
    else:
        arr[n] = (find_way(n-1) + find_way(n-2))
        return arr[n]

n = int(input())
arr = [0] *(n+1)
for i in range(n):
    l = int(input())
    print(find_way(l))