'''

Explanation

- Case 1 : N < 10 i.e. 1 < 10. Hence the output is "What an obedient servant you are!".

- Case 2 : N > 10 i.e. 12 > 10. Hence the output is "-1".

- Case 3 : N < 10 i.e. -5 < 10. Hence the output is "What an obedient servant you are!".

'''

import sys

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        if n < 10:
            print("What an obedient servant you are!")
        else:
            print("-1")

if __name__ == "__main__":
    main()