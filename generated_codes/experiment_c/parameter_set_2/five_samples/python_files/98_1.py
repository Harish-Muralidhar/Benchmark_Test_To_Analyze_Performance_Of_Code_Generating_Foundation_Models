
A:

I have solved this problem. I have used the concept of prime number. I have used the concept of prime number.
<code>def prime(n):
    if n &lt;= 1:
        return False
    if n &lt;= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i &lt;= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def check(r, c, arr):
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '^':
                l = 0
                r = 0
                t = 0
                b = 0
                flag = 0
                for k in range(j - 1, -1, -1):
                    if arr[i][k] == '^':
                        l += 1
                    else:
                        break
                for k in range(j + 1, c):
                    if arr[i][k] == '^':
                        r += 1
                    else:
                        break
                for k in range(i - 1, -1, -1):
                    if arr[k][j] == '^':
                        t += 1
                    else:
                        break
                for k in range(i + 1, r):
                    if arr[k][j] == '^':
                        b += 1
                    else:
                        break
                if prime(min(l, r, t, b)):
                    flag = 1
                if flag == 1:
                    return True
    return False

for _ in range(int(input())):
    r, c = map(int, input().split())
    arr = []
    for i in range(r):
        arr.append(input())
    if check(r, c, arr):
        print("Asuna")
    else:
        print("Kirito")
</code>
