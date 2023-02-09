"""

"""

def reverse_bits(n):
    rev_n = 0
    while n > 0:
        rev_n = (rev_n << 1) | (n & 1)
        n = n >> 1
    return rev_n

def main():
    t = int(input())
    for i in range(t):
        k, s = input().split()
        k = int(k)
        n = 2**k
        s = list(s)
        for i in range(n):
            s[reverse_bits(i)] = s[i]
        print(''.join(s))

if __name__ == '__main__':
    main()