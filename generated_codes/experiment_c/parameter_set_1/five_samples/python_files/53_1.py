'''

'''

'''

#Note: - 

Take all the strings as a list.

Check the count of a

Check the count of b

If the count of a == count of b:
    
    Calculate the length of the individual string.
    If the length of the individaul string is equal to 1:
        Then return the length of the list
    else:
        return len(list)-1

else:
    return the maximum count of a or b

'''

def palindrome(list):
    count_a = 0
    count_b = 0
    for i in list:
        if len(i) == 1:
            if i == "a":
                count_a += 1
            else:
                count_b += 1
        else:
            if i[0] == "a" and i[1] == "a":
                count_a += 2
            elif i[0] == "b" and i[1] == "b":
                count_b += 2
            else:
                count_a += 1
                count_b += 1
    if count_a == count_b:
        res = len(list)
        for i in list:
            if len(i) == 1:
                return res
            else:
                res -= 1
        return res
    else:
        return max(count_a, count_b)


T = int(input())
while T > 0:
    N = int(input())
    list = input().split()
    print(palindrome(list))
    T -= 1