"""

"""

import fractions

def max_fraction(a,b):
    #print(a,b)
    if len(a)==1:
        return a[0],b[0]
    else:
        max_num = a[0]
        max_den = b[0]
        for i in range(1,len(a)):
            max_num = max_num + a[i]
            max_den = max_den + b[i]
        return max_num,max_den

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = []
        b = []
        for j in range(n):
            num,den = input().split("/")
            a.append(int(num))
            b.append(int(den))
        for j in range(n):
            max_num,max_den = max_fraction(a[j:],b[j:])
            gcd = fractions.gcd(max_num,max_den)
            print(str(max_num//gcd)+"/"+str(max_den//gcd))
        print()

if __name__ == '__main__':
    main()