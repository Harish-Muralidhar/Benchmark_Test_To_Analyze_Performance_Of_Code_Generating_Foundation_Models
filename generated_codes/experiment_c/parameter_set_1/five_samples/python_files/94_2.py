'''
'''

# Write your code here

def get_input():
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        print(get_prime_words(a, b))

def get_prime_words(a, b):
    res = 0
    if a > b:
        res = (a - b) * ((a - b - 1) // 2 + 1)
    elif a == b:
        res = a * (a - 1) // 2 + 1
    else:
        res = a * ((a - 1) // 2 + 1)
    return res % 531169


if __name__ == '__main__':
    get_input()