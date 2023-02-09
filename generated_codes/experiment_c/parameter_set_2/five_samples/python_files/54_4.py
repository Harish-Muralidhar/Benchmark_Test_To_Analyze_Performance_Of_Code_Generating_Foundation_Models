"""

Solution:
"""

def find_arr(n,e,o):
    if o==0:
        if e==0:
            return [1]*n
        else:
            return [-1]
    if e==0:
        if o==0:
            return [1]*n
        else:
            return [-1]
    if e==1:
        if o==1:
            return [1,1,1]
        else:
            return [-1]
    if e==2:
        if o==2:
            return [1,1,1]
        else:
            return [-1]
    if e==3:
        if o==3:
            return [1,1,1]
        else:
            return [-1]
    if e==4:
        if o==4:
            return [1,1,1,1]
        else:
            return [-1]
    if e==5:
        if o==5:
            return [1,1,1,1,1]
        else:
            return [-1]
    if e==6:
        if o==6:
            return [1,1,1,1,1,1]
        else:
            return [-1]
    if e==7:
        if o==7:
            return [1,1,1,1,1,1,1]
        else:
            return [-1]
    if e==8:
        if o==8:
            return [1,1,1,1,1,1,1,1]
        else:
            return [-1]
    if e==9:
        if o==9:
            return [1,1,1,1,1,1,1,1,1]
        else:
            return [-1]
    if e==10:
        if o==10:
            return [1,1,1,1,1,1,1,1,1,1]
        else:
            return [-1]
    if e==11:
        if o==11:
            return [1,1