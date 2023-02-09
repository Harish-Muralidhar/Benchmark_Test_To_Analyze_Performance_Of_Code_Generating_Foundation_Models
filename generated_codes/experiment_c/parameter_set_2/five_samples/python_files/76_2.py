"""
"""

def main():
    t = int(input())
    while t>0:
        x = int(input())
        b = int(input())
        dishes = list(map(int,input().split()))
        c = int(input())
        tribes = list(map(int,input().split()))
        print(find_min_people(x,b,dishes,c,tribes))
        t-=1

def find_min_people(x,b,dishes,c,tribes):
    dishes = [0] + dishes
    tribes = [0] + tribes
    dp = [0]*(x+1)
    for i in range(1,x+1):
        dp[i] = dp[i-1]
        if i in dishes:
            dp[i] = max(dp[i],dishes[i])
        if i in tribes:
            dp[i] = max(dp[i],tribes[i])
    return dp[x]

if __name__ == '__main__':
    main()