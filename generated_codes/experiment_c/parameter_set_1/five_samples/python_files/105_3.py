"""

"""

import sys

def onebase_to_decimal(onebase):
    """
    Input: 
        onebase - a string representing a 1-base number
    Output:
        Returns the decimal value of the 1-base number
    """
    # Your code here
    onebase = onebase.replace(' ','')
    decimal = 0
    flag = 1
    temp = ''
    
    for i in range(len(onebase)):
        if onebase[i] == '0':
            temp += '0'
            if len(temp) == 2:
                flag = 0
                temp = ''
        elif onebase[i] == '1':
            if flag:
                decimal += 2 ** (len(temp) - 1)
            else:
                decimal += int('1' + '0' * (len(temp) - 2),2)
            flag = 1
            temp = ''
    return decimal

def main():
    # input 1-base number
    onebase = ''
    for line in sys.stdin:
        if line.strip() == '#':
            print(onebase_to_decimal(onebase))
            onebase = ''
        elif line.strip() == '~':
            break
        else:
            onebase += line.strip()

if __name__ == '__main__':
    main()