"""

Test 2 : Chef will make 2 moves: pick up the first two elements (that is, 4 and 2), remove the larger one (4), incurring a cost equal to the smaller one (2). Then, pick up the last two elements (that is, 2 and 5), remove the larger one (5), incurring a cost equal to the smaller one (2).

"""

import heapq

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    heapq.heapify(arr)
    cost = 0
    while len(arr) > 1:
        cost += heapq.heappop(arr)
        heapq.heappop(arr)
    print(cost)