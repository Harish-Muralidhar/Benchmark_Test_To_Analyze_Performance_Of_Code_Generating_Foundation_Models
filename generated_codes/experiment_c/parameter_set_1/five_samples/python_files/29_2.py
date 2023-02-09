'''

'''

import sys

def gross_salary(salary):
    if salary < 1500:
        return salary + salary * 0.1 + salary * 0.9
    else:
        return salary + 500 + salary * 0.98

def main():
    t = int(sys.stdin.readline())
    salary_list = [int(sys.stdin.readline()) for i in range(t)]
    for salary in salary_list:
        print(gross_salary(salary))

main()