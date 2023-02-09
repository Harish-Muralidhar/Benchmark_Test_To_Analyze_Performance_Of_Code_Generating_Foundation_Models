'''

'''

def count_pairs(n, u, v):
    u = u - 1
    v = v - 1
    count = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                count += 1
                continue
            if i == u and j == v:
                count += 1
                continue
            if i == v and j == u:
                count += 1
                continue
            if i < u and j < v:
                if i == j:
                    count += 1
                    continue
                if i == u - 1 and j == v - 1:
                    count += 1
                    continue
                if i == v - 1 and j == u - 1:
                    count += 1
                    continue
                if i == u - 2 and j == v - 2:
                    count += 1
                    continue
                if i == v - 2 and j == u - 2:
                    count += 1
                    continue
                if i == u - 3 and j == v - 3:
                    count += 1
                    continue
                if i == v - 3 and j == u - 3:
                    count += 1
                    continue
                if i == u - 4 and j == v - 4:
                    count += 1
                    continue
                if i == v - 4 and j == u - 4:
                    count += 1
                    continue
                if i == u - 5 and j == v - 5:
                    count += 1
                    continue
                if i == v - 5 and j == u - 5:
                    count += 1
                    continue
                if i == u - 6 and j == v - 6:
                    count += 1
                    continue
                if i == v - 6 and j == u - 6:
                    count += 1
                    continue
                if i == u - 7 and j == v - 7:
                    count += 1
                    continue
                if i == v - 7 and j == u - 7:
                    count += 1
                    continue
                if i == u - 8 and j == v - 8:
                    count += 1
                    continue
                if i == v - 8 and j == u - 8:
                    count += 1
