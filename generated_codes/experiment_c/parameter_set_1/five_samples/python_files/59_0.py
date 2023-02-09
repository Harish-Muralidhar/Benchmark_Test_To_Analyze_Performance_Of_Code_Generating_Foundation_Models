'''

'''
def check_xor(x,y):
    global ans
    if x ^ y != 0:
        ans = 0
        return
    else:
        ans = 1

def check_less_equal(x,y):
    global ans
    if x > y:
        ans = 0
        return
    else:
        ans = 1

def get_total(x,y):
    global ans
    ans = ans ^ y
    return ans

for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    total_sum = 0
    for j in range(n):
        total_sum = get_total(total_sum,a[j])
        check_xor(a[j],total_sum)
        check_less_equal(total_sum,a[j])
    print(ans)