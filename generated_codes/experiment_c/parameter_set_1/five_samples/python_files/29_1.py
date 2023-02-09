'''
'''

import sys

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def main():
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        exit(1)
    elif not is_number(sys.argv[1]):
        print("Argument must be an integer")
        exit(1)
    elif not is_int(sys.argv[1]):
        print("Argument must be an integer")
        exit(1)
    else:
        salary = int(sys.argv[1])
        if salary < 0:
            print("Argument must be a positive integer")
            exit(1)
        elif salary < 1500:
            hra = 0.1 * int(salary)
            da = 0.9 * int(salary)
        else:
            hra = 500
            da = 0.98 * int(salary)
        gross = hra + da + salary
        print("Gross salary: {0}".format(int(gross)))

if __name__ == '__main__':
    main()