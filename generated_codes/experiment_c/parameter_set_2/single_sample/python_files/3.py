'''


'''

import sys

def F(S):
    balance = 0
    max_balance = 0
    for index in range(len(S)):
        if S[index] == '(':
            balance += 1
        if S[index] == ')':
            balance -= 1
        max_balance = max(max_balance, balance)
    return max_balance

def solve(A):
    if F(A) == 0:
        return A
    else:
        balance = 0
        for index in range(len(A)):
            if A[index] == '(':
                balance += 1
            if A[index] == ')':
                balance -= 1
            if balance == 0:
                return solve(A[1:index]) + solve(A[index+1:])

if __name__ == "__main__":
    # For fast I/O
    #sys.stdin = open("input.txt", "r")
    #sys.stdout = open("output.txt", "w")

    # Read each test case
    t = int(input())
    for _ in range(t):
        A = input()
        print(solve(A))