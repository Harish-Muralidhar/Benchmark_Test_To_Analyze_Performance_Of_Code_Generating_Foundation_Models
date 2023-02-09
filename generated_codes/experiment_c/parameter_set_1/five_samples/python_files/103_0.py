"""

Explanation
In the first test case, the answer is 4^4 = 256, so Johnny should read out the first two digits (2 and 5) and the last two digits (5 and 6).

In the second test case, the answer is 9^9 = 387420489, so Johnny should read out the first three digits (3, 8 and 7), and the last three digits (4, 8 and 9).

"""

import time
start = time.clock()
def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)

def digit(num):
    fact = factorial(num)
    #print fact
    string = str(fact)
    length = len(string)
    return length

def main():
    test_cases = int(raw_input())
    for i in range(test_cases):
        num = raw_input().split()
        a = int(num[0])
        b = int(num[1])
        c = digit(a)
        c = c%b
        print c
        
main()
print time.clock() - start