"""

"""

def main():
    t = int(input())
    for i in range(t):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort()
        sum = 0
        for j in range(n):
            sum += a[j]
        if sum % x == 0:
            print(sum//x)
        else:
            print(-1)

if __name__ == '__main__':
    main()