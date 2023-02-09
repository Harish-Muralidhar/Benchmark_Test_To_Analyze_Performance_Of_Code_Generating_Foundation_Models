'''
Sum 0 is present in first and second index, 1 is present in second and third index, 2 is present in fourth index.

'''

n = int(input())
for _ in range(n):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = []
    for i in a:
        if i not in b:
            b.append(i)
        else:
            b.append(i)
            b.append(i)
    print(*b)