'''

'''


# Write your code here
def min_max_diff(s1, s2):
    c = 0
    l = []
    for i in range(len(s1)):
        if s1[i]=='?' or s2[i]=='?':
            c+=1
        if s1[i]!=s2[i] and (s1[i]=='?' or s2[i]=='?'):
            c-=1
            l.append(c)
        if s1[i]!=s2[i] and (s1[i]!='?' or s2[i]!='?'):
            l.append(c)
    # print(l)
    return min(l), max(l)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s1 = input()
        s2 = input()
        print(*min_max_diff(s1, s2))