'''

'''

"""
Solution Approach :
===================
* this is basic Dynamic programming question
* here we use 1D array of size (sum+1)
* for each iteration we calculate the number of combinations for given amount and store it at index i in the array
* and after the iteration we return the count from the last index of array
"""


def count_num_of_combinations_for_given_sum(amount, denominations):
    num_of_combinations = [0] * (amount + 1)
    num_of_combinations[0] = 1
    for coin in denominations:
        for j in range(coin, amount + 1):
            num_of_combinations[j] += num_of_combinations[j - coin]
    return num_of_combinations[amount]


def minimum_number_of_coins_to_make_a_total(amount, denominations):
    num_of_combinations = [0] * (amount + 1)
    num_of_combinations[0] = 0
    for i in range(amount + 1):
        minimum_num_of_coins = float('inf')
        for coin in denominations:
            if i >= coin:
                minimum_num_of_coins = min(minimum_num_of_coins, num_of_combinations[i - coin] + 1)
        num_of_combinations[i] = minimum_num_of_coins
    return num_of_combinations[amount]


# print(minimum_number_of_coins_to_make_a_total(6, [1, 2, 5]))
#
# print(minimum_number_of_coins_to_make_a_total(13, [1, 2, 5]))
#
# print(minimum_number_of_coins_to_make_a_total(17, [1, 2, 5]))
#
# print(minimum_number_of_coins_to_make_a_total(25, [1, 2, 5]))


def main():
    T = int(input())
    for t in range(T):
        N, X = map(int, input().strip().split())
        ai = list(map(int, input().strip().split()))
        if count_num_of_combinations_for_given_sum(sum(ai), ai) > 1:
            print('-1')
        else:
            total_amount = sum(ai)
            print(total_amount // X)


if __name__ == '__main__':
    main()