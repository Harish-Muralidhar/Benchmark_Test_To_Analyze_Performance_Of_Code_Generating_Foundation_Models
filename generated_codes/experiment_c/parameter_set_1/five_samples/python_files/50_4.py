'''

Solution:

1) Find the frequency of all the alphabets in the string.

2) Find the number of triplets in the string by finding the number of pairs of first letter and then finding the triplets

3) Now, for each triplet, we need to find the number of pairs it can be formed with.

4) Every combination of three letters can be used to form a triplet.

5) There are four possibilities.

6) Three letters of the same kind and three letters of different kinds.

7) The frequency of the first letter should be >1 and the frequencies of other letters should be >0.

8) Sum the frequency of the letters.

9) There are three possibilities. Three of the same kind and two of one kind and one of another kind.

10) The frequency of the first letter should be >2 and the frequencies of other letters should be >0.

11) Sum the frequency of the letters.

12) There is one possibility. Two of each kind.

13) The frequencies of all the letters should be >1.

14) Multiply the frequency of the letters.

15) Find the answer by subtracting the number of triplets from the number of substrings of the string.

'''

from collections import Counter

n = input()

a = Counter(n)

n = len(n)

#print(a)

b = list(a.values())

#print(b)

l = len(b)

s = 0

for i in b:

   s += i * (i-1) * (i-2) // 6

#print(s)

#print(n)

for i in range(l):

    s += b[i] * (b[i]-1) // 2 * (n - b[i])

#print(s)

for i in range(l):

    for j in range(i+1, l):

        s += b[i] * b[j] * (n - b[i] - b[j])

#print(s)

for i in range(l):

    for j in range(i+1, l):

        for k in range(j+1, l):

            s += b[i] * b[j] * b[k]

#print(s)

print(n*(n-1)*(n-2)//6 - s)