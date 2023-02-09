'''

'''

def can_be_combined(c1, c2, desired, factor):
    if c1[0] * c1[1] * factor * c2[1] == c2[0] * c2[1] * factor * c1[1]:
        return True
    return False

def get_ratio(c1, c2, desired, factor):
    ratio = (c1[0] * factor * c2[1] + c2[0] * factor * c1[1]) / (c1[1] * factor * c2[1])
    return ratio

def find_min_candies(candies, desired):
    min_candies = len(candies)
    for i in range(len(candies)):
        for j in range(i + 1, len(candies)):
            if candies[i][0] > candies[j][0]:
                c1, c2 = candies[j], candies[i]
            else:
                c1, c2 = candies[i], candies[j]
            factor = 1
            while True:
                if can_be_combined(c1, c2, desired, factor):
                    if get_ratio(c1, c2, desired, factor) == desired[0] / desired[1]:
                        min_candies = min(min_candies, 2)
                    break
                factor += 1
    return min_candies

def main():
    N = int(input())
    candies = list()
    for _ in range(N):
        chocolate, caramel = list(map(int, input().split()))
        candies.append((chocolate, caramel))
    desiredChocolate, desiredCaramel = list(map(int, input().split()))
    desired = (desiredChocolate, desiredCaramel)
    min_candies = find_min_candies(candies, desired)
    if min_candies == len(candies):
        print(-1)
    else:
        print(min_candies)

if __name__ == '__main__':
    main()