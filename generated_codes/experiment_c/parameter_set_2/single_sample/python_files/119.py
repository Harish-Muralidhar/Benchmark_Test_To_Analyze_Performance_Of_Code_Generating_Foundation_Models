'''

Example case 2.
Is it possible to make N equal pieces?
No.
Is it possible to make N pieces?
Yes, you can cut 7 pieces with angles 1, 2, 3, 4, 5, 6, 7.
Is it possible to make N pieces, such that no two of them are equal?
Yes, you can cut 7 pieces with angles 1, 2, 3, 4, 5, 6, 7.

'''

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        if n == 1:
            print("y y y")
        elif n == 2:
            print("y y n")
        elif n == 3:
            print("y n n")
        else:
            print("n n n")

if __name__ == "__main__":
    main()