

A:

I think the best way to do this is to loop through all the angles and check if you can.  Then, if you can make all the pieces, check the gcd of the angles and see if they are equal.  If they are, it's possible to make N pieces of different sizes, if they aren't, it's not possible.  You can't use a gcd check by itself because a gcd of 1 doesn't necessarily mean that all the pieces have the same size.  (e.g. If you have 10 pieces with angles 1, 11, 21, ... 91, you have a gcd of 1, but the pieces are not the same size.
Python Code:
<code>from fractions import gcd

def all_pieces(n, angle):
    return sum([(360/angle) for i in range(n)]) == 360

def different_pieces(n, angle):
    return gcd(angle, 360/n) == 1

def equal_pieces(n, angle):
    return sum([(360/angle) for i in range(n)]) == 360 and gcd(angle, 360/n) &gt; 1

# T is the number of tests
T = int(input())

for i in range(T):
    N = int(input())
    equal = False
    different = False
    all = False
    for angle in range(1, 360-N):
        if all_pieces(N, angle):
            all = True
        if different_pieces(N, angle):
            different = True
        if equal_pieces(N, angle):
            equal = True
    print("y" if equal else "n", end=' ')
    print("y" if all else "n", end=' ')
    print("y" if different else "n")
</code>
