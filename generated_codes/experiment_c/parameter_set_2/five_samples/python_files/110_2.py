"""

"""
class Solution:
    def solve(self, A, E, V):
        if A==0 and E==0 and V==0:
            return 1
        if A==0 and E==0:
            return 0
        if A==0:
            if V>E:
                return 0
            else:
                return 1
        if E==0:
            if V>A:
                return 0
            else:
                return 1
        if V==0:
            return 1
        if V>A+E:
            return 0
        if V>A and V>E:
            return 0
        if V==A+E:
            return 1
        if V==A or V==E:
            return 1
        if V==A-1 or V==E-1:
            return 1
        if V==A+1 or V==E+1:
            return 2
        if V==A+2 or V==E+2:
            return 3
        if V==A+3 or V==E+3:
            return 4
        if V==A+4 or V==E+4:
            return 5
        if V==A+5 or V==E+5:
            return 6
        if V==A+6 or V==E+6:
            return 7
        if V==A+7 or V==E+7:
            return 8
        if V==A+8 or V==E+8:
            return 9
        if V==A+9 or V==E+9:
            return 10
        if V==A+10 or V==E+10:
            return 11
        if V==A+11 or V==E+11:
            return 12
        if V==A+12 or V==E+12:
            return 13
        if V==A+13 or V==E+13:
            return 14
        if V==A+14 or V==E+14:
            return 15
        if V==A+15 or V==E+15:
            return 16
        if V==A+16 or V==E+16:
            return 17
        if V