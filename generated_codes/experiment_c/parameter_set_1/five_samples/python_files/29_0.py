'''

'''

n = int(input())

for i in range(n):
    salary = int(input())
    if salary < 1500:
        gross = salary * (1 + 0.1 + 0.9)
    else:
        gross = salary + (500 + 0.98 * salary)
    print(round(gross,2))