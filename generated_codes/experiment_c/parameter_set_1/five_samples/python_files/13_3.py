"""

Explanation

The first test case is depicted below. The second test case is the same except the value of R is 2 instead of 1.



In the third test case, the Chef and the head server are too far away to communicate directly. If they could communicate with the sous-chef, then the sous-chef could relay the Chef's message to the head server. However, the sous-chef and the head server are too far away for this to work. There is no way for all three to communicate with each other.



https://www.codechef.com/problems/TWOVSTEN
"""
from math import sqrt


def is_team_in_contact(chef, server_head, sous_chef, transceiver_range):
    chef_to_server_head_distance = sqrt(
        (chef['x'] - server_head['x']) ** 2 + (chef['y'] - server_head['y']) ** 2
    )
    chef_to_sous_chef_distance = sqrt(
        (chef['x'] - sous_chef['x']) ** 2 + (chef['y'] - sous_chef['y']) ** 2
    )
    server_head_to_sous_chef_distance = sqrt(
        (server_head['x'] - sous_chef['x']) ** 2 + (server_head['y'] - sous_chef['y']) ** 2
    )

    if chef_to_server_head_distance <= transceiver_range and chef_to_sous_chef_distance <= transceiver_range:
        return True
    elif server_head_to_sous_chef_distance <= transceiver_range and chef_to_sous_chef_distance <= transceiver_range:
        return True
    elif server_head_to_sous_chef_distance <= transceiver_range and chef_to_server_head_distance <= transceiver_range:
        return True

    return False


def main():
    transceiver_range = int(input())
    chef = {'x': int(input()), 'y': int(input())}
    server_head = {'x': int(input()), 'y': int(input())}
    sous_chef = {'x': int(input()), 'y': int(input())}

    print('yes' if is_team_in_contact(chef, server_head, sous_chef, transceiver_range) else 'no')


if __name__ == '__main__':
    main()