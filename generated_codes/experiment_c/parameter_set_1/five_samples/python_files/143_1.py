'''


Note: Large Input/Output files. For this problem, you will need to download the following files:


The first file contains the input. The first line of the input file contains an integer T, the number of test cases. T test cases follow. Each test case consists of exactly two lines. The first line contains an integer K, the number of available colors for cherries. The second line contains a string S that represents the current arrangement of the cherries in the cake.
The second file contains the output. For each test case output the lexicographically smallest valid arrangement of the cherries in the cake that can be obtained from the given arrangement by replacement of each question mark by some digit from 0 to K – 1. If it is impossible to place the cherries output NO (output is case sensitive).


'''
import re

T = int(input())
for _ in range(T):
    K = int(input())
    S = input()
    L = len(S)
    if K > 10 or L > 100 or L < 1:
        print("NO")
        continue

    if L == 1:
        if S[0] == '?':
            print("0")
        else:
            print(S)
        continue

    if K == 1 and S[0] == '?' and S[-1] == '?':
        print("0", end='')
        for i in range(1, L-1):
            print("?", end='')
        print("0")
        continue

    if S[0] == '?' and S[-1] == '?':
        S = S[1:-1]

    S = S.replace('?', '.')
    p = re.compile(r'0{2,}|1{2,}|2{2,}|3{2,}|4{2,}|5{2,}|6{2,}|7{2,}|8{2,}|9{2,}')
    if p.search(S):
        print("NO")
        continue

    i = 0
    j = 1
    while j < L:
        if S[i] == S[j]:
            if S[i] == '.':
                S = S[:i] + '0' + S[i+1:]
                i = i+1
                j = j+1
                continue
            else:
                print("NO")
                break
        else:
            i = j
            j = j+1
    else:
        print(S)