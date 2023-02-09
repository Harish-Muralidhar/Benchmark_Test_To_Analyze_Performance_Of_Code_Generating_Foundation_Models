'''

'''

def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)

class candy_flavours:
    def __init__(self, choc, car):
        self.choc = choc
        self.car = car
        self.ratio = choc/car
        self.gcd = gcd(choc, car) 
    def __eq__(self, other):
        if self.ratio == other.ratio:
            return True
        else: return False
    def __lt__(self, other):
        if self.ratio < other.ratio:
            return True
        else: return False
    def __gt__(self, other):
        if self.ratio > other.ratio:
            return True
        else: return False
    def __add__(self, other):
        if self.ratio == other.ratio:
            return candy_flavours(self.choc + other.choc, self.car + other.car)
        else: return None
    def __str__(self):
        return "Candy with Ratio:{} and GCD: {}".format(self.ratio, self.gcd)

def candies_to_buy(candy_list, total_choc, total_car):
    candy_list.sort()
    for index, candy in enumerate(candy_list):
        if index != 0:
            if candy.ratio == candy_list[index-1].ratio:
                candy_list[index] = candy_list[index-1] + candy
                candy_list.pop(index-1)
    # print(candy_list)
    count = 0
    while len(candy_list) > 0:
        if candy_list[0].choc == total_choc and candy_list[0].car == total_car:
            count += 1
            break
        if candy_list[0].choc == total_choc:
            candy_list.pop(0)
        elif candy_list[0].choc > total_choc:
            count += 1
            total_choc = total_choc + candy_list[0].choc
        else:
            total_choc = total_choc - candy_list[0].choc
            count += 1

    # print(count)
    return count

if __name__ == '__main__':
    a = candy_flavours(2, 3)
    b = candy_flavours(4, 6)
    c = candy_flavours(10, 15)
    d = candy_flavours(5, 8)
    print(candies_to_buy([a,b,c,d], 5, 8))