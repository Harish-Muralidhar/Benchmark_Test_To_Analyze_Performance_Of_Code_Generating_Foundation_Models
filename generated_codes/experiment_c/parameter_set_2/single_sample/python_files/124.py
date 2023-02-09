"""

Explanation

In the first test case, the Chef created 4 appetizers and numbered them 00, 01, 10, and 11. The appetizers were finished in the order 00, 11, 10, and 01. The server placed the appetizers in the order cehf.

In the second test case, the Chef created 16 appetizers and numbered them 0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, and 1111. The appetizers were finished in the order 0000, 0111, 1011, 1110, 0100, 0011, 1001, 1101, 0010, 0101, 1010, 1111, 0110, 0001, 1000, 1100. The server placed the appetizers in the order eayejpuinpopolre.

"""

def main():
    t = int(input())
    for _ in range(t):
        k, s = input().split()
        k = int(k)
        n = 2**k
        s = s[:n]
        print(s[::-1])

if __name__ == '__main__':
    main()