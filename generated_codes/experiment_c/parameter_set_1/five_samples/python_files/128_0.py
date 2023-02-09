'''
'''

for i in range(int(input())):
    s = input()
    n = int(input())
    s = sorted(s)
    print(''.join(s[:n]))