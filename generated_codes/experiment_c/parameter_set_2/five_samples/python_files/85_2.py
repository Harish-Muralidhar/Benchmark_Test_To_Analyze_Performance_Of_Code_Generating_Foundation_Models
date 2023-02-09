'''

'''

#Solution

#!/usr/bin/python3

from math import log2

def get_parent(x):
    if x % 2 == 0:
        return x // 2
    else:
        return (x - 1) // 2

def get_left_child(x):
    return 2 * x

def get_right_child(x):
    return 2 * x + 1

def get_path(u, v):
    path = []
    while u != v:
        if u > v:
            path.append(0)
            u = get_parent(u)
        else:
            path.append(1)
            v = get_parent(v)
    return path

def get_answer(n, u, v):
    path = get_path(u, v)
    answer = 1
    for i in range(len(path)):
        if path[i] == 0:
            answer += get_right_child(answer)
        else:
            answer += get_left_child(answer)
    return answer

def main():
    q = int(input())
    for _ in range(q):
        n, u, v = map(int, input().split())
        print(get_answer(n, u, v))

if __name__ == '__main__':
    main()