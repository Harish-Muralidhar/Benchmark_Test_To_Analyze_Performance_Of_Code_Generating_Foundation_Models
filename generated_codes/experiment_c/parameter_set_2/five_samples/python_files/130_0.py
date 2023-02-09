'''


'''

def main():
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        n = len(s)
        i = 1
        j = 0
        while i < n:
            if s[i] == '.':
                j += 1
                i += 1
            else:
                i += 1
        print(j)

if __name__ == "__main__":
    main()