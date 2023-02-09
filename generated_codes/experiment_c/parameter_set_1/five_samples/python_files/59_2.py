"""

"""

from math import pow

from sys import stdin, stdout

mod = 1000000009

for _ in range(int(stdin.readline().strip())):

    n = int(stdin.readline())

    A = [int(i) for i in stdin.readline().strip().split()]

    cnt, temp, ans = 0, 0, 1

    for i in range(n-1, -1, -1):

        ai = A[i]

        cnt += pow(2, temp)

        if cnt > ai + 1:

            ans = 0

            break

        ans = (ans * ((ai - cnt + 1) % mod)) % mod

        temp += 1

    stdout.write(str(ans)+"\n")