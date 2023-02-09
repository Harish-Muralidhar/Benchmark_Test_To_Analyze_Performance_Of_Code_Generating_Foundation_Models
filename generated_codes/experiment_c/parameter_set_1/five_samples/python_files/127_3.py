'''



'''

# Write your code here

def w_index(sub, word):
    word_index = []
    for i in range(len(word)):
        if word[i:i+len(sub)] == sub:
            word_index.append([i, i+len(sub)-1])
    return word_index

def t_index(sub, word):
    for i in range(len(sub)):
        if word[i:i+len(sub)] == sub:
            return [i, i+len(sub)-1]

def t_win(t_ind, w_ind):
    s = 0
    e = len(t_ind)
    while s < e:
        if t_ind[s] in w_ind:
            return True
        s += 1
    return False

def win(s, words):
    t_ind = []
    w_ind = []
    for i in words:
        w_ind.extend(w_index(i, s))
    for i in words:
        t_ind.extend(t_index(i, s))
    if t_win(t_ind, w_ind):
        return 'Teddy'
    else:
        return 'Tracy'

def main():
    n = int(input())
    for i in range(n):
        s = input()
        n = int(input())
        words = []
        for j in range(n):
            words.append(input())
        print(win(s, words))

if __name__ == '__main__':
    main()