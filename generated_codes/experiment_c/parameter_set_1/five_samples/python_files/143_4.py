'''

'''

import sys

def output(arr):
    if arr == 0:
        print "NO"
    else:
        output = ""
        for i in range(len(arr)):
            output += arr[i]
        print output

def compute_solution(K, S):
    if len(S) == 1:
        new_arr = ['0']
        return new_arr
    for i in range(len(S)):
        if S[i] == '?':
            S[i] = '0'
    for i in range(len(S)):
        if S[i] == S[(i + 1) % len(S)]:
            return 0
    new_arr = S
    for i in range(len(S)):
        if S[i] == '?':
            for j in range(K):
                if j == int(S[(i+1) % len(S)]) or j == int(S[(i-1) % len(S)]):
                    continue
                else:
                    S[i] = str(j)
                    if S < new_arr:
                        new_arr = S
    return new_arr

f = open(sys.argv[1], 'r')
T = int(f.readline())
for i in range(T):
    K = int(f.readline())
    S = map(str, list(f.readline()))
    output(compute_solution(K, S))