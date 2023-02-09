"""


"""

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        n, k = map(int,input().split())
        dictionary = input().split()
        phrases = []
        for _ in range(k):
            phrases.append(input().split()[1:])
        for word in dictionary:
            if any(word in phrase for phrase in phrases):
                print("YES",end=" ")
            else:
                print("NO",end=" ")
        print()

if __name__ == '__main__':
    main()