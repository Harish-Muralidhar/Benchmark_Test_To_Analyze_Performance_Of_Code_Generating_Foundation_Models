"""


"""

# from itertools import combinations

# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s.remove(a)
#                 s.remove(b)
#                 s.append(abs(a - b))
#             if s[0] == 1:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))

# from itertools import combinations

# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s = [abs(a - b)]
#             if s[0] == 1:
#                 count += 1
#     return count

#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))


# from itertools import combinations


# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s = [abs(a - b)]
#             if s[0] == 1:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))
#
#
#
# from itertools import combinations


# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s = [abs(a - b)]
#             if s[0] == 1:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))
#
#
#
# from itertools import combinations


# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s = [abs(a - b)]
#             if s[0] == 1:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))


# from itertools import combinations


# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s = [abs(a - b)]
#             if s[0] == 1:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))


# from itertools import combinations
#
#
# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s = [abs(a - b)]
#             if s[0] == 1:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))


# from itertools import combinations
#
#
# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s = [abs(a - b)]
#             if s[0] == 1:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))
#
#
# from itertools import combinations
#
#
# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s = [abs(a - b)]
#             if s[0] == 1:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))
#
#
# from itertools import combinations
#
#
# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s = [abs(a - b)]
#             if s[0] == 1:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))


# from itertools import combinations
#
#
# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s = [abs(a - b)]
#             if s[0] == 1:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))


# from itertools import combinations
#
#
# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s = [abs(a - b)]
#             if s[0] == 1:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))


# from itertools import combinations
#
#
# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s = [abs(a - b)]
#             if s[0] == 1:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))
#
#
# from itertools import combinations
#
#
# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s = [abs(a - b)]
#             if s[0] == 1:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))
#
#
# from itertools import combinations
#
#
# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s = [abs(a - b)]
#             if s[0] == 1:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))
#
#
#
# from itertools import combinations
#
#
# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s = [abs(a - b)]
#             if s[0] == 1:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))
#
#
# from itertools import combinations
#
#
# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s = [abs(a - b)]
#             if s[0] == 1:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))
#
#
#
# from itertools import combinations
#
#
# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))
#                 a, b = s[0], s[-1]
#                 s = [abs(a - b)]
#             if s[0] == 1:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#         print(get_solution(n, nums))
#
#
# from itertools import combinations
#
#
# def get_solution(n, nums):
#     count = 0
#     for i in range(1, n + 1):
#         for s in combinations(nums, i):
#             flag = True
#             while len(set(s)) > 1:
#                 s = list(set(s))