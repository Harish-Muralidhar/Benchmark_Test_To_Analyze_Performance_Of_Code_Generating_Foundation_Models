"""

If Sergey gets any score greater than 4, he'll get enrolled anyway.
If Sergey gets 3 or less points, he won't get enrolled.

"""

def get_input():
    return int(input())

def get_list():
    return list(map(int, input().split()))

def get_min(N, K, E, M, scores, min_score):
    total_score = sum(scores)
    total_min_score = sum(min_score)
    if K == 0:
        return 0
    elif K == N:
        return M - total_score
    elif K == N-1:
        return total_min_score - total_score + 1
    else:
        return total_min_score - total_score + 1
    return 0

def main():
    T = get_input()
    for i in range(T):
        N, K, E, M = get_list()
        scores = []
        for j in range(N-1):
            scores.append(get_list())

        min_score = get_list()
        min_score.append(get_min(N, K, E, M, scores[j], min_score))

        print(min_score[-1])

if __name__ == '__main__':
    main()