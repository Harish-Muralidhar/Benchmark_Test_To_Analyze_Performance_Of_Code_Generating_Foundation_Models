'''

Constraints
1 <= S <= 100000
0 <= product_id <= 9
0 <= size_id <= 2
0 <= province_id <= 9
0 <= city_id <= 19
0 <= region_id <= 4
M/F
1 <= age <= 90
1 <= units_sold <= 100

'''

# Write your code here
import sys

def main():
    S = int(input())
    if 1 <= S <= 100000:
        for i in range(S):
            line = sys.stdin.readline()
            if line[0] == 'I':
                line = line.split()
                product_id = line[1].split('.')
                if len(product_id) == 1:
                    product_id.append('-1')
                province = line[2].split('.')
                if len(province) == 1:
                    province.append('-1')
                    province.append('-1')
                elif len(province) == 2:
                    province.append('-1')
                sex = line[3]
                age = line[4]
                units_sold = line[5]
                print(product_id, province, sex, age, units_sold)
            else:
                line = line.split()
                product_id = line[1].split('.')
                if len(product_id) == 1:
                    product_id.append('-1')
                province = line[2].split('.')
                if len(province) == 1:
                    province.append('-1')
                    province.append('-1')
                elif len(province) == 2:
                    province.append('-1')
                sex = line[3]
                age = line[4].split('-')
                if len(age) == 1:
                    age.append('-1')
                print(product_id, province, sex, age)
    else:
        print('Invalid input')

if __name__ == '__main__':
    main()