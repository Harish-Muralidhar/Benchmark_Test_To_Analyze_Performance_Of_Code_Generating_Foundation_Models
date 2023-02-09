'''

Test 2 : Chef will make 2 moves: pick up both the elements (that is, 4 and 2), remove the larger one (4), incurring a cost equal to the smaller one (2); pick up the last two elements (that is, 2 and 5), remove the larger one (5), incurring a cost equal to the smaller one (2).

'''

def min_cost(arr, n):
    arr.sort()
    return sum(arr[:n-1])

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(min_cost(arr, n))