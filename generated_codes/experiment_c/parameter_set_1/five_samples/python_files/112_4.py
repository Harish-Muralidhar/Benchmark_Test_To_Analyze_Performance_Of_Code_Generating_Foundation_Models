'''

'''

def CountPairs(a, n):
    pairs = 0
    for i in range(n):
        for j in range(i+1,n):
            if(a[i]<a[j]):
                pairs += 1
    return pairs

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(CountPairs(a, n))