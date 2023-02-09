"""

"""

import fileinput

def get_provinces():
    return {x: dict() for x in range(10)}

def get_cities():
    return {x: dict() for x in range(20)}

def get_regions():
    return {x: dict() for x in range(5)}

def get_ages():
    return {x: 0 for x in range(1, 91)}

def get_sizes():
    return {x: dict() for x in range(3)}

def get_genders():
    return {'M': dict(), 'F': dict()}

provinces = get_provinces()

for line in fileinput.input():
    line = line.strip()
    if fileinput.isfirstline():
        continue

    if line[0] == 'I':
        _, product_id, province_id, gender, age, units_sold = line.split(' ')
        product_id, size_id = product_id.split('.')
        size_id = int(size_id)
        province_id, city_id, region_id = [int(i) for i in province_id.split('.')]
        age = int(age)
        units_sold = int(units_sold)
        if province_id not in provinces:
            provinces[province_id] = get_cities()
        cities = provinces[province_id]

        if city_id not in cities:
            cities[city_id] = get_regions()
        regions = cities[city_id]

        if region_id not in regions:
            regions[region_id] = {product_id: {size_id: {'ages': get_ages(), 'genders': get_genders()}}}
        products = regions[region_id]

        if product_id not in products:
            products[product_id] = {size_id: {'ages': get_ages(), 'genders': get_genders()}}
        sizes = products[product_id]

        if size_id not in sizes:
            sizes[size_id] = {'ages': get_ages(), 'genders': get_genders()}
        age_dict = sizes[size_id]['ages']

        if age not in age_dict:
            age_dict[age] = 0
        gender_dict = sizes[size_id]['genders']

        if gender not in gender_dict:
            gender_dict[gender] = get_ages()
        genders_age_dict = gender_dict[gender]

        if age not in genders_age_dict:
            genders_age_dict[age] = 0
        genders_age_dict[age] += units_sold
        age_dict[age] += units_sold
    else:
        _, product_id, province_id, gender, start_age, end_age = line.split(' ')
        start_age = int(start_age)
        end_age = int(end_age)
        product_id, size_id = product_id.split('.')
        size_id = int(size_id)
        province_id, city_id, region_id = [int(i) for i in province_id.split('.')]
        unit_count = 0

        if province_id != -1:
            province_data = provinces[province_id]
            if city_id != -1:
                city_data = province_data[city_id]
                if region_id != -1:
                    region_data = city_data[region_id]
                    if product_id != -1:
                        product_data = region_data[product_id]
                        if size_id != -1:
                            product_data = product_data[size_id]
                            unit_count += sum(product_data['genders'][gender].values())
                        else:
                            for size_id, product_data in product_data.items():
                                unit_count += sum(product_data['genders'][gender].values())
                    else:
                        for product_id, product_data in region_data.items():
                            if size_id != -1:
                                product_data = product_data[size_id]
                                unit_count += sum(product_data['genders'][gender].values())
                            else:
                                for size_id, product_data in product_data.items():
                                    unit_count += sum(product_data['genders'][gender].values())
                else:
                    for region_id, region_data in city_data.items():
                        if product_id != -1:
                            product_data = region_data[product_id]
                            if size_id != -1:
                                product_data = product_data[size_id]
                                unit_count += sum(product_data['genders'][gender].values())
                            else:
                                for size_id, product_data in product_data.items():
                                    unit_count += sum(product_data['genders'][gender].values())
                        else:
                            for product_id, product_data in region_data.items():
                                if size_id != -1:
                                    product_data = product_data[size_id]
                                    unit_count += sum(product_data['genders'][gender].values())
                                else:
                                    for size_id, product_data in product_data.items():
                                        unit_count += sum(product_data['genders'][gender].values())
            else:
                for city_id, city_data in province_data.items():
                    if region_id != -1:
                        region_data = city_data[region_id]
                        if product_id != -1:
                            product_data = region_data[product_id]
                            if size_id != -1:
                                product_data = product_data[size_id]
                                unit_count += sum(product_data['genders'][gender].values())
                            else:
                                for size_id, product_data in product_data.items():
                                    unit_count += sum(product_data['genders'][gender].values())
                        else:
                            for product_id, product_data in region_data.items():
                                if size_id != -1:
                                    product_data = product_data[size_id]
                                    unit_count += sum(product_data['genders'][gender].values())
                                else:
                                    for size_id, product_data in product_data.items():
                                        unit_count += sum(product_data['genders'][gender].values())
                    else:
                        for region_id, region_data in city_data.items():
                            if product_id != -1:
                                product_data = region_data[product_id]
                                if size_id != -1:
                                    product_data = product_data[size_id]
                                    unit_count += sum(product_data['genders'][gender].values())
                                else:
                                    for size_id, product_data in product_data.items():
                                        unit_count += sum(product_data['genders'][gender].values())
                            else:
                                for product_id, product_data in region_data.items():
                                    if size_id != -1:
                                        product_data = product_data[size_id]
                                        unit_count += sum(product_data['genders'][gender].values())
                                    else:
                                        for size_id, product_data in product_data.items():
                                            unit_count += sum(product_data['genders'][gender].values())
        else:
            for province_id, province_data in provinces.items():
                if city_id != -1:
                    city_data = province_data[city_id]
                    if region_id != -1:
                        region_data = city_data[region_id]
                        if product_id != -1:
                            product_data = region_data[product_id]
                            if size_id != -1:
                                product_data = product_data[size_id]
                                unit_count += sum(product_data['genders'][gender].values())
                            else:
                                for size_id, product_data in product_data.items():
                                    unit_count += sum(product_data['genders'][gender].values())
                        else:
                            for product_id, product_data in region_data.items():
                                if size_id != -1:
                                    product_data = product_data[size_id]
                                    unit_count += sum(product_data['genders'][gender].values())
                                else:
                                    for size_id, product_data in product_data.items():
                                        unit_count += sum(product_data['genders'][gender].values())
                    else:
                        for region_id, region_data in city_data.items():
                            if product_id != -1:
                                product_data = region_data[product_id]
                                if size_id != -1:
                                    product_data = product_data[size_id]
                                    unit_count += sum(product_data['genders'][gender].values())
                                else:
                                    for size_id, product_data in product_data.items():
                                        unit_count += sum(product_data['genders'][gender].values())
                            else:
                                for product_id, product_data in region_data.items():
                                    if size_id != -1:
                                        product_data = product_data[size_id]
                                        unit_count += sum(product_data['genders'][gender].values())
                                    else:
                                        for size_id, product_data in product_data.items():
                                            unit_count += sum(product_data['genders'][gender].values())
                else:
                    for city_id, city_data in province_data.items():
                        if region_id != -1:
                            region_data = city_data[region_id]
                            if product_id != -1:
                                product_data = region_data[product_id]
                                if size_id != -1:
                                    product_data = product_data[size_id]
                                    unit_count += sum(product_data['genders'][gender].values())
                                else:
                                    for size_id, product_data in product_data.items():
                                        unit_count += sum(product_data['genders'][gender].values())
                            else:
                                for product_id, product_data in region_data.items():
                                    if size_id != -1:
                                        product_data = product_data[size_id]
                                        unit_count += sum(product_data['genders'][gender].values())
                                    else:
                                        for size_id, product_data in product_data.items():
                                            unit_count += sum(product_data['genders'][gender].values())
                        else:
                            for region_id, region_data in city_data.items():
                                if product_id != -1:
                                    product_data = region_data[product_id]
                                    if size_id != -1:
                                        product_data = product_data[size_id]
                                        unit_count += sum(product_data['genders'][gender].values())
                                    else:
                                        for size_id, product_data in product_data.items():
                                            unit_count += sum(product_data['genders'][gender].values())
                                else:
                                    for product_id, product_data in region_data.items():
                                        if size_id != -1:
                                            product_data = product_data[size_id]
                                            unit_count += sum(product_data['genders'][gender].values())
                                        else:
                                            for size_id, product_data in product_data.items():
                                                unit_count += sum(product_data['genders'][gender].values())
        print(unit_count)