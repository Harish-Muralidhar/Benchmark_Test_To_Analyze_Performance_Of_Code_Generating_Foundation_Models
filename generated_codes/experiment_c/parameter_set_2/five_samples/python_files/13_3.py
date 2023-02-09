'''

Explanation

In the first case, all three people are already close enough to communicate directly.

In the second case, the Chef and the head server are close enough to communicate directly, but the sous-chef is too far away from the Chef. However, the sous-chef is close enough to the head server so they can communicate through the head server.

In the third case, any two people are close enough to communicate directly, but there will always be a third person who is too far away to participate in the conversation.

'''

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def main():
    t = int(input())
    for i in range(t):
        r = int(input())
        x1, y1 = map(int, input().split())
        x2, y2 = map(int, input().split())
        x3, y3 = map(int, input().split())
        if distance(x1, y1, x2, y2) <= r:
            if distance(x1, y1, x3, y3) <= r or distance(x2, y2, x3, y3) <= r:
                print("yes")
            else:
                print("no")
        elif distance(x1, y1, x3, y3) <= r:
            if distance(x2, y2, x3, y3) <= r:
                print("yes")
            else:
                print("no")
        elif distance(x2, y2, x3, y3) <= r:
            if distance(x1, y1, x3, y3) <= r:
                print("yes")
            else:
                print("no")
        else:
            print("no")

if __name__ == "__main__":
    main()