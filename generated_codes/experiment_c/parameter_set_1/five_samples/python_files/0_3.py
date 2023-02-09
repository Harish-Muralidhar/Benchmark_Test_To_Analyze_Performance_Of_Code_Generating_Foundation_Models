"""
So, BWBW is the lexicographically smallest arrangement maximizing the value.

"""

for _ in range(int(input())):
    
    s1 = input()
    s2 = input()
    
    a = [0]*26
    b = [0]*26
    
    
    for i in s1:
        a[ord(i)-65] += 1
    for i in s2:
        b[ord(i)-65] += 1
        
    count = 0
    for i in range(26):
        if a[i] > b[i]:
            count += abs(a[i]-b[i])
    print(count)