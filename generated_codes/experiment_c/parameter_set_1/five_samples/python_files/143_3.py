/*



*/

from itertools import permutations

T = int(input())

for i in range(T):
    K = int(input())
    s = list(input())
    #print(s)
    
    # if '?' not in s:
    #     print(''.join(s))
    
    # if N == 1:
    #     if '?' in s:
    #         for i in range(K):
    #             s[s.index('?')] = str(i)
    #             print(''.join(s))
    #             break
    #     else:
    #         print(''.join(s))

    # else:
    #     if '?' in s:
    #         if (s[0] != s[-1]) and (s[0] != s[1]):
    #             for i in range(K):
    #                 s[s.index('?')] = str(i)
    #                 print(''.join(s))
    #                 break
    #         else:
    #             print('NO')
    #     else:
    #         print(''.join(s))

    # if '?' in s:
    #     if (s[0] != s[-1]) and (s[0] != s[1]):
    #         for i in range(K):
    #             s[s.index('?')] = str(i)
    #             print(''.join(s))
    #             break
    #     else:
    #         print('NO')
    # else:
    #     print(''.join(s))
    
    if '?' in s:
        if (s[0] != s[-1]) and (s[0] != s[1]):
            for i in range(K):
                s[s.index('?')] = str(i)
                print(''.join(s))
                break
        else:
            print('NO')
    elif '?' not in s:
        print(''.join(s))
    else:
        print('NO')