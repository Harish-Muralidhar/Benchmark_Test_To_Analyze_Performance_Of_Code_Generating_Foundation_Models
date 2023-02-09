'''

'''

def count_pairs(n, u, v):
    if u == v:
        return n
    if u > v:
        u, v = v, u
    if u == 1:
        return n // 2
    if u % 2 == 0:
        return count_pairs(n // 2, u // 2, v // 2)
    else:
        return count_pairs(n // 2, (u - 1) // 2, (v - 1) // 2)

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n, u, v = map(int, input().split())
        print(count_pairs(n, u, v))