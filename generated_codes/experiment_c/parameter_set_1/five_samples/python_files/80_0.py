'''

Solution

'''
x = int(input())
y = 0
wei = []
while y != x:
    wei.append(input().split())
    y += 1

print(wei)
# print(wei[0][0])
# print(wei[1][0])

# print(wei[0][1])
# print(wei[1][1])

# print(wei[0][2])
# print(wei[1][2])

# print(wei[0][3])
# print(wei[1][3])

# print(wei[0][4])
# print(wei[1][4])

for i in range(0, x):
    # print(i)
    if wei[i][0] == 'I':
        if wei[i][1].find(".") == -1:
            product_id = wei[i][1]
            size_id = '-1'
        else:
            a = wei[i][1].split(".")
            product_id = a[0]
            size_id = a[1]
        if wei[i][2].find(".") == -1:
            province = wei[i][2]
            city_id = '-1'
            region_id = '-1'
        elif wei[i][2].count(".") == 1:
            b = wei[i][2].split(".")
            province = b[0]
            city_id = b[1]
            region_id = '-1'
        else:
            c = wei[i][2].split(".")
            province = c[0]
            city_id = c[1]
            region_id = c[2]
        sex = wei[i][3]
        age = wei[i][4]
        units_sold = wei[i][5]

    elif wei[i][0] == 'Q':
        if wei[i][1].find(".") == -1:
            product_id = wei[i][1]
            size_id = '-1'
        else:
            a = wei[i][1].split(".")
            product_id = a[0]
            size_id = a[1]
        if wei[i][2].find(".") == -1:
            province = wei[i][2]
            city_id = '-1'
            region_id = '-1'
        elif wei[i][2].count(".") == 1:
            b = wei[i][2].split(".")
            province = b[0]
            city_id = b[1]
            region_id = '-1'
        else:
            c = wei[i][2].split(".")
            province = c[0]
            city_id = c[1]
            region_id = c[2]
        sex = wei[i][3]
        age = wei[i][4]
        units_sold = wei[i][5]

'''

# print(product_id)
# print(size_id)
# print(province)
# print(city_id)
# print(region_id)
# print(sex)
# print(age)
# print(units_sold)

# print(wei[2][1].split("."))

# print(wei[0][1].find("."))
# print(wei[1][1].find("."))
# print(wei[2][1].find("."))