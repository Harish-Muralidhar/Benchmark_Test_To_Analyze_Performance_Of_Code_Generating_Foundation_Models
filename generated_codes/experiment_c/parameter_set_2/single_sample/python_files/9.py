'''

'''

from collections import Counter

def main():
    s = input()
    c = Counter(s)
    print(min(c['C'],c['H'],c['E'],c['F']))

if __name__ == '__main__':
    main()