'''



'''

def get_sum_of_first_and_last_digit(num):
    first_digit = num % 10
    last_digit = 0
    
    while num > 0:
        last_digit = num
        num = num // 10
    
    return last_digit + first_digit