'''

It is guaranteed that there will be no more than 50 queries.

'''

# Write your code for the above question here
import sys
#print(sys.version)

#S = int(input())
S = int(sys.argv[1])

class Sales(object):
    def __init__(self,product_id,size_id,province_id,city_id,region_id,sex,age,unit):
        self.product_id = product_id
        self.size_id = size_id
        self.province_id = province_id
        self.city_id = city_id
        self.region_id = region_id
        self.sex = sex
        self.age = age
        self.unit = unit

    def __str__(self):
        return "Product Id: {} Size Id: {} Province Id: {} City Id: {} Region Id: {} Sex: {} Age: {} Unit Sold: {}".format(self.product_id, self.size_id, self.province_id, self.city_id, self.region_id, self.sex, self.age, self.unit)


def get_input(S):
    sales_list = []
    for i in range(S):
        inp = sys.argv[i+2]
        if inp[0] == 'I':
            inp_list = inp.split(' ')
            product_id, size_id, province_id, city_id, region_id, sex, age, unit = get_sales_details(inp_list)
            sales_list.append(Sales(product_id, size_id, province_id, city_id, region_id, sex, age, unit))
        else:
            inp_list = inp.split(' ')
            product_id, size_id, province_id, city_id, region_id, sex, age = get_query_details(inp_list)
            total_units = get_total_units_sold(sales_list, product_id, size_id, province_id, city_id, region_id, sex, age)
            print(total_units)

def get_total_units_sold(sales_list, product_id, size_id, province_id, city_id, region_id, sex, age):
    total_units = 0
    for sales in sales_list:
        if ((product_id == sales.product_id or product_id == -1) and
            (size_id == sales.size_id or size_id == -1) and
            (province_id == sales.province_id or province_id == -1) and
            (city_id == sales.city_id or city_id == -1) and
            (region_id == sales.region_id or region_id == -1) and
            (sex == sales.sex or sex == 'N') and
            (age[0] <= sales.age <= age[1])):
            total_units += sales.unit
    return total_units

def get_sales_details(inp_list):
    product_id, size_id, province_id, city_id, region_id, sex, age, unit = '','','','','','','',''
    if inp_list[1].find('.') != -1:
        product_id, size_id = inp_list[1].split('.')
        product_id = int(product_id)
        size_id = int(size_id)
    else:
        product_id = int(inp_list[1])
    if inp_list[2].find('.') != -1:
        province_id, city_id = inp_list[2].split('.')
        province_id = int(province_id)
        if city_id.find('.') != -1:
            city_id, region_id = city_id.split('.')
            city_id = int(city_id)
            region_id = int(region_id)
        else:
            city_id = int(city_id)
    else:
        province_id = int(inp_list[2])
    sex = inp_list[3]
    age = int(inp_list[4])
    unit = int(inp_list[5])
    return product_id, size_id, province_id, city_id, region_id, sex, age, unit

def get_query_details(inp_list):
    product_id, size_id, province_id, city_id, region_id, sex, age = '','','','','','',''
    if inp_list[1].find('.') != -1:
        product_id, size_id = inp_list[1].split('.')
        product_id = int(product_id)
        size_id = int(size_id)
    else:
        product_id = int(inp_list[1])
    if inp_list[2].find('.') != -1:
        province_id, city_id = inp_list[2].split('.')
        province_id = int(province_id)
        if city_id.find('.') != -1:
            city_id, region_id = city_id.split('.')
            city_id = int(city_id)
            region_id = int(region_id)
        else:
            city_id = int(city_id)
    else:
        province_id = int(inp_list[2])
    sex = inp_list[3]
    if inp_list[4].find('-') != -1:
        age_range = inp_list[4].split('-')
        age = [int(age_range[0]), int(age_range[1])]
    else:
        age = int(inp_list[4])
    return product_id, size_id, province_id, city_id, region_id, sex, age

if __name__ == '__main__':
    get_input(S)