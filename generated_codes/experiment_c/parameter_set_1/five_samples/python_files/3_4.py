'''

'''

def find_new_parentheses(parentheses):
    if len(parentheses) < 1:
        return -1
    
    i = 0
    j = 1
    while i < j and j < len(parentheses):
        
        if parentheses[j] == '(':
            j += 1
        else:
            if parentheses[i] == ')':
                j += 1
            else:
                i += 1
                j += 1
    
    return parentheses[i:j]


if __name__ == '__main__':
    t = int(input().strip())
    for i in range(t):
        s = input().strip()
        print('Case #{}: {}'.format(i+1, find_new_parentheses(s)))