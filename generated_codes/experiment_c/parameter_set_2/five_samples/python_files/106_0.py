'''

'''

# Write your code here
n, q = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        for j in range(query[1]-1, query[2]):
            arr[j] += query[3]
            arr[j] %= 1000000007
    elif query[0] == 2:
        for j in range(query[1]-1, query[2]):
            arr[j] *= query[3]
            arr[j] %= 1000000007
    elif query[0] == 3:
        for j in range(query[1]-1, query[2]):
            arr[j] = query[3]
    else:
        print(sum(arr[query[1]-1:query[2]])%1000000007)