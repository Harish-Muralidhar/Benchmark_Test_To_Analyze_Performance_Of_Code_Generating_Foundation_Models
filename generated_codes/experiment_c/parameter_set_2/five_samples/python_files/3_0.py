'''


'''


def F(S):
    balance = 0
    max_balance = 0
    for index in range(len(S)):
        if S[index] == '(':
            balance = balance + 1
        if S[index] == ')':
            balance = balance - 1
        max_balance = max(max_balance, balance)
    return max_balance


def get_min_string(A):
    balance = 0
    min_string = ""
    for index in range(len(A)):
        if A[index] == '(':
            balance = balance + 1
        if A[index] == ')':
            balance = balance - 1
        if balance == 0:
            min_string = A[:index + 1]
            break
    return min_string


def get_max_string(A):
    balance = 0
    max_string = ""
    for index in range(len(A)):
        if A[index] == '(':
            balance = balance + 1
        if A[index] == ')':
            balance = balance - 1
        if balance == 0:
            max_string = A[:index + 1]
            break
    return max_string


def get_min_string_with_max_balance(A):
    min_string = ""
    max_balance = F(A)
    for index in range(len(A)):
        if A[index] == '(':
            balance = F(A[:index + 1])
            if balance == max_balance:
                min_string = A[:index + 1]
                break
    return min_string


def get_max_string_with_max_balance(A):
    max_string = ""
    max_balance = F(A)
    for index in range(len(A)):
        if A[index] == ')':
            balance = F(A[:index + 1])
            if balance == max_balance:
                max_string = A[:index + 1]
                break
    return max_string


def get_min_string_with_