

A:

This is a very interesting question. I think the answer is no, no, no.
<code>def is_possible(n):
    return n &lt;= 360

def is_possible_equal(n):
    if n &lt;= 360:
        return 360 % n == 0
    else:
        return False

def is_possible_different(n):
    if n &lt;= 360:
        return 360 % n == 0
    else:
        return False

for _ in range(int(input())):
    n = int(input())
    print('y' if is_possible(n) else 'n', end=' ')
    print('y' if is_possible_equal(n) else 'n', end=' ')
    print('y' if is_possible_different(n) else 'n')
</code>
