"""



Explanation

In the first test case, the Chef has prepared 4 appetizers numbered 0 to 3. The appetizers are arrayed in the order "chef" and the Chef writes the numbers "00", "01", "10", and "11" on pieces of paper. The servers read the numbers upside down and place the appetizers in the order "cehf".


In the second test case, the Chef has prepared 16 appetizers numbered 0 to 15. The appetizers are arrayed in the order "enjoyourapplepie" and the Chef writes the numbers "0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", and "1111" on pieces of paper. The servers read the numbers upside down and place the appetizers in the order "eayejpuinpopolre".

"""

# cook your dish here

import math

def main():
    t = int(input())
    for i in range(t):
        k, s = input().split()
        k = int(k)
        n = int(math.pow(2, k))
        l = []
        for j in range(n):
            l.append(s[j])
        for j in range(n):
            num = bin(j)[2:]
            num = num.rjust(k, '0')
            num = num[::-1]
            num = int(num, 2)
            print(l[num], end='')
        print()

if __name__ == '__main__':
    main()