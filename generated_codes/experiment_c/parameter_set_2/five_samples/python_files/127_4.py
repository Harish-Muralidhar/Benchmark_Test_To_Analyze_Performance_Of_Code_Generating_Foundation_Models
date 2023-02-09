'''
wi are distinct

'''

def get_winner(s, dict):
    if s in dict:
        return 'Tracy'
    else:
        return 'Teddy'

def get_winner_optimized(s, dict):
    if s in dict:
        return 'Tracy'
    else:
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] in dict:
                    return 'Teddy'
        return 'Tracy'

def get_winner_optimized_2(s, dict):
    if s in dict:
        return 'Tracy'
    else:
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] in dict:
                    return 'Teddy'
        return 'Tracy'

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input()
        n = int(input())
        dict = []
        for j in range(n):
            dict.append(input())
        print(get_winner_optimized(s, dict))