'''



Explanation

In the first test case, employee 1 should get at least 10$ more than employee 2, and employee 2 should get at least 20$ more than employee 3, so employee 1 should get at least 30$ more than employee 3. Also, employee 2 should get at least 5$ more than employee 4, so employee 1 should get at least 35$ more than employee 4. So, the minimum total bonus is 460$. 

In the second test case, employee 1 should get at least 10$ more than employee 2, and employee 2 should get at least 10$ more than employee 3, so employee 1 should get at least 20$ more than employee 3. Also, employee 3 should get at least 10$ more than employee 1, so employee 3 should get at least 10$ more than employee 2. This is a contradiction, so it’s not possible to distribute bonus among them.

'''

# Write your code here

def get_min_bonus(n,m,l,comparisons):
    # Write your code here
    pass

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,m,l = map(int,input().split())
        comparisons = []
        for _ in range(m):
            comparisons.append(list(map(int,input().split())))
        print(get_min_bonus(n,m,l,comparisons))