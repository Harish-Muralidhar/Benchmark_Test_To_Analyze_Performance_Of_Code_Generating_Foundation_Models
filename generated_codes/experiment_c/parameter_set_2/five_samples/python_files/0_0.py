"""
Hence, the answer is BWBW.
"""

for _ in range(int(input())):
    x = input()
    y = input()
    z = ''
    for i in range(len(x)):
        if x[i] == y[i]:
            z += 'B'
        else:
            z += 'W'
    print(z)