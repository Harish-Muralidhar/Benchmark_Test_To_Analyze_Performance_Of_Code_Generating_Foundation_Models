'''

'''

for _ in range(int(input())):
    string = input()
    stack = []
    balance = 0
    for i in string:
        if i=='(':
            stack.append(i)
            balance+=1
        else:
            stack.append(i)
            balance-=1
    for i in range(balance):
        stack.append(')')
    print(''.join(stack))