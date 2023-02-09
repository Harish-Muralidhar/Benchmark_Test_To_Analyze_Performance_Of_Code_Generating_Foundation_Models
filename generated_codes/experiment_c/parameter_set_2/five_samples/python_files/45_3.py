'''

Explanation
The first test case has 4 characters. The character 'a' occurs twice and the characters 'c' and 'b' occur once. The sum of the numbers of occurrences of 'c' and 'b' is 1 + 1 = 2 which is equal to the number of occurrences of 'a'.

The second test case has 7 characters. The character 'z' occurs 4 times and the characters 'q' occurs 3 times. The sum of the numbers of occurrences of 'q' is 3 which is equal to the number of occurrences of 'z'.

The third test case has 3 characters. The character 'a' occurs once and the characters 'b' and 'c' occur once. The sum of the numbers of occurrences of 'b' and 'c' is 1 + 1 = 2 which is not equal to the number of occurrences of 'a'.

The fourth test case has 8 characters. The character 'k' occurs 2 times and the characters 'l' and 'w' occur 3 times. The sum of the numbers of occurrences of 'l' and 'w' is 3 + 3 = 6 which is equal to the number of occurrences of 'k'.

'''

# Write your code here

def count_char(str):
    count = {}
    for i in str:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

def check_sum(count):
    for i in count:
        if count[i] == sum(count.values()) - count[i]:
            return True
        else:
            return False

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        str = input()
        count = count_char(str)
        if check_sum(count):
            print("YES")
        else:
            print("NO")