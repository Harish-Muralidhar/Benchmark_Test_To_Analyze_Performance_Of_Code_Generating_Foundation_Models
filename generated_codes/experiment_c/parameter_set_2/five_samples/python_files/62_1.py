"""

Explanation
For the first query, the answer is 2 because the minimum element in the range 2, 3, 4, 5 is 2.
For the second query, the array becomes [1, 6, 2, 6, 4].
For the third query, the answer is 0 because the minimum element in the range 2, 2 is 0.
For the fourth query, the array becomes [1, 6, 2, 2, 4].
For the fifth query, the answer is 0 because the minimum element in the range 1, 2, 3 is 0.

"""

# Write your code here
N,Q = map(int,input().split())

arr = list(map(int,input().split()))

for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 0:
        print(min(arr[query[1]-1:query[2]]))
    else:
        for i in range(query[1]-1,query[2]):
            arr[i] = arr[i] & query[3]