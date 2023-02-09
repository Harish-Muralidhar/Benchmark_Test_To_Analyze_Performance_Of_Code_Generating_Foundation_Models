"""
"""

T = int(input())
for t in range(T):
    X = int(input())
    B = int(input())
    x_y = list(map(int,input().split()))
    x = [x_y[2*i] for i in range(B)]
    y = [x_y[2*i+1] for i in range(B)]
    C = int(input())
    p_q_r = list(map(int,input().split()))
    p = [p_q_r[3*i] for i in range(C)]
    q = [p_q_r[3*i+1] for i in range(C)]
    r = [p_q_r[3*i+2] for i in range(C)]

    min_chefs = max(y)
    for i in range(B):
        min_chefs = max(min_chefs, min(y[i],x[i]-x[i-1]))
        
    for i in range(C):
        d = x[-1] - p[i]
        chefs_needed = (d//q[i])*q[i] + q[i]
        min_chefs = max(min_chefs,chefs_needed)
    print(sum(y) + min_chefs)