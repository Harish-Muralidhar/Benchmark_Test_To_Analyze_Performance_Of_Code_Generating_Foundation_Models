'''


'''

def check(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
    return stack

def main():
    t = int(input())
    for i in range(t):
        s = input()
        stack = check(s)
        if stack:
            print(s[:len(s)-len(stack)])
        else:
            print(s)

if __name__ == '__main__':
    main()