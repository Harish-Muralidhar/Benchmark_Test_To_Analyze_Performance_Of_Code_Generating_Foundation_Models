'''

Explanation
A's balance sequence is [0, 1, 0, 1, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 1, 0]. The maximal balance over all prefixes is 3.


	The string '((()))' is the only valid parentheses sequence with the minimal possible length amongst ones satisfying the conditions stated in the problem statement.

'''


def solution(s):
    print("in solution")
    d = { "(": 1, ")": -1 }
    max_balance = 0
    balance = 0
    for i in s:
        balance += d[i]
        max_balance = max(balance, max_balance)
    temp = max_balance
    print("max_balance", max_balance)
    for i in range(max_balance):
        s += "("

    temp = 0
    for i in range(max_balance):
        temp += 1
        s += ")"

    for i in range(max_balance):
        s += "("

    return s


if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        s = input().strip()
        print(solution(s))