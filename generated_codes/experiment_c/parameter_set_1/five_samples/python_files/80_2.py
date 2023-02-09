'''
'''
import collections
import sys
try:
    sys.stdin = open('input.txt','r')
    sys.stdout = open('output.txt','w')
except:
    pass

def parse(input_string):
    ip_list = input_string.split()
    if len(ip_list) == 4:
        product_id, province, sex, age = ip_list
        return 'sale', product_id, province, sex, age, 1
    elif len(ip_list) == 5:
        product_id, province, sex, age, units_sold = ip_list
        return 'sale', product_id, province, sex, age, units_sold
    else:
        product_id, province, sex, age_range = ip_list
        start_age, end_age = age_range.split('-')
        return 'query', product_id, province, sex, start_age, end_age
    

def get_total_units_sold(input_list, key, value):
    if key == 'product_id':
        if value == '-1':
            return sum([int(x[-1]) for x in input_list])
        else:
            return sum([int(x[-1]) for x in input_list if x[1] == value])
    elif key == 'province':
        if value == '-1':
            return sum([int(x[-1]) for x in input_list])
        else:
            return sum([int(x[-1]) for x in input_list if x[2] == value])
    elif key == 'sex':
        if value == '-1':
            return sum([int(x[-1]) for x in input_list])
        else:
            return sum([int(x[-1]) for x in input_list if x[3] == value])
    elif key == 'age':
        start_age, end_age = value
        return sum([int(x[-1]) for x in input_list if start_age <= x[4] <= end_age])
    else:
        return 0

def get_result(input_list, query):
    product_id, province, sex, age_range = query[1:]
    if product_id == '-1' and province == '-1' and sex == '-1' and age_range == '-1':
        return get_total_units_sold(input_list, 'all', '-1')
    if product_id == '-1':
        temp_list = input_list
    else:
        temp_list = [x for x in input_list if x[1] == product_id]
    if province == '-1':
        temp_list = temp_list
    else:
        temp_list = [x for x in temp_list if x[2] == province]
    if sex == '-1':
        temp_list = temp_list
    else:
        temp_list = [x for x in temp_list if x[3] == sex]
    if age_range == '-1':
        temp_list = temp_list
    else:
        start_age, end_age = age_range.split('-')
        temp_list = [x for x in temp_list if start_age <= x[4] <= end_age]
    return get_total_units_sold(temp_list, 'all', '-1')

def main():
    input_list = []
    queries = []
    num_inputs = int(input())
    for _ in range(num_inputs):
        parsed_input = parse(input())
        if parsed_input[0] == 'sale':
            input_list.append(parsed_input)
        else:
            queries.append(parsed_input)

    for query in queries:
        print(get_result(input_list, query))


if __name__ == '__main__':
    main()