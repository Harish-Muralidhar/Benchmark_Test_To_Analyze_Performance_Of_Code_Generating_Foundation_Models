'''
Explanation

In the first test case, the subarray 2 3 4 is the favorite sequence. 
In the second test case, 2 3 4 is not a subarray in the sequence.
'''


def substring(string, substring):
    if substring in string:
        return "Yes"
    return "No"

t = int(input())
while(t):
    n = int(input())
    string = list(map(int, input().split()))
    k = int(input())
    sub_string = list(map(int, input().split()))
    if k <= n:
        new_string = ' '.join([str(i) for i in string])
        new_sub_string = ' '.join([str(i) for i in sub_string])
        print(substring(new_string, new_sub_string))
    t = t-1