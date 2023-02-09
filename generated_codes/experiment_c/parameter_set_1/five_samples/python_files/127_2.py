'''

Subtask 1 (30 points):
1 <= N <= 10

Subtask 2 (70 points):
Original constraints

'''


def check_win(s, dic):
    if not s:
        return 'Tracy'
    for x in dic:
        i = s.find(x)
        if i >= 0:
            if check_win(s[:i], dic) == 'Tracy':
                return 'Teddy'
            else:
                return 'Tracy'

    return 'Teddy'


t = int(input())

for i in range(t):
    s = input()
    dicti = {}
    _ = int(input())
    dicti = set([x for x in input().split()])
    print(check_win(s, dicti))