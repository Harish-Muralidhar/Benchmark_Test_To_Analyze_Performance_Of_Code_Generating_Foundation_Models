'''

Test 2 :  Chef will make only 1 move: pick up both the elements (that is, 4 and 2), remove the larger one (4), incurring a cost equal to the smaller one (2).
'''

import heapq

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    heapq.heapify(arr)
    cost = 0
    while len(arr) > 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        cost += min(a, b)
        heapq.heappush(arr, max(a, b))
    print(cost)