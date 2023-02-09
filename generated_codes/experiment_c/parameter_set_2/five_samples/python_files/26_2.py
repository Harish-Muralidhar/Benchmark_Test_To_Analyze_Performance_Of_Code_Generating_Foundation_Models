'''

Explanation

- Test Case 1:
Since the value given is less than 10, we print the required string.

- Test Case 2:
Since the value given is greater than 10, we print -1.

- Test Case 3:
Since the value given is less than 10, we print the required string.

'''

# Write your code here

T = int(input())

for i in range(T):
    N = int(input())
    if N < 10:
        print("What an obedient servant you are!")
    else:
        print("-1")