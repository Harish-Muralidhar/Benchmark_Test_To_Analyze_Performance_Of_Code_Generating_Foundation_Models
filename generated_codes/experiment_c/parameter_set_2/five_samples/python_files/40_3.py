"""


Explanation
Example case 1. The first person only knows about one gesture, which is the Indian "Yes" gesture. This is insufficient information to make a decision.
Example case 2. The second person uses "Yes" and "No" gestures only. This is a clear indication that the person is not from India.
Example case 3. The third person uses all three gestures. This is a clear indication that the person is from India.

"""

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        if s.count("Y") > 0:
            print("NOT INDIAN")
        elif s.count("I") > 0:
            print("INDIAN")
        else:
            print("NOT SURE")

main()