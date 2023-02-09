'''

'''

def get_min_score(N, K, E, M, scores, last_scores):
    scores.sort()
    min_score = scores[N-K-1]
    min_score += 1
    if min_score > M:
        return 'Impossible'
    return min_score

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, K, E, M = map(int, input().split())
        scores = []
        for _ in range(N-1):
            scores.append(sum(map(int, input().split())))
        last_scores = map(int, input().split())
        print(get_min_score(N, K, E, M, scores, last_scores))