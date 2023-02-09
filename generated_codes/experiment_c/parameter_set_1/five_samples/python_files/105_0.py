"""


Explanation of sample input
    First case in sample input is equivalent to the binary 11011. So, 27 is the required output.
    Second case in sample input is equivalent to the binary 1. Hence, 1 is the required output.

"""


import sys
import re


def to_binary(n):
    binary = ""
    while n != 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary


def to_decimal(binary):
    decimal = 0
    for i, b in enumerate(binary):
        decimal += 2**i * int(b)
    return decimal


def convert_to_decimal(input_1base):
    flag = 1
    binary = ""
    for block in input_1base.split():
        if block == "0":
            binary += "1"
            flag = 1
        elif block == "00":
            flag = 0
        else:
            binary += to_binary(int(block) - 2) * flag
    return to_decimal(binary)

def main():
    for line in sys.stdin:
        line = line.strip()
        if re.match(r'#', line):
            yield convert_to_decimal(line[:-1])
        elif re.match(r'~', line):
            break
        else:
            yield convert_to_decimal(line)


if __name__ == '__main__':
    for result in main():
        print(result)