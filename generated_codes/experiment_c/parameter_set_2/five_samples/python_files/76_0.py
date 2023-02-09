"""

"""

def get_min_people(x, b, c, dishes, clans):
    #print(x, b, c, dishes, clans)
    if b == 0:
        if c == 0:
            return 0
        else:
            min_people = x
            for i in range(c):
                if clans[i][1] <= min_people:
                    min_people += clans[i][2]
            return min_people
    else:
        min_people = dishes[0][1]
        for i in range(b):
            if dishes[i][1] <= min_people:
                min_people = dishes[i][1]
        for i in range(c):
            if clans[i][1] <= min_people:
                min_people += clans[i][2]
        return min_people

def get_clans_count(x, b, c, dishes, clans):
    if b == 0:
        return 0
    else:
        min_people = dishes[0][1]
        for i in range(b):
            if dishes[i][1] <= min_people:
                min_people = dishes[i][1]
        clans_count = 0
        for i in range(c):
            if clans[i][1] <= min_people:
                clans_count += 1
        return clans_count

def get_dishes_count(x, b, c, dishes, clans):
    if b == 0:
        return 0
    else:
        min_people = dishes[0][1]
        for i in range(b):
            if dishes[i][1] <= min_people:
                min_people = dishes[i][1]
        dishes_count = 0
        for i in range(b):
            if dishes[i][1] <= min_people:
                dishes_count += 1
        return dishes_count

def get_min_people_with_clans(x, b, c, dishes, clans):
    if b == 0:
        return 0
    else:
        min_people = dishes[0][1]