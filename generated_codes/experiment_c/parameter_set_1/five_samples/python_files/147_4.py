"""

"""

import sys

def main():
    count = 0
    n = int(input())

    for i in range(n):
        list = input().split(" ")
        count = 0

        for j in range(len(list)):
            if int(list[j]) == j+1:
                count = count + 1

        print(count)

if __name__ == "__main__":
    main()