"""



Time Limit : 100000 ms


"""


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def add_fractions(a, b):
    return a[0] * b[1] + b[0] * a[1], a[1] * b[1]


def lcm(a, b):
    return a * b // gcd(a, b)


def solve(fractions):
    fractions = [fraction.split("/") for fraction in fractions]
    fractions = [[int(x) for x in fraction] for fraction in fractions]

    max_numerators = [fractions[0][0]]
    max_denominators = [max_numerators[0] + fractions[0][1]]

    for i in range(1, len(fractions)):
        numerator, denominator = fractions[i]

        new_numerator = numerator + max_numerators[i - 1]
        new_denominator = denominator + max_denominators[i - 1]

        common_divisor = gcd(new_numerator, new_denominator)
        max_numerators.append(new_numerator // common_divisor)
        max_denominators.append(new_denominator // common_divisor)

    return ["{}/{}".format(numerator, denominator) for numerator, denominator in zip(max_numerators, max_denominators)]


def main():
    num_test_cases = int(input())

    for _ in range(num_test_cases):
        num_fractions = int(input())

        fractions = []

        for _ in range(num_fractions):
            fractions.append(input())

        print("\n".join(solve(fractions)))


if __name__ == "__main__":
    main()