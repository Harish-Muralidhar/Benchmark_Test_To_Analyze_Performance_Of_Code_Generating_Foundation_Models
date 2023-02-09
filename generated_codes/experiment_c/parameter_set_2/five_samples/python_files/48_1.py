'''

Explanation:

In the first example, there are n=3 dolls which have types as given in the input. As there is odd number of dolls, one doll must be missing. As there are 2 dolls of type 1 and 1 doll of type 2, type 2 must be the one missing.

In the second example, there are n=5 dolls which have types as given in the input. As there is odd number of dolls, one doll must be missing. As there are 2 dolls of type 1, 2 dolls of type 2 and 1 doll of type 3, type 3 must be the one missing.

'''

def missing_doll(arr):
    n = len(arr)
    for i in range(n):
        if arr.count(arr[i])%2!=0:
            return arr[i]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(missing_doll(arr))