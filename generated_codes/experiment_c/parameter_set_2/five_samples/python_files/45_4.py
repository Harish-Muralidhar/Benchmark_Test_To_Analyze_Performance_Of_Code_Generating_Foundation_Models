'''

Explanation
In the first test case the character 'a' occurs once, the character 'c' occurs once and the character 'b' occurs once. Thus the sum of the numbers of occurrences of the characters 'a' and 'c' is equal to the number of occurrences of the character 'b'.
In the second test case the character 'z' occurs 4 times, the character 'q' occurs 3 times and the character 'w' occurs once. Thus the sum of the numbers of occurrences of the characters 'z' and 'w' is equal to the number of occurrences of the character 'q'.
In the third test case the character 'a' occurs once, the character 'b' occurs once and the character 'c' occurs once. Thus the sum of the numbers of occurrences of the characters 'a' and 'b' is not equal to the number of occurrences of the character 'c'.
In the fourth test case the character 'k' occurs twice, the character 'l' occurs once, the character 'w' occurs 4 times. Thus the sum of the numbers of occurrences of the characters 'k' and 'l' is equal to the number of occurrences of the character 'w'.

'''

t = int(input())

for i in range(t):
    s = input()
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    l = list(d.values())
    l.sort()
    if len(l) == 1:
        print("YES")
    elif len(l) == 2:
        if l[0] == l[1]:
            print("YES")
        else:
            print("NO")
    else:
        if l[0] == l[1] and l[1] == l[2]:
            print("YES")
        elif l[0] == l[1]:
            if l[0] + l[1] == l[2]:
                print("YES")
            else:
                print("NO")
        elif l[1] == l[2]:
            if l[1] + l[2] == l[0]:
               