'''


https://www.codechef.com/problems/EMILYG
'''

from itertools import combinations


def is_sum_to_k_multiple_possbile(num_arr, num_packs, k):
    if any(sum(candies_set) % k != 0 for candies_set in combinations(num_arr, num_packs)):
        return -1
    return min(sum(candies_set) for candies_set in combinations(num_arr, num_packs))


def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        num_packs, num_friends, k = map(int, input().strip().split())
        num_arr = list(map(int, input().strip().split()))
        print(is_sum_to_k_multiple_possbile(num_arr, num_packs, k))


if __name__ == '__main__':
    main()