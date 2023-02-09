'''
=100, nnn=2, nnn=1.

'''

def play_game(n,k):
    for i in range(k):
        op,li,logical_value = input().split()
        li = int(li)
        if op == '<':
            if logical_value == 'Yes':
                n = min(n,li-1)
            else:
                n = max(n,li)
        elif op == '>':
            if logical_value == 'Yes':
                n = max(n,li+1)
            else:
                n = min(n,li)
        else:
            if logical_value == 'Yes':
                n = li
            else:
                n = li+1
    return n

t = int(input())
for i in range(t):
    k = int(input())
    n = 10**9
    print(play_game(n,k))