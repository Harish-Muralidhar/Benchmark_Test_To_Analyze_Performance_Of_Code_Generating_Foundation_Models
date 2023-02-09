'''

Sample Explanation
In the first sample case, we can make two moves:

1. Remove the symbols "CHE" from the string. The string becomes "FCHEFFF".
2. Remove the symbols "CHEF" from the string. The string becomes "F".

In the second sample case, we can make only one move:

1. Remove the symbols "CHEF" from the string. The string becomes "HHEEFCC".

'''

# Write your code here
import re

str1 = input()

pattern = re.compile("CHEF")

count = 0

while True:
    if re.search(pattern, str1):
        str1 = re.sub(pattern, "", str1)
        count += 1
    else:
        break

print(count)