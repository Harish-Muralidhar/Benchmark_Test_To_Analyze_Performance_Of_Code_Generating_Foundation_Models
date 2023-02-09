'''

Constraint
Time limit: 15 seconds
Memory limit: 1GB

'''
# Use of Counter

from collections import Counter

def get_zeroes(num):
    count = 0
    for i in range(1,num):
        count += i*Counter(str(i))['0']
    return count

T = int(input())
for _ in range(T):
    num = int(input())
    print(get_zeroes(num))