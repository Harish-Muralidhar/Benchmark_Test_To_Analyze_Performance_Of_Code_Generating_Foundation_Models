"""

Explanation

In the first case, the Chef created 4 appetizers numbered 0 to 3. He wrote the numbers in binary, padded with zeros to make 2 bits. The numbers are "00", "01", "10", and "11". When read upside down, the numbers are "00", "10", "01", and "11". The Chef placed the appetizers on the counter in the order they were finished, with the number written beside them. The servers retrieved the appetizers and placed them in the order indexed by the binary number read upside down. Thus, the appetizers are placed in the order "00", "10", "01", and "11". The message displayed is "cehf".

In the second case, the Chef created 16 appetizers numbered 0 to 15. He wrote the numbers in binary, padded with zeros to make 4 bits. The numbers are "0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", and "1111". When read upside down, the numbers are "0000", "1000", "0100", "1100", "0010", "1010", "0110", "1110", "0001", "1001", "0101", "1101", "0011", "1011", "0111", and "1111". The Chef placed the appetizers on the counter in the order they were finished, with the number written beside them. The servers retrieved the appetizers and placed them in the order indexed by the binary number read upside down. Thus, the appetizers are placed in the order "0000", "1000", "0010", "1010", "0001", "1001", "0011", "1011", "0100", "1100", "0110", "1110", "0101", "1101", "0111", and "1111". The message displayed is "eayejpuinpopolre".

"""

def main():
    t = int(input())
    for i in range(t):
        k,s = input().split()
        k = int(k)
        n = 2**k
        s = list(s)
        for i in range