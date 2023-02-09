'''

Test 2 :  Chef will make 2 moves: pick up the first two elements (4 and 2), remove the larger one (4), incurring a cost equal to the smaller one (2). Next, pick up the last two elements (2 and 5), remove the larger one (5), incurring a cost equal to the smaller one (2).

'''

# Write your code here

def min_cost(arr):
    cost = 0
    while len(arr) > 1:
        arr.sort()
        cost += arr[0]
        arr.pop(0)
        arr.pop(0)
    return cost

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(min_cost(arr))