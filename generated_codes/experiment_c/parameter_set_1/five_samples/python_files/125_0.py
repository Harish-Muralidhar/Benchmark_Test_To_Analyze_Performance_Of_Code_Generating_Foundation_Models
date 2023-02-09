"""
Example case 2. Game will have 2 turns. In the first turn Sasha will choose 4, while Chef will choose 3. In the second turn Sasha will choose 1, while Chef will choose 4. Hence answer is 1.5.
Example case 3. In both turns Sasha will choose 2 and chef will choose 2. Hence answer is 0.0.

"""

# Write your code here
def main():

    test_cases = int(input())
    for _ in range(test_cases):
        N = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        a_sum = 0
        b_sum = 0

        for i in a:
            a_sum += (1/i)
        for i in b:
            b_sum += (1/i)

        result = 1 / (a_sum*b_sum)
        print("{:.6f}".format(result))

if __name__ == '__main__':
    main()