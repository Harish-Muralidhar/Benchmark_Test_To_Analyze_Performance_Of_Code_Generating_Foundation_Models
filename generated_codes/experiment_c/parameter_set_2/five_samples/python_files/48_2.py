'''

'''

# Write your code here
def find_missing_doll(n,dolls):
    for i in range(n):
        if dolls.count(dolls[i])%2 != 0:
            return dolls[i]

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        dolls = list(map(int,input().strip().split()))
        print (find_missing_doll(n,dolls))