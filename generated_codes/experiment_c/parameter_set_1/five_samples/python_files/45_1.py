'''

Explanation
In the first example the character 'a' occurs one time, the character 'c' occurs one time, the character 'b' occurs one time. The sum of these numbers is equal to 1 + 1 + 1 = 3. The number of occurrences of the character 'a' is equal to the sum of the numbers of occurrences of the other characters, which means that the given string satisfies the condition.

In the second example the character 'z' occurs four times, the character 'q' occurs two times. The sum of these numbers is equal to 4 + 2 = 6. The number of occurrences of the character 'z' is equal to the sum of the numbers of occurrences of the other characters, which means that the given string satisfies the condition.

In the third example the character 'a' occurs one time, the character 'b' occurs one time, the character 'c' occurs one time. The sum of these numbers is equal to 1 + 1 + 1 = 3. The number of occurrences of the character 'a' is not equal to the sum of the numbers of occurrences of the other characters, which means that the given string does not satisfies the condition.

In the fourth example the character 'k' occurs two times, the character 'l' occurs one time, the character 'w' occurs four times. The sum of these numbers is equal to 2 + 1 + 4 = 7. The number of occurrences of the character 'k' is equal to the sum of the numbers of occurrences of the other characters, which means that the given string satisfies the condition.

'''

def check_letters(string):
    for letter in string:
        if string.count(letter) == sum([string.count(x) for x in string if x != letter]):
            return "YES"
        else:
            return "NO"

def test():
    assert check_letters("acab") == "YES"
    assert check_letters("zzqzqq") == "YES"
    assert check_letters("abc") == "NO"
    assert check_letters("kklkwwww") == "YES"

test()