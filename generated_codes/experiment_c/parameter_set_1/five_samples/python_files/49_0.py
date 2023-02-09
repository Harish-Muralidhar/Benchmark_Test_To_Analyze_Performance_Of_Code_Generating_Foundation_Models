"""


Test 2 : Chef will make two moves:

pick up both the first two elements (that is, 4 and 2), remove the larger one (4), incurring a cost equal to the smaller one (2).
pick up the last two elements (that is, the remaining 2 and 5), remove the larger one (5), incurring a cost equal to the smaller one (2).

The total cost incurred will be equal to 2 + 2 = 4.
"""
from heapq import heappush, heappop
t= int(input())
for _ in range(t):
    n= int(input())
    arr= list(map(int, input().split()))
    heap= []
    for i in arr:
        heappush(heap, i)
    ans= 0
    while len(heap)>1:
        a= heappop(heap)
        b= heappop(heap)
        ans+= (a+b)
        heappush(heap, a+b)
    print(ans)