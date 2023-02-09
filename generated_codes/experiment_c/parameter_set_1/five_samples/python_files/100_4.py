"""


"""

import sys
def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    # check if the partial sum is equals to target
    if s == target:
        print "Yes"
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])

def main():
    number = int(sys.stdin.readline().strip())
    for i in range(number):
        temp = sys.stdin.readline().strip().split()
        number_of_wallets = int(temp[0])
        target = int(temp[1])
        temp = sys.stdin.readline().strip().split()
        list_of_wallets = []
        for i in range(len(temp)):
            list_of_wallets.append(int(temp[i]))
        subset_sum(list_of_wallets, target)

if __name__ == '__main__':
    main()