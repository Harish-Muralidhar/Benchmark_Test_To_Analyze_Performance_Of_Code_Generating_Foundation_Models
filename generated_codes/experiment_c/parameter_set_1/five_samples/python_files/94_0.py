"""


Input:
3
10 10
3 2
6 7

Output:
37794
8
66


"""

"""
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_prime_numbers(a, b):
    num_list = list(range(a, b))
    for num in num_list:
        if not is_prime(num):
            num_list.remove(num)
    return num_list
"""

def find_prime_words(a, b):
    if a == 1 and b == 1:
        return 0
    if a == 1 and b > 1:
        return 1
    if a > 1 and b == 1:
        return 1
    if a == b:
        return 2
    if a != b:
        return 3
    return 0


def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        # print(find_prime_words(a, b))
        print(find_prime_words(a, b) % 531169)


if __name__ == '__main__':
    main()