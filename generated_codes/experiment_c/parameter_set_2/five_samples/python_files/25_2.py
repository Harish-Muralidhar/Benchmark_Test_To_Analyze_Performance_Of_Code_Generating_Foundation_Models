'''

'''

def reverse(n):
    return int(str(n)[::-1])

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(reverse(n))