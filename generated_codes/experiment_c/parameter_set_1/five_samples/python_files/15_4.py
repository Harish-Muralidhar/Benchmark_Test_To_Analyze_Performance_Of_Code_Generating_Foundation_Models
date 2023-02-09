'''
Example 3 : Cops at house 10 can cover houses 1 to 51, cops at house 51 can cover houses 35 to 81. So, there are 9 safe houses.
'''
import math

def cal_safe_house(max_cop_speed, max_time, cop_house_list):

    for(i, house_no) in enumerate(cop_house_list):
        start = house_no - 1
        end = house_no + max_cop_speed * max_time - 1
        cop_house_list[i] = [start, end]

    safe_house_list = []
    for house_no in range(1, 101):
        is_safe = True
        for house_range in cop_house_list:
            if house_no >= house_range[0] and house_no <= house_range[1]:
                is_safe = False
                break
        if is_safe:
            safe_house_list.append(house_no)

    return safe_house_list

if __name__ == '__main__':
    TOTAL_TEST_CASE = int(input())
    TEST_CASE_LIST = []
    for i in range(TOTAL_TEST_CASE):
        max_cop_speed, max_time, total_cop = [int(x) for x in input().split()]
        cop_house_list = [int(x) for x in input().split()]
        TEST_CASE_LIST.append([max_cop_speed, max_time, cop_house_list])

    for test_case in TEST_CASE_LIST:
        max_cop_speed = test_case[0]
        max_time = test_case[1]
        cop_house_list = test_case[2]
        print(len(cal_safe_house(max_cop_speed, max_time, cop_house_list)))