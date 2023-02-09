'''

'''

# Write your code here

t=int(input())
for i in range(t):
    salary=int(input())
    if salary<1500:
        hra=salary*0.1
        da=salary*0.9
    else:
        hra=500
        da=salary*0.98
    gross_salary=salary+hra+da
    print(gross_salary)