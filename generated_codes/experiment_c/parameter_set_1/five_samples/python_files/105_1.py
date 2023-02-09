"""

    
    Explanation 
    In the first case, the given 1-based number is equivalent to 11011 in binary number system. Converting it to decimal, we get the value 27.
    In the second case the binary value is 01. Converting it to decimal, we get 1.

"""
import sys
def one_base(n):
    flag = 1
    binr = 0
    for i in range(len(n)):
        if len(n[i]) == 1 and n[i][0] == 0:
            flag = 1
            continue
        elif len(n[i]) == 2:
            flag = 0
            continue
        else:
            binr = binr * 2**(len(n[i])-2) + flag * (2**(len(n[i])-2)-1)
            flag = 0
    return binr

def main():
    for line in sys.stdin:
        line = line.strip()
        if line == "~":
            break
        n = line.split()
        while True:
            l = sys.stdin.readline()
            l = l.strip()
            if l[-1] == "#":
                n.append(l[:-1])
                break
            else:
                n.append(l)
        print(one_base(n))
main()