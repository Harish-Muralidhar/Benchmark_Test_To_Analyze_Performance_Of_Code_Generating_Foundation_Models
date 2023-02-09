'''


'''


def count_ways(n):
    return (
        (n // 2) + 1
    )

def main():
    t = int(input())

    while t:
        n = int(input())
        print(count_ways(n))
        t -= 1


if __name__ == '__main__':
    main()