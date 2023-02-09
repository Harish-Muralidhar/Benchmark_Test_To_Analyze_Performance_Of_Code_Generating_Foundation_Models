"""
"""

#code here
test = int(input())
for i in range(test):
    n = int(input())
    lst = list(map(int,input().split()))
    for j in range(1,len(lst)):
        if lst[j]>lst[j-1]:
            lst[j] = lst[j]-lst[j-1]
        else:
            lst[j-1] = lst[j-1]-lst[j]
    print(lst[-1])