'''

'''

def check_winner(s, words):
    if not s:
        return 'Tracy'
    if not words:
        return 'Teddy'
    for word in words:
        if word in s:
            return check_winner(s.replace(word, ''), words)
    return 'Teddy'

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        n = int(input())
        words = []
        for _ in range(n):
            words.append(input())
        print(check_winner(s, words))

if __name__ == '__main__':
    main()