'''

In the third example,
you can paint the first and last balloon. So, the answer is 2.

'''

def min_balloon_paint(s):
    if s.count('a') == len(s) or s.count('b') == len(s):
        return 0
    else:
        return min(s.count('a'), s.count('b'))

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(min_balloon_paint(s))