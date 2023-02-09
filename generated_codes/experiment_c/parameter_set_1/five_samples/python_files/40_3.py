NOT INDIAN

Explanation
Example case 1. The first person only knows about English gestures. So he cannot be an Indian. The next person uses "Indian Yes" gesture. Hence, he is an Indian. The third person is a contradiction: for him both "Yes" and "No" have the same gesture! So we conclude that the information is insufficient to make a decision about his nationality. The last two persons do not know about the Indian gesture, so they cannot be Indians.



A:

<code>def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        if 'I' in s:
            print('INDIAN')
        elif 'Y' in s:
            print('NOT INDIAN')
        else:
            print('NOT SURE')

if __name__ == '__main__':
    main()
</code>
