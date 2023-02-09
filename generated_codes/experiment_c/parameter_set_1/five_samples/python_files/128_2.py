'''

Solution:

T = int(input())
while T != 0:
    K = int(input())
    a = list(map(str, input()))
    a.sort()
    print("".join(map(str, a[:K])))
    T -= 1
'''