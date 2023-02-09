'''

Test 2 :  Chef will make 2 moves: pick up both the elements in the first two positions (that is, 4 and 2), remove the larger one (4), incurring a cost equal to the smaller one (2). Then pick up the last two elements (2 and 5), remove 2 (the larger one), incurring a cost equal to 2. The total cost incurred will be equal to 4.

'''

def min_cost_operations(a):

    cost = 0

    while len(a) > 1:
        a.sort()
        cost += a[0]
        a.pop(0)
        a.pop(0)

    return cost

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N = int(input())
        a = list(map(int, input().split()))
        print(min_cost_operations(a))