'''

'''
# Write your code here
import sys

testcase = int(sys.stdin.readline())

for i in range(testcase):
    line = sys.stdin.readline()
    if int(line)<10:
        print("What an obedient servant you are!")
    else:
        print("-1")