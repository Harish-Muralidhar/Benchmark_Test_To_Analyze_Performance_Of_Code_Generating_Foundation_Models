'''

Input:
1
12345
Output:
54321


Input:
2
123
321
Output:
321
123
'''
def reverse(n):
    x = n
    r = 0
    while(x):
        r = r*10 + x%10
        x = x//10
    return r

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(reverse(n))