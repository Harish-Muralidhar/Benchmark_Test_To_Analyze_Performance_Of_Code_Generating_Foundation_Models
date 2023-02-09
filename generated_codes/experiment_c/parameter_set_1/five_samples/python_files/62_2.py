"""

Explanation
The sequence of the queries is:

0 2 5: The minimum in the range [2, 5] is 2.
1 1 5 6: The array becomes [1, 6, 2, 3, 4].
0 2 2: The minimum in the range [2, 2] is 2.
1 2 5 3: The array becomes [1, 6, 2, 3, 4].
0 1 3: The minimum in the range [1, 3] is 1, since the array has all numbers equal to 1.
"""

def min_query(arr,a,b):
    mini=arr[a]
    for i in range(a,b+1):
        if mini>arr[i]:
            mini=arr[i]
    return mini

def and_query(arr,a,b,c):
    for i in range(a,b+1):
        arr[i]=arr[i]&c
    return arr


n,q=map(int,input().split())
arr=list(map(int,input().split()))
query=[]
for i in range(q):
    query.append(list(map(int,input().split())))

for i in range(q):
    if query[i][0]==0:
        print(min_query(arr,query[i][1],query[i][2]))
    elif query[i][0]==1:
        arr=and_query(arr,query[i][1],query[i][2],query[i][3])