'''



'''

# Write your code here

import sys

def gross_salary(salary):
    if salary < 1500:
        return salary + (salary * 0.1) + (salary * 0.9)
    else:
        return salary + 500 + (salary * 0.98)

if __name__ == "__main__":
    test_cases = int(sys.stdin.readline().strip())
    for i in range(test_cases):
        salary = int(sys.stdin.readline().strip())
        print(gross_salary(salary))