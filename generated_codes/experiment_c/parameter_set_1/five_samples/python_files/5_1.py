"""

"""

t = int(input())
for i in range(t):
    n = int(input())
    n_arr = list(map(int,input().split()))
    f_n = int(input())
    f_arr = list(map(int,input().split()))
    if(set(f_arr).issubset(set(n_arr))):
        print("Yes")
    else:
        print("No")