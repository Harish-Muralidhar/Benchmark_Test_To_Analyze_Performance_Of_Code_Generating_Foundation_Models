'''


'''

def divisible_by_k(n,k):
    count = 0
    for i in range(n):
        if int(input()) % k == 0:
            count += 1
    return count

n,k = map(int,input().split())
print(divisible_by_k(n,k))