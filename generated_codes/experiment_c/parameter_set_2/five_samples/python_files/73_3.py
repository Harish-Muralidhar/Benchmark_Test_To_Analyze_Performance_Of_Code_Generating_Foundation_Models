'''

Explanation
Example case 1: Joe can play the beats (2, 5, 8, 11) while Chef can play the beats (4, 8, 16).
Example case 2: Joe can play the beats (2, 3, 4, 5) while Chef can play the beats (2, 4).
Example case 3: Joe can play the beats (2, 3, 9, 10, 19, 27, 28) while Chef can play the beats (3, 8, 11).
Example case 4: Joe can play the beats (2, 4, 7, 10, 13, 25) while Chef can play the beats (1, 4).
'''

def arigeom(arr):
    n = len(arr)
    a = []
    b = []
    for i in range(n-1):
        diff = arr[i+1] - arr[i]
        if diff == arr[i] - arr[i-1]:
            a.append(arr[i])
        else:
            b.append(arr[i])
    a.append(arr[-1])
    b.append(arr[-1])
    return a,b

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    a,b = arigeom(arr)
    print(*a)
    print(*b)