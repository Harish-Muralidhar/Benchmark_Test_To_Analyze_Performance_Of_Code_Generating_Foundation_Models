'''
'''

def min_score(n, k, e, m, scores):
    min_score = 0
    scores.sort()
    for i in range(n-k):
        min_score += scores[i]
    min_score = min_score + k*(e-1) + 1
    if min_score > m*e:
        return "Impossible"
    return min_score

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k, e, m = map(int, input().split())
        scores = []
        for j in range(n-1):
            scores.append(sum(map(int, input().split())))
        scores.append(sum(map(int, input().split())))
        print(min_score(n, k, e, m, scores))