'''

Note: Your code should be able to convert the sample input into the sample output. However, this is not enough to pass the challenge, because the code will be run on multiple test cases. Therefore, your code must solve this problem statement.

'''
def check_smallest_group(x,dishes_list,clans_list):
    # print(x,dishes_list,clans_list)
    dishes_list.sort()
    clans_list.sort()
    # print(x,dishes_list,clans_list)
    # print(len(dishes_list),len(clans_list))
    if len(dishes_list) == 0 and len(clans_list) == 0:
        return 1
    if len(dishes_list) == 0 and len(clans_list) != 0:
        return clans_list[0][1]
    if len(clans_list) == 0 and len(dishes_list) != 0:
        return dishes_list[0][1]
    if len(clans_list) != 0 and len(dishes_list) != 0:
        if clans_list[0][0] < dishes_list[0][0]:
            if clans_list[0][1] <= dishes_list[0][1]:
                return 1
            else:
                clans_list.pop(0)
                return check_smallest_group(x,dishes_list,clans_list)
        else:
            if dishes_list[0][1] <= clans_list[0][1]:
                return 1
            else:
                dishes_list.pop(0)
                return check_smallest_group(x,dishes_list,clans_list)
        

if __name__ == "__main__":
    # print(check_smallest_group(10,[(2,5),(8,1)],[(1,1,1),(4,3,2),(9,1,1)]))
    t = int(input())
    for i in range(t):
        x = int(input())
        dishes_num = int(input())
        dishes_list = []
        for j in range(dishes_num):
            dishes_list.append(tuple(map(int,input().split())))
        clans_num = int(input())
        clans_list = []
        for j in range(clans_num):
            clans_list.append(tuple(map(int,input().split())))
        print(check_smallest_group(x,dishes_list,clans_list))