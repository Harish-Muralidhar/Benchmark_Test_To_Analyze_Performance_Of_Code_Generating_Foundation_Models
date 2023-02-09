'''

In the third example,
you can paint the first and last balloons to make all of them appear to be the same color. So, the answer is 2.

'''

# Write your code here

def min_balloons(s):
    if len(s) == 1:
        return 0
    if s[0] == s[-1]:
        return 0
    else:
        return 1

def main():
    t = int(input())
    for i in range(t):
        s = input()
        print(min_balloons(s))

if __name__ == '__main__':
    main()