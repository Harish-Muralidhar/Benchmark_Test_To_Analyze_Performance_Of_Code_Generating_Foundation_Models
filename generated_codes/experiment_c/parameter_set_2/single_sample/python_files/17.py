'''

'''

def solve(n,k,e,m,scores):
    scores.sort()
    if scores[n-k]==0:
        return 0
    return scores[n-k]-1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,k,e,m = map(int, input().split())
        scores = []
        for _ in range(n-1):
            scores.append(sum(map(int, input().split())))
        scores.append(sum(map(int, input().split()))+int(input()))
        print(solve(n,k,e,m,scores))