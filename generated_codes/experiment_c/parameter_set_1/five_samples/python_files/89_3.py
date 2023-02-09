"""

Explanation
The first system (index 1) protects houses from 1 to 4. The second system protects from 3 to 5. The enemy bombs house number 3. Then the first system remains protecting from 1 to 4 and the second one from 4 to 6. The enemy bombs house number 3 again.
"""

import sys
def main():
    n,m = map(int, input().split())
    a = {}
    for i in range(m):
        s = sys.stdin.readline().strip()
        if s[0] == 'P':
            u,v = map(int, s[2:].split())
            a[i] = [u,v]
        elif s[0] == 'M':
            i, d = map(int, s[2:].split())
            u, v = a[i-1]
            a[i] = [u+d,v+d]
        else:
            x = int(s[2:])
            c = 0
            for k in a:
                if a[k][0] <= x <= a[k][1]:
                    c += 1
            print(c)


if __name__ == '__main__':
    main()