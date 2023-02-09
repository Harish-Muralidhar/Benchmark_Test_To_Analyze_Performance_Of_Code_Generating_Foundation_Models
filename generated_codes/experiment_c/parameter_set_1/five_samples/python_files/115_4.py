'''

'''
import math
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    count = 0
    while max(l) != min(l):
        l = list(map(lambda x: x-1 if x == max(l) else x,l))
        count += 1
    print(count)