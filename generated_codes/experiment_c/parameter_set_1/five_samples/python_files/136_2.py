'''

'''
# import math
#
#
# def find_total_no_of_zombies_can_be_saved(no_of_zombies, no_of_colors):
#     return math.pow(no_of_colors, no_of_zombies)
#
#
# if __name__ == '__main__':
#     no_of_zombies, no_of_colors = map(int, input().split())
#     print(find_total_no_of_zombies_can_be_saved(no_of_zombies, no_of_colors) % (10^9 + 7))

# import math
#
#
# def find_total_no_of_zombies_can_be_saved(no_of_zombies, no_of_colors):
#     return math.pow(no_of_colors, no_of_zombies)
#
#
# if __name__ == '__main__':
#     no_of_zombies, no_of_colors = map(int, input().split())
#     print(find_total_no_of_zombies_can_be_saved(no_of_zombies, no_of_colors) % (10^9 + 7))


import math

# no_of_zombies = int(input())
# no_of_colors = int(input())

# no_of_zombies, no_of_colors = map(int, input().split())
#
# print(find_total_no_of_zombies_can_be_saved(no_of_zombies, no_of_colors))


def find_total_no_of_zombies_can_be_saved(no_of_zombies, no_of_colors):
    return math.pow(no_of_colors, no_of_zombies)


if __name__ == '__main__':
    no_of_zombies, no_of_colors = map(int, input().split())
    print(find_total_no_of_zombies_can_be_saved(no_of_zombies, no_of_colors) % (10^9 + 7))