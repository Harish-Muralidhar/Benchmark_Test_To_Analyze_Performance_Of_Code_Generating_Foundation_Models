"""

Test 2 : Chef will make only 1 move: pick up both the elements (that is, 4 and 2), remove the larger one (4), incurring a cost equal to the smaller one (2).

"""

def min_cost(arr):
    cost = 0
    while len(arr) > 1:
        arr.sort()
        cost += arr[0]
        arr.pop(0)
        arr.pop(0)
    return cost

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(min_cost(arr))