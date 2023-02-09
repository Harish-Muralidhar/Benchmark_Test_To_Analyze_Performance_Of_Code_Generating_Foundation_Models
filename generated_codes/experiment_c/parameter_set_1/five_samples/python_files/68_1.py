'''

'''

import sys

def subsets(lis):
    res = []
    if len(lis) == 0:
        res.append([])
        return res
    else:
        res += subsets(lis[1:])
        temp = []
        for x in res:
            temp.append([lis[0]] + x)
        res += temp
    return res

#input.txt is used for redirection of the input
input = open('input.txt', 'r')
#sys.stdin = input
#output.txt is used for redirection of the input
output = open('output.txt', 'w')
#sys.stdout = output

T = int(input.readline())
for i in range(T):
    N, Q = map(int, input.readline().split())
    lis = list(map(int, input.readline().split()))
    for j in range(Q):
        M = int(input.readline())
        sum_lis = subsets(lis)
        count = 0
        for k in sum_lis:
            if abs(sum(k)) % M == 0:
                count += 1
        output.write(str(count) + '\n')
        print(count)