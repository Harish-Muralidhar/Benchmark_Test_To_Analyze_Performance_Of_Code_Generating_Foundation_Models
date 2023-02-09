
A:

I think your logic is fine, I just wrote it in python.
<code>def prime_cross(l):
    return [i for i in range(1, min(l) + 1) if all(j % i == 0 for j in l)]

def num_primes(l):
    return len(prime_cross(l))

def solution(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                # get the continous ^ to the left
                l = 0
                while j - 1 - l &gt;= 0 and grid[i][j - 1 - l] == "^":
                    l += 1
                # get the continous ^ to the right
                r = 0
                while j + 1 + r &lt; len(grid[0]) and grid[i][j + 1 + r] == "^":
                    r += 1
                # get the continous ^ to the top
                t = 0
                while i - 1 - t &gt;= 0 and grid[i - 1 - t][j] == "^":
                    t += 1
                # get the continous ^ to the bottom
                b = 0
                while i + 1 + b &lt; len(grid) and grid[i + 1 + b][j] == "^":
                    b += 1
                # if the number of primes is even, it's a win for Kirito,
                # else it's a win for Asuna
                if num_primes([l, r, t, b]) % 2 == 0:
                    return "Kirito"
                else:
                    return "Asuna"
</code>
<code>print(solution([["^", "#", "^", "#", "^", "^", "^"],
                ["^", "#", "^", "^", "^", "#", "^"],
                ["^", "#", "^", "^", "^", "^", "^"],
                ["^", "^", "^", "^", "#", "^", "^"],
                ["^", "^", "^", "^", "^", "^", "^"],
                ["^", "^", "^", "^", "^", "^", "^"],
                ["^", "^", "^", "^", "^", "^", "^"]]))
</code>
returns <code>"Asuna"</code> which is the correct answer.
