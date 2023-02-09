"""
"""

def get_max_candies_to_buy(N, chocolate, caramel, desired_chocolate, desired_caramel):
    # Write your code here
    d = {}
    for i in range(N):
        if d.get(chocolate[i]):
            d[chocolate[i]].append(caramel[i])
        else:
            d[chocolate[i]] = [caramel[i]]
    num = 0
    min_choc = min(chocolate)
    min_caramel = min(caramel)
    while 1:
        #print('Chocolate: ' + str(desired_chocolate) + ' Caramel: ' + str(desired_caramel))
        if desired_chocolate == 0 and desired_caramel == 0:
            return num
        if desired_chocolate == 0 or desired_chocolate < min_choc:
            return -1
        if desired_caramel == 0 or desired_caramel < min_caramel:
            return -1
        if desired_chocolate == min_choc and desired_caramel == min_caramel:
            return num + 1
        max_candy_to_buy = 0
        max_choc = 0
        max_caramel = 0
        for k in d.keys():
            if k < desired_chocolate:
                for c in d[k]:
                    ch = desired_chocolate - k
                    ca = desired_caramel - c
                    if ch == 0 or ca == 0:
                        return num + 1
                    if ch > 0 and ca > 0 and ch <= min_choc and ca <= min_caramel:
                        if max_candy_to_buy < ch + ca:
                            max_candy_to_buy = ch + ca
                            max_choc = ch
                            max_caramel = ca
                        # return num + 1
        if max_candy_to_buy != 0:
            #print('Buy: ' + str(max_choc) + ' ' + str(max_caramel))
            desired_chocolate = max_choc
            desired_caramel = max_caramel
            num += 1
        else:
            return -1

N = int(input())
chocolate = []
caramel = []
for i in range(N):
    c, ca = map(int, input().split())
    chocolate.append(c)
    caramel.append(ca)
desired_chocolate, desired_caramel = map(int, input().split())
print(get_max_candies_to_buy(N, chocolate, caramel, desired_chocolate, desired_caramel))