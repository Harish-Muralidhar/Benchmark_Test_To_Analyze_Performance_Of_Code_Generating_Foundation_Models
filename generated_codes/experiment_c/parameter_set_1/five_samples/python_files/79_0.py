"""

Explanation

In the first test case, there are n = 4 rows and k = 2.  The trap can be dropped at the following positions:


The trap will catch 0 bugs in the first position, 1 bug in the second position, 2 bugs in the third position, 4 bugs in the fourth position, 0 bugs in the fifth position, 0 bugs in the sixth position, 2 bugs in the seventh position, and 0 bugs in the eighth position.

"""


def TrapBug(n,k,arr):
    #n = int(n)
    #k = int(k)
    arr = [[int(x) for x in r.split()] for r in arr]
    for i in range(n-k+1):
        for j in range(n-k+1):
            num_of_bugs = []
            for p in range(i,k+i):
                for q in range(j,k+j):
                    num_of_bugs.append(arr[p][q])
            print(min(num_of_bugs),end =' ')
        print('\n')


if __name__ == '__main__':
    n = input()
    k = input()
    arr = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        arr.append(line)
    TrapBug(n,k,arr)