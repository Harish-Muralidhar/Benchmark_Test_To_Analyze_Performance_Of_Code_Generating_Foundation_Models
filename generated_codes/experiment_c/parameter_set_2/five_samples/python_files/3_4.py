'''


'''

#code

t = int(input())
for i in range(t):
    s = input()
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                stack.append(i)
    print('('*len(stack)+s+')'*len(stack))