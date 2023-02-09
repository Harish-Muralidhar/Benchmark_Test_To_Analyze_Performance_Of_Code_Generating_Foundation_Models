"""
"""

# cook your dish here
for i in range(int(input())):
    max = int(input())
    count = 0
    while max > 0:
        max = max - 2**(count)
        count +=1
    print(count-1)