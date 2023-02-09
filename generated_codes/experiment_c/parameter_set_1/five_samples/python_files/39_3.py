'''

'''

def max_coins( N, K):
    max_coins = 0
    for i in range(1,K+1):
        num_of_coins_for_people = N // i
        if num_of_coins_for_people % i == 0:
            max_coins = num_of_coins_for_people
            return max_coins
    else:
        num_of_coins_for_people = N // (i-1)
        if num_of_coins_for_people % (i-1) == 0:
            max_coins = num_of_coins_for_people

    return max_coins

def main():
    T = int(input())
    while T>0:
        N,K = map(int,input().split())
        print(max_coins(N,K))
        T -= 1


if __name__ == '__main__':
    main()