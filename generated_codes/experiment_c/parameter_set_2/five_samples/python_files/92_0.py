'''


'''

# Write your code here

def min_candies(n, m, k, a):
    a.sort()
    min_candies = 0
    for i in range(m):
        min_candies += a[i]
    if min_candies % k == 0:
        return min_candies
    else:
        return -1

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(min_candies(n, m, k, a))