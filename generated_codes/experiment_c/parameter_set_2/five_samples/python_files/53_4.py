'''

'''

# Write your code here

def is_palindrome(string):
    return string == string[::-1]

def min_deletion(string):
    if is_palindrome(string):
        return 0
    else:
        return 1

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        string = input().split()
        count = 0
        for j in string:
            count += min_deletion(j)
        print(count)

if __name__ == "__main__":
    main()