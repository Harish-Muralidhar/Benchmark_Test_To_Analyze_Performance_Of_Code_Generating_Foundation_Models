'''

In the third example,
You need to paint 2 balloons.

Note: Your code should be able to convert the sample input into the sample output. However, this is not enough to pass the challenge, because the code will be run on multiple test cases. Therefore, your code must solve this problem statement.

'''

# Write your code here
import sys

def count_flips(s):
    flips = 0
    while len(s) > 1:
        if s[0] == s[1]:
            s = s[1:]
        else:
            flips += 1
            s = s[1:]
    return flips
        
if __name__ == "__main__":
    test_cases = int(input().strip())
    for a_tc in range(test_cases):
        s = input().strip()
        print(count_flips(s))