"""

Solution:

"""

def get_subseq(seq):
    n = len(seq)
    print(n)
    res = []
    for i in range(2**n):
        res.append([seq[j] for j in range(n) if (i & (1<<j))])
    return res

def get_max_subseq():
    seq = [2, 3, 5, 7] 
    print(get_subseq(seq))

get_max_subseq()