'''
Example case 2. In this example 2 as 20 is greater than 10.
Example case 3. In this example 3 as 10 is equal to 10.
'''

# Write your code here
import sys

def main():
    t=int(sys.stdin.readline())
    for i in range(t):
        a,b=map(int,sys.stdin.readline().split())
        if a>b:
            print('>')
        elif a<b:
            print('<')
        else:
            print('=')

main()