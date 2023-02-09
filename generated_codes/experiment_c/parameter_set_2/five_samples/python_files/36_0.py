"""


Explanation

Example case 1. The first phrase of the second test case contains the 0^th and 2^nd words of the dictionary of the forgotten language.

Example case 2. The only phrase of the second test case contains the 3^rd word of the dictionary of the forgotten language.

"""

def main():
    test_cases = int(input())
    for i in range(test_cases):
        n, k = map(int, input().split())
        dictionary = input().split()
        for j in range(k):
            phrase = input().split()
            for word in phrase:
                if word in dictionary:
                    print("YES", end = " ")
                    break
            else:
                print("NO", end = " ")
        print()

if __name__ == "__main__":
    main()