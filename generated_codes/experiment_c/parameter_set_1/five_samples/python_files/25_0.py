"""


"""


def reverse_number(num):
    rev = 0
    while num > 0:
        rev = (rev*10) + (num%10)
        num = num//10
    return rev

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(reverse_number(n))