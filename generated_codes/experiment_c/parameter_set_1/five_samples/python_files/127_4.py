"""
S and wi are composed of lowercase English alphabets
S and wi contains only lowercase English alphabets (i.e. letters 'a'-'z')

Allocated time: 10 mins
"""

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        n = int(input())
        d = [input() for _ in range(n)]
        if (len(s) == 0):
            print("Tracy")
        else:
            flag = False
            for i in range(n):
                if (gcd(len(s), len(d[i])) > 1):
                    flag = True
                    break
            if (flag):
                print("Tracy")
            else:
                print("Teddy")

if __name__ == "__main__":
    main()