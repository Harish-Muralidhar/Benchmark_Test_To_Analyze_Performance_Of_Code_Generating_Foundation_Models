"""


"""

def main():
    t = int(input())
    while t > 0:
        n, m = map(int, input().split())
        a = []
        for i in range(n):
            a.append(list(map(int, input())))
        count = 0
        for i in range(m):
            for j in range(i+1, m):
                for k in range(n):
                    if a[k][i] == 1 and a[k][j] == 1:
                        count += 1
        print(count)
        t -= 1

if __name__ == '__main__':
    main()