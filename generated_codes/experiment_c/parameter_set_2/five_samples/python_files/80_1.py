'''

Constraints
1 <= S <= 100000
0 <= product_id <= 9
0 <= size_id <= 2
0 <= province_id <= 9
0 <= city_id <= 19
0 <= region_id <= 4
0 <= units_sold <= 100
1 <= age <= 90

'''

import sys

def main():
    '''
    Write your code here.
    '''
    n = int(input())
    dic = {}
    for i in range(n):
        inp = input().split()
        if inp[0] == 'I':
            if inp[1] == '-1':
                if inp[2] == '-1':
                    if inp[3] == 'M':
                        if inp[4] == '1-90':
                            if 'M' not in dic:
                                dic['M'] = int(inp[5])
                            else:
                                dic['M'] += int(inp[5])
                        else:
                            if inp[4] not in dic:
                                dic[inp[4]] = int(inp[5])
                            else:
                                dic[inp[4]] += int(inp[5])
                    else:
                        if inp[4] == '1-90':
                            if 'F' not in dic:
                                dic['F'] = int(inp[5])
                            else:
                                dic['F'] += int(inp[5])
                        else:
                            if inp[4] not in dic:
                                dic[inp[4]] = int(inp[5])
                            else:
                                dic[inp[4]] += int(inp[5])
                else:
                    if inp[3] == 'M':
                        if inp[4] == '1-90':
                            if inp[2] not in dic:
                                dic[inp[2]] = {}
                                dic[inp[2]]['M']