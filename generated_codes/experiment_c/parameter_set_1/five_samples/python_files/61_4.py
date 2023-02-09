'''

There are multiple test sets. Each test set is worth 1 point. 
Your overall score is computed as the sum of points you have scored on all the test sets. 
If your program fails on a test set, you will get 0 points for it. 

N_TEST_SETS is at most 100.
N is at most 10^6.
Ai is at most 10^9.

'''

# SOLUTION

def answer(a):
    count = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            count += a[i] & a[j]
    return count
    
if __name__ == "__main__":
    n = int(input())
    a = [int(i) for i in input().split()]
    print (answer(a))