'''


'''

def F(S):
    balance = 0
    max_balance = 0
    for i in range(len(S)):
        if S[i] == '(':
            balance += 1
        else:
            balance -= 1
        max_balance = max(max_balance, balance)
    return max_balance

def get_min_lex_string(A):
    B = ''
    balance = 0
    for i in range(len(A)):
        if A[i] == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            B += A[:i+1]
            break
    return B

def get_min_lex_string_2(A):
    B = ''
    balance = 0
    for i in range(len(A)):
        if A[i] == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            B += A[:i+1]
            break
    return B

def get_min_lex_string_3(A):
    B = ''
    balance = 0
    for i in range(len(A)):
        if A[i] == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            B += A[:i+1]
            break
    return B

def get_min_lex_string_4(A):
    B = ''
    balance = 0
    for i in range(len(A)):
        if A[i] == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            B += A[:i+1]
            break
    return B

def get_min_lex_string_5(A):
    B = ''
    balance = 0
    for i in range(len(A)):
        if A[i] == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            B += A[:i+1]