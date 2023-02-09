"""
"""

def suraj_billing_problem(lst, n):
    if n == 1:
        return lst[0]
    if n == 2:
        return max(lst[0], lst[1])
    if n == 3:
        return max(lst[0] + lst[1], lst[2])
    
    return min(lst[-1] + suraj_billing_problem(lst[:-2], n-2),
               lst[-2] + suraj_billing_problem(lst[:-3], n-3))

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        lst = list(map(int, input().split()))
        lst.sort()
        print(suraj_billing_problem(lst, n))
        t -= 1