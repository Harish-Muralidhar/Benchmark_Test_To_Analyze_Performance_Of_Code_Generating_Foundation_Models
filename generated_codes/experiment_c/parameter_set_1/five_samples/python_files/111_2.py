'''

Test Case Generation

Test Case 1

Input : 

C0D3C43F

Output :

3943

Explanation :

Changing the character 'C' to the character '9' thus giving the string "C0D3943F" gives the maximum age of the universe.


Test Case 2

Input :

C0D3C45F

Output :

3945

Explanation :

Changing the character 'C' to the character '9' thus giving the string "C0D3945F" gives the maximum age of the universe.


'''

from itertools import combinations

s = input()

def wrong(s):
    for i in range(len(s)):
        temp = list(s)
        for j in range(10):
            temp[i] = str(j)
            for k in range(26):
                temp[i] = chr(65+k)
                yield "".join(temp)

def check(s):
    return all(i in "0123456789" for i in s)

print(max(int(i) for i in wrong(s) if check(i)))