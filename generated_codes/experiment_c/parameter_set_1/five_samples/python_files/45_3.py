"""

Explanation
In the first example, the string "acab" has exactly 2 occurrences of the letter 'a', 2 occurrences of the letter 'b' and 1 occurrence of the letter 'c'. 
In the second example, the string "zzqzqq" has exactly 3 occurrences of the letter 'z', 4 occurrences of the letter 'q'. 
In the third example, the string "abc" has exactly 1 occurrence of the letter 'a', 1 occurrence of the letter 'b', 1 occurrence of the letter 'c'. 
In the fourth example, the string "kklkwwww" has exactly 2 occurrences of the letter 'k', 4 occurrences of the letter 'w', 2 occurrences of the letter 'l'.

"""

from collections import Counter

# number of test cases
t = int(input())

for i in range(t):
  
  #get string 
  s = input()
  c = Counter(s)
  
  #find the sum of the values
  total = sum(c.values())
  
  #remove the max value
  max_value = max(c.values())
  total -= max_value
  
  #if the sum of the values is equal to the max value, print YES. Otherwise print NO
  if total == max_value:
    print("YES")
  else:
    print("NO")