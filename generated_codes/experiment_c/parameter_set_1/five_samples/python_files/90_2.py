'''
There are no two barricades with the same coordinates.

'''

w,h,d,n = map(int,input().split())
barricades = []
for k in range(n):
    barricades.append(list(map(int,input().split())))

d = int(d)
mid_x = int(w/2)
mid_y = int(h/2)

points = []
for i in range(mid_x-d,mid_x+d+1):
    for j in range(mid_y-d,mid_y+d+1):
        if i == mid_x-d or i == mid_x+d or j == mid_y-d or j == mid_y+d:
            points.append([i,j])

cost = 0
for k in points:
    for i in barricades:
        if i[0] == k[0] and i[1] == k[1]:
            cost = cost + i[2]

print(cost)