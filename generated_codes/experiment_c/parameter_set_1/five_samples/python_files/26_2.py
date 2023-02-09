'''

'''
import sys

def main():
    a = []
    T = int(input())
    for i in range(T):
        N = int(input())
        if N < 10:
            a.append("What an obedient servant you are!")
        else:
            a.append("-1")

    for i in a:
        print(i)
if __name__ == "__main__":
    main()