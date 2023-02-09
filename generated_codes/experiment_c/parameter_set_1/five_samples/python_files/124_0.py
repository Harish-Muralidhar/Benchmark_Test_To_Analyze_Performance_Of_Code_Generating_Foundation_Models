"""


=================================================

SOLUTION :

"""

def main():
    t = int(input())
    while t:
        t -= 1
        k,s = input().split()
        k = int(k)
        n = len(s)
        print(s[::-1])

if __name__ == "__main__":
    main()