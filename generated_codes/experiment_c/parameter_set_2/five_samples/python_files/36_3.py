'''

Explanation

Example case 1. The first phrase contains the word piygu, so the first word is still in use. The second phrase contains the word ezyfo, so the second word is still in use. The third word is not used in any of the phrases, so the answer is NO for the third word.

Example case 2. The only phrase contains the word kegqz four times, but the fourth word is vxvyj, so the answer is NO for the fourth word. The first, second and third words are not used in any of the phrases, so the answer is NO for these words.

'''

def check_word_in_phrase(word,phrase):
    for w in phrase:
        if w==word:
            return True
    return False

def check_word_in_phrases(word,phrases):
    for phrase in phrases:
        if check_word_in_phrase(word,phrase):
            return True
    return False

def check_words_in_phrases(words,phrases):
    result=[]
    for word in words:
        if check_word_in_phrases(word,phrases):
            result.append("YES")
        else:
            result.append("NO")
    return result

def main():
    t=int(input())
    for i in range(t):
        nk=input().split()
        n=int(nk[0])
        k=int(nk[1])
        words=input().split()
        phrases=[]
        for i in range(k):
            l=input().split()
            l=l[1:]
            phrases.append(l)
        result=check_words_in_phrases(words,phrases)
        print(" ".join(result))

if __name__=="__main__":
    main()