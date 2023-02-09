'''
Sample Explanation
Explanation for the 1st example:
The string can be splitted into strings "CHEFCHEF" and "F" after one move. Then the string "CHEFCHEF" can be splitted into strings "CHEF" and "CHEF" after another move. In total we made two moves.


'''


def chef_in_string():
  s = "CHHHEEEFFCC"
  count = 0
  for i in range(0,len(s)):
    if s[i:i+4] == 'CHEF':
      count += 1
      s = s.replace('CHEF','')
  return count

print(chef_in_string())