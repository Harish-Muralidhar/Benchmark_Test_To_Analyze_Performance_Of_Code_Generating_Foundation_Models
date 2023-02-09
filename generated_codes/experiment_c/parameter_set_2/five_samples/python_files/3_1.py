'''


'''

# Write your code here

import sys

def F(S):
    balance = 0
    max_balance = 0
    for index in range(len(S)):
        if S[index] == '(':
            balance += 1
        elif S[index] == ')':
            balance -= 1
        max_balance = max(max_balance, balance)
    return max_balance

def solve(S):
    N = len(S)
    if N == 0:
        return ''
    if S[0] == ')':
        return '(' + solve(S[1:])
    if S[-1] == '(':
        return solve(S[:-1]) + ')'
    if F(S) == 0:
        return S
    if F(S) == 1:
        return '(' + solve(S[1:-1]) + ')'
    if F(S) == 2:
        return '(' + solve(S[1:])
    if F(S) == -1:
        return solve(S[:-1]) + ')'
    if F(S) == -2:
        return solve(S[1:]) + ')'
    return '(' + solve(S[1:])

T = int(input())
for i in range(T):
    S = input()
    print(solve(S))