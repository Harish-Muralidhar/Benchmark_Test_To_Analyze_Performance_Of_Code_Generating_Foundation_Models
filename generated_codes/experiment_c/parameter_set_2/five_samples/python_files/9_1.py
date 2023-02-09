'''

Sample Explanation
In the first example, the optimal solution is to make two moves:

Move 1: remove the symbols "C", "H", "E", "F" from the string, the string becomes "CHEFF".
Move 2: remove the symbols "C", "H", "E", "F" from the string, the string becomes "".
In the second example, the optimal solution is to make one move:

Move 1: remove the symbols "C", "H", "E", "F" from the string, the string becomes "HHEEFFC".

'''

def chef_in_string(s):
    chef = 'chef'
    i = 0
    count = 0
    while i < len(s):
        if s[i] == chef[0]:
            if s[i:i+4] == chef:
                count += 1
                i += 4
            else:
                i += 1
        else:
            i += 1
    return count

if __name__ == '__main__':
    s = input()
    print(chef_in_string(s))