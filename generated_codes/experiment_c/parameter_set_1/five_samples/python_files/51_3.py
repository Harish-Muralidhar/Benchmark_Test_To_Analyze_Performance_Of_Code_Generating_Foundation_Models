'''


Explanation
For test case 1, the minimum bonus that can be given is 460$. A possible way is giving bonus of 140, 100, 120, 100$.
For test case 2, if employee 1 gets more bonus than employee 2, then employee 2 should get more bonus than employee 3, which is not possible. So, the analysis is inconsistent.

'''

import itertools


def check_inconsistent(pairs, allowed_pairs):
    for pair in pairs:
        employee1, employee2 = pair[0], pair[1]
        if not (employee1, employee2) in allowed_pairs and not (employee2, employee1) in allowed_pairs:
            return True
    return False


def get_bonus(employee_count, comparison_count, minimum_bonus, comparisons, allowed_pairs):
    pairs = list(itertools.combinations(range(employee_count), 2))
    if check_inconsistent(pairs, allowed_pairs):
        return "Inconsistent analysis."
    # print(pairs)
    results = [minimum_bonus] * employee_count
    while len(pairs) > 0:
        new_pairs = []
        for pair in pairs:
            employee1, employee2 = pair[0], pair[1]
            if employee1 > employee2:
                employee1, employee2 = employee2, employee1
            if employee1 in allowed_pairs[(employee1, employee2)]:
                if results[employee1] < results[employee2] + comparisons[(employee1, employee2)]:
                    results[employee1] = results[employee2] + comparisons[(employee1, employee2)]
            else:
                new_pairs.append(pair)
        pairs = new_pairs
    # print(results)
    return sum(results)


def main():
    test_case_count = int(input())
    for i in range(test_case_count):
        employee_count, comparison_count, minimum_bonus = map(int, input().split())
        comparisons = {}
        allowed_pairs = {}
        for j in range(comparison_count):
            employee1, employee2, bonus = map(int, input().split())
            comparisons[(employee1 - 1, employee2 - 1)] = bonus
            allowed_pairs[(employee1 - 1, employee2 - 1)] = [employee1 - 1]
        print(get_bonus(employee_count, comparison_count, minimum_bonus, comparisons, allowed_pairs))


if __name__ == '__main__':
    main()