'''
'''

def ordering(item_list):
    item_list.sort()
    index = 0
    price_list = []
    while index < len(item_list):
        if index+2 < len(item_list) and item_list[index] == item_list[index+1] == item_list[index+2]:
            price_list.append(item_list[index+1] + item_list[index])
            index += 3
        else:
            price_list.append(item_list[index])
            index += 1
    return sum(price_list)

if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        item_count = int(input())
        item_list = list(map(int, input().strip().split()))
        print (ordering(item_list))