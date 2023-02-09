'''


'''


def game_result(a):
    if len(a) == 1:
        return a[0]
    else:
        a = [abs(a[i] - a[i+1]) for i in range(0, len(a)-1)]
        return game_result(a)


def subsequence_generator(a):
    if len(a) == 1:
        return [a, []]
    elif len(a) == 2:
        return [a, [a[0]], [a[1]], []]
    else:
        previous = subsequence_generator(a[:-1])
        ss = []
        for p in previous:
            ss.append(p)
            ss.append(p + [a[-1]])
        return ss


def subsequence_game_result(a):
    if len(a) == 1:
        return a[0] == 1
    else:
        a = [abs(a[i] - a[i+1]) for i in range(0, len(a)-1)]
        return subsequence_game_result(a)


def subsequence_count(a):
    ss = subsequence_generator(a)
    count = 0
    for s in ss:
        if subsequence_game_result(s):
            count += 1
    return count


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(100000)
    t = int(input())
    for i in range(t):
        n = int(input())
        a = [int(i) for i in input().split()]
        print(subsequence_count(a))